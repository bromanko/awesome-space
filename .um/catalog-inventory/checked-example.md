> **Saved-check reclassification — not a new workflow run.** Existing link-check logs were evaluated with the updated classifier. No model calls or fresh network checks were made. The correction remains held because its retained Celestia Motherlode link failed verification. The unchanged NASA link fluctuated between checks and is now recorded as an unrelated website failure, rather than attributed to the patch.

# One-entry integration example

Saved initial research was reused. Prior discussion collection, Opus history review, patch validation and report rendering ran through the current production code. This is not a full catalog run.

# Catalog review

**0 ready for review · 1 held**

1 checked · 0 unchanged · 1 saved assessment reused · 0 source checks unavailable

<h2>Celestia — Held</h2>

<p>related: I ran six searches across orbitalindex/awesome-space and bromanko/awesome-space for &quot;Celestia&quot;, &quot;https://celestia.space/&quot; and &quot;https://celestiaproject.space/&quot;. They returned one record: PR #43, &quot;Fixed Celestia &#x27;Motherlode&#x27; typos&quot;. That PR was merged on 2020-09-30. Its patch only fixed spelling in the description (&quot;Motherload&quot;→&quot;Motherlode&quot;, &quot;addons&quot;→&quot;add-ons&quot;) and left the Celestia URL as https://celestia.space/. It does not move the link to https://celestiaproject.space/, and no maintainer objected to such a change. This makes it useful context, not a duplicate, rejection or obsolete match. The proposed description is the same as the current corrected text, so #43 does not conflict with it. No open PR in the searched records proposes the domain change. The search results were marked complete. Proposed edit failed checks; held for maintainer review. See validation logs.</p>

<details>
<summary>Show held diff</summary>

```diff
--- a/README.md
+++ b/README.md
@@ -67,7 +67,7 @@
 
 * [100,000 Stars](https://stars.chromeexperiments.com/) - 100,000 Stars is an interactive visualization of the stellar neighborhood showing the location of 119,617 nearby stars.
 * [ANISE](https://github.com/nyx-space/anise) - ANISE provides a toolkit and files for Attitude, Navigation, Instrument, Spacecraft, and Ephemeris data. It's a modern replacement of the NAIF SPICE toolkit.
-* [Celestia](https://celestia.space/) - Free real-time 3D visualization of space. (See also [Celestia Motherlode](http://www.celestiamotherlode.net/) for many add-ons.)
+* [Celestia](https://celestiaproject.space/) - Free real-time 3D visualization of space. (See also [Celestia Motherlode](http://www.celestiamotherlode.net/) for many add-ons.)
 * [Cesium.js](https://cesiumjs.org/) - An open-source JavaScript library for world-class 3D globes and maps
 * [Cosmic Timeline](https://cosmic-timeline.netlify.app/) - Interactive journey through the history of the universe, from the Planck epoch to today, with the physical values at each instant computed from the Planck 2018 cosmological model.
 * [Gaia Sky](https://zah.uni-heidelberg.de/institutes/ari/gaia/outreach/gaiasky/) - Real-time, 3D, astronomy visualization software developed in the framework of ESA's Gaia mission. Runs on Windows, Linux and macOS.
```

</details>

<details>
<summary>Evidence and checks</summary>

<p>celestia.space no longer belongs to the project. It now resolves to 0.0.0.0, uses abovedomains.com nameservers, and its Oct 2026 Wayback snapshot is a parked &#x27;This domain may be for sale&#x27; page. The official CelestiaProject/Celestia GitHub repo (active, pushed 2026-11-09) lists https://celestiaproject.space as its homepage. The Celestia Motherlode link is still a live add-on repository and should stay as it is.</p>

<p>https://celestia.space/ — DNS gives 0.0.0.0 and the connection is refused. NS records are ns1/ns2.abovedomains.com.</p>

<p>http://web.archive.org/web/20261005071525/https://celestia.space/ — Archived 2026-10-05: &#x27;celestia.space … This domain may be for sale.&#x27;</p>

<p>https://github.com/CelestiaProject/Celestia — GitHub API: full_name CelestiaProject/Celestia, not archived, pushed 2026-11-09, description &#x27;Real-time 3D visualization of space.&#x27;, homepage https://celestiaproject.space.</p>

