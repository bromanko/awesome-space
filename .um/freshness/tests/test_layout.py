"""Guard actual catalog coverage and preservation of its authored layout."""
from pathlib import Path
import hashlib
import re
import sys
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import ci
import catalog

class LayoutTests(unittest.TestCase):
    def test_every_external_resource_bullet_is_represented(self):
        text=Path('README.md').read_text()
        expected=[str(n) for n,line in enumerate(text.splitlines(),1)
                  if re.match(r'^\s*[-*+] ',line) and re.search(r'\[[^]]+\]\(https?://',line)]
        rows=ci.entries(text)
        self.assertEqual([r['id'] for r in rows],expected)
        self.assertEqual(len({catalog.key(r) for r in rows}),len(rows))

    def proposal(self,text):
        entry=ci.entries(text)[0]
        data=dict(entries=[entry],readme=text,readmeHash=hashlib.sha256(text.encode()).hexdigest(),catalogSha='a'*40)
        row=dict(id=entry['id'],action='update',reason='Official documentation.',evidence=[dict(url=entry['url'],observation='Updated wording.')],blockers=[],limitations=[],newName=None,newUrl=None,newDescription='Corrected wording.')
        return ci.previews(data,dict(results=[row]),'unchanged')[0]

    def test_indentation_bullet_and_separator_survive(self):
        for line in ['  - [Tool](https://example.com) -- Original.','* [Tool](https://example.com) : Original.','* [Tool](https://example.com) – Original.']:
            proposal=self.proposal('# Tools\n'+line+'\n')[0]
            self.assertIn('+'+line.replace('Original.','Corrected wording.'),proposal['patch'])

    def test_compound_entry_is_researched_but_not_rewritten(self):
        text='# Hardware\n* Radio [hardware](https://example.com/hw) and [firmware](https://example.com/sw) - A radio.\n'
        entry=ci.entries(text)[0]
        self.assertEqual(entry['sourceUrls'],['https://example.com/hw','https://example.com/sw'])
        self.assertFalse(entry['editable'])
        self.assertEqual(self.proposal(text),[])

    def test_linked_companion_must_have_a_complete_snapshot(self):
        entry=dict(url='https://example.com/hw',sourceUrls=['https://example.com/hw','https://example.com/sw'])
        with patch.object(catalog,'get_url',side_effect=[('https://example.com/hw',b'hw'),OSError('unavailable')]):
            self.assertFalse(catalog.snapshot(entry)['complete'])

    def test_descriptionless_resources_are_not_skipped(self):
        entry=ci.entries('# Data\n* [Archive](https://example.com)\n')[0]
        self.assertFalse(entry['editable'])
        self.assertEqual(entry['name'],'Archive')