<p>https://celestiaproject.space/ — HTTP 200 but behind an Anubis proof-of-work bot check, so the page body couldn&#x27;t be read with curl.</p>

<p>http://www.celestiamotherlode.net/ — HTTP 200: &#x27;The Celestia Motherlode is a repository for various addons like textures, models or celestial objects for Celestia … hosts over 10 GB of Celestia addons&#x27;.</p>

<p>Caveats: Couldn&#x27;t read the celestiaproject.space content because of the bot check. Ownership is supported by the official GitHub repo&#x27;s homepage field.; Motherlode is http-only.</p>

<p>related: I ran six searches across orbitalindex/awesome-space and bromanko/awesome-space for &quot;Celestia&quot;, &quot;https://celestia.space/&quot; and &quot;https://celestiaproject.space/&quot;. They returned one record: PR #43, &quot;Fixed Celestia &#x27;Motherlode&#x27; typos&quot;. That PR was merged on 2020-09-30. Its patch only fixed spelling in the description (&quot;Motherload&quot;→&quot;Motherlode&quot;, &quot;addons&quot;→&quot;add-ons&quot;) and left the Celestia URL as https://celestia.space/. It does not move the link to https://celestiaproject.space/, and no maintainer objected to such a change. This makes it useful context, not a duplicate, rejection or obsolete match. The proposed description is the same as the current corrected text, so #43 does not conflict with it. No open PR in the searched records proposes the domain change. The search results were marked complete. Proposed edit failed checks; held for maintainer review. See validation logs.</p>

</details>

<details>
<summary>Saved review baseline</summary>

0 new completed reviews · 1 pending.

To retain completed reviews, review and commit the bundled `baseline.json` as `.um/freshness/baseline.json`.

</details>

<details>
<summary>Full research and run details</summary>

# Freshness research

Advisory only; every suggested change requires maintainer review.
No list edits, PRs, comments, or reviews were submitted.

Catalog revision: `66d4217e6bf0858ae59f99a8d382e282cd2ea5a3`
Scope: one saved-research entry; not a full catalog run
Catalog recheck: unchanged

Sources below are agent-reported observations, not independent verification.

## Entry 70

<pre>Celestia

celestia.space no longer belongs to the project. It now resolves to 0.0.0.0, uses abovedomains.com nameservers, and its Oct 2026 Wayback snapshot is a parked &#x27;This domain may be for sale&#x27; page. The official CelestiaProject/Celestia GitHub repo (active, pushed 2026-11-09) lists https://celestiaproject.space as its homepage. The Celestia Motherlode link is still a live add-on repository and should stay as it is.

https://celestia.space/
DNS gives 0.0.0.0 and the connection is refused. NS records are ns1/ns2.abovedomains.com.
http://web.archive.org/web/20261005071525/https://celestia.space/
Archived 2026-10-05: &#x27;celestia.space … This domain may be for sale.&#x27;
https://github.com/CelestiaProject/Celestia
GitHub API: full_name CelestiaProject/Celestia, not archived, pushed 2026-11-09, description &#x27;Real-time 3D visualization of space.&#x27;, homepage https://celestiaproject.space.
https://celestiaproject.space/
HTTP 200 but behind an Anubis proof-of-work bot check, so the page body couldn&#x27;t be read with curl.
http://www.celestiamotherlode.net/
HTTP 200: &#x27;The Celestia Motherlode is a repository for various addons like textures, models or celestial objects for Celestia … hosts over 10 GB of Celestia addons&#x27;.

Blocking uncertainties:
None reported.

Informational caveats:
Couldn&#x27;t read the celestiaproject.space content because of the bot check. Ownership is supported by the official GitHub repo&#x27;s homepage field.
Motherlode is http-only.

Recommendation: update
Proposed name: None
Proposed URL: https://celestiaproject.space/
Proposed description: Free real-time 3D visualization of space. (See also [Celestia Motherlode](http://www.celestiamotherlode.net/) for many add-ons.)</pre>


</details>

Proposals only; no catalog edits or PRs submitted. Full records and checked patches are in the run artifacts.
