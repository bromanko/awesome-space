# Catalog review inventory

**63 proposed changes · 12 uncertain · 37 unresolved keeps**

210 entries researched. 98 saved reviews for recurring runs.

Research recommendations from the initial Opus review. The full set has not passed prior-discussion or patch validation. Proposed diffs are previews, not approved patches. Nothing was applied or submitted.

Catalog: `659f9ff6a55682f8ee138b60d5c4f6029a729fa1` · README SHA-256: `29fdbe683bded6dcb221cadc5513c10571701cdab5278e3babe34b669f18b175`

## Proposed changes

<h3>AstroBin API — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -51,7 +51,7 @@
 
 ### Astronomy APIs
 
-* [AstroBin API](http://www.astrobin.com/help/api/) - AstroBin is an image hosting website specifically targeted to astrophotographers. Its API offers a basic set of RESTful endpoints. Currently the API is read-only, and  allows you to get data about images, and perform basic searches.
+* [AstroBin API](https://welcome.astrobin.com/application-programming-interface) - AstroBin is an image hosting website specifically targeted to astrophotographers. Its API offers a basic set of RESTful endpoints. Currently the API is read-only, and allows you to get data about images, and perform basic searches.
 * [astrometry.net](http://astrometry.net/) - "If you have astronomical imaging of the sky with celestial coordinates you do not know—or do not trust—then Astrometry.net is for you. Input an image and we'll give you back astrometric calibration meta-data, plus lists of known objects falling inside the field of view."
 * [Markarian Multiwavelength Data Center (MMDC)](https://mmdc.am/) - Multiwavelength SEDs and light curves of blazars from archival catalogues and new Swift, NuSTAR and Fermi-LAT analyses, with a REST API, a Python client ([astro-mmdc](https://github.com/icranet/astro-mmdc)) and SSC/EIC/hadronic modeling.
 * [Open Astronomy Catalog API](https://astrocats.space/) - The Open Astronomy Catalog API (OACAPI) offers a lightweight, simple way to access data available via the Open Astronomy Catalogs (e.g. the Open Supernova, Tidal Disruption, Kilonova, and Fast Stars Catalogs).
```

<details>
<summary>Evidence and limitations</summary>

<p>The description is still accurate. AstroBin&#x27;s official API page still says the API is a basic, read-only set of RESTful endpoints for getting image data and doing basic searches. The listed http://www.astrobin.com/help/api/ now permanently redirects to AstroBin&#x27;s own page at welcome.astrobin.com, so this is a URL-only update.</p>

<p>http://www.astrobin.com/help/api/ — curl -L resolves to https://welcome.astrobin.com/application-programming-interface (HTTP 200).</p>

<p>https://welcome.astrobin.com/application-programming-interface — Page title &#x27;AstroBin&#x27;s read-only API&#x27;: &#x27;AstroBin implements a basic set of RESTful APIs. Currently, the APIs are read-only, and they allow you to get data about images, and perform some basic searches.&#x27; It also gives example endpoints under https://www.astrobin.com/api/v1/ and says XML and JSON responses are supported.</p>

<p>Caveats: Did not request an API key or call the endpoints.; The double space in &#x27;and  allows&#x27; in the current description could be fixed at the same time.</p>

<p>Independent source check: Official old URL redirects to the proposed API page, which confirms basic read-only image data and searches. Valid URL cleanup; proposed prose only repairs spacing.</p>

<p>http://www.astrobin.com/help/api/ — Redirect to official welcome.astrobin.com API page observed.</p>

<p>https://welcome.astrobin.com/application-programming-interface — Read-only API capabilities directly documented.</p>

</details>

<h3>Open Astronomy Catalog API — remove</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -54,7 +54,6 @@
 * [AstroBin API](http://www.astrobin.com/help/api/) - AstroBin is an image hosting website specifically targeted to astrophotographers. Its API offers a basic set of RESTful endpoints. Currently the API is read-only, and  allows you to get data about images, and perform basic searches.
 * [astrometry.net](http://astrometry.net/) - "If you have astronomical imaging of the sky with celestial coordinates you do not know—or do not trust—then Astrometry.net is for you. Input an image and we'll give you back astrometric calibration meta-data, plus lists of known objects falling inside the field of view."
 * [Markarian Multiwavelength Data Center (MMDC)](https://mmdc.am/) - Multiwavelength SEDs and light curves of blazars from archival catalogues and new Swift, NuSTAR and Fermi-LAT analyses, with a REST API, a Python client ([astro-mmdc](https://github.com/icranet/astro-mmdc)) and SSC/EIC/hadronic modeling.
-* [Open Astronomy Catalog API](https://astrocats.space/) - The Open Astronomy Catalog API (OACAPI) offers a lightweight, simple way to access data available via the Open Astronomy Catalogs (e.g. the Open Supernova, Tidal Disruption, Kilonova, and Fast Stars Catalogs).
 * [SpaceXDB-Api](https://github.com/R4yGM/SpaceXDB-Api) - [SpaceXDB](https://www.spacexdb.cf) is a website containing SpaceX launch information and telemetry.
 
 ### Astronomy Software
```

<details>
<summary>Evidence and limitations</summary>

<p>The official site says the Open Astronomy Catalogs and the API (OACAPI, api.astrocats.space) have been permanently retired and are no longer online, and the API host now returns HTTP 410 Gone. The site points to the astrocatalogs GitHub organization for the catalog data and software. That is an archive, not a successor API, so it doesn&#x27;t qualify for &#x27;replace&#x27; in the Astronomy APIs section.</p>

<p>https://astrocats.space/ — Page title &#x27;Open Astronomy Catalogs — shut down&#x27;. It says the website (including the Open Supernova, Tidal Disruption, Kilonova, Nova, Black Hole and Fast Stars catalogs and all subdomains) and the Open Astronomy Catalog API (OACAPI, api.astrocats.space) &#x27;have been permanently retired and are no longer online&#x27;. It says the data and software remain on GitHub, and that astroquery.oac is being removed from astroquery (astropy/astroquery#3686).</p>

<p>https://api.astrocats.space/ — Returns HTTP/1.1 410 Gone.</p>

<p>Caveats: A maintainer could instead choose to list the astrocatalogs GitHub organization as a data archive in a data section. That would be a new entry, not a successor to the API.</p>

<p>Independent source check: Official shutdown notice explicitly includes OACAPI and its host, and says data/software remain on GitHub. An archival dataset is not a functioning replacement API.</p>

<p>https://astrocats.space/ — Official page directly states permanent retirement of website andAPI.</p>

</details>

<h3>Cesium.js — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -68,7 +68,7 @@
 * [100,000 Stars](https://stars.chromeexperiments.com/) - 100,000 Stars is an interactive visualization of the stellar neighborhood showing the location of 119,617 nearby stars.
 * [ANISE](https://github.com/nyx-space/anise) - ANISE provides a toolkit and files for Attitude, Navigation, Instrument, Spacecraft, and Ephemeris data. It's a modern replacement of the NAIF SPICE toolkit.
 * [Celestia](https://celestia.space/) - Free real-time 3D visualization of space. (See also [Celestia Motherlode](http://www.celestiamotherlode.net/) for many add-ons.)
-* [Cesium.js](https://cesiumjs.org/) - An open-source JavaScript library for world-class 3D globes and maps
+* [CesiumJS](https://cesium.com/platform/cesiumjs/) - An open-source JavaScript library for world-class 3D globes and maps
 * [Cosmic Timeline](https://cosmic-timeline.netlify.app/) - Interactive journey through the history of the universe, from the Planck epoch to today, with the physical values at each instant computed from the Planck 2018 cosmological model.
 * [Gaia Sky](https://zah.uni-heidelberg.de/institutes/ari/gaia/outreach/gaiasky/) - Real-time, 3D, astronomy visualization software developed in the framework of ESA's Gaia mission. Runs on Windows, Linux and macOS.
 * [Harmony of the Spheres](https://github.com/TheHappyKoala/Harmony-of-the-Spheres) - Newtonian gravity and space simulator that runs in your browser
```

<details>
<summary>Evidence and limitations</summary>

<p>cesiumjs.org now redirects to the cesium.com company homepage rather than to the library. The official product page is cesium.com/platform/cesiumjs/ and names the library &#x27;CesiumJS&#x27;. It describes &#x27;an open source JavaScript library for creating world-class 3D globes and maps&#x27;, so the description is still accurate.</p>

<p>https://cesiumjs.org/ — curl -L resolves to https://cesium.com/ (the company homepage).</p>

<p>https://cesium.com/platform/cesiumjs/ — &#x27;CesiumJS is an open source JavaScript library for creating world-class 3D globes and maps…&#x27; It is released under Apache 2.0 and installed with npm install cesium.</p>

<p>Caveats: Changing the name from &#x27;Cesium.js&#x27; to &#x27;CesiumJS&#x27; only matches the official spelling. Whether to rename is a maintainer choice.</p>

<p>Independent source check: Old domain resolves to the company homepage. Dedicated official CesiumJS product page directly supports name, open-sourceJavaScript and3Dglobe/map purpose. Valid more-specific destination.</p>

<p>https://cesiumjs.org/ — Redirect to cesium.com observed.</p>

<p>https://cesium.com/platform/cesiumjs/ — Official library identity and capabilities verified.</p>

</details>

<h3>KStars — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -72,7 +72,7 @@
 * [Cosmic Timeline](https://cosmic-timeline.netlify.app/) - Interactive journey through the history of the universe, from the Planck epoch to today, with the physical values at each instant computed from the Planck 2018 cosmological model.
 * [Gaia Sky](https://zah.uni-heidelberg.de/institutes/ari/gaia/outreach/gaiasky/) - Real-time, 3D, astronomy visualization software developed in the framework of ESA's Gaia mission. Runs on Windows, Linux and macOS.
 * [Harmony of the Spheres](https://github.com/TheHappyKoala/Harmony-of-the-Spheres) - Newtonian gravity and space simulator that runs in your browser
-* [KStars](https://edu.kde.org/kstars/) - KStars is free, open source, cross-platform astronomy software. It provides many features, including a graphical simulation of the night sky, observing planner, a sky calendar tool, an FOV editor, and more.
+* [KStars](https://kstars.kde.org/) - KStars is free, open source, cross-platform astronomy software. It provides many features, including a graphical simulation of the night sky, observing planner, a sky calendar tool, an FOV editor, and more.
 * [LeoLabs Visualization](https://platform.leolabs.space/visualization) - Low Earth Orbit Catalog Visualization.
 * [Mars Now](https://mars.nasa.gov/explore/mars-now/) - This visualization shows the current location and communication activity of all operating landers, rovers and orbiters at Mars that transmit data to Earth via NASA’s Mars Relay Network.
 * [NASA Eyes](https://eyes.nasa.gov/) - Immersible apps to explore the Earth and solar system
```

<details>
<summary>Evidence and limitations</summary>

<p>The description is accurate. KStars is still free, open-source and cross-platform (version 3.8.5 released 3 October 2026), and its features page lists the sky simulation, Observation Planner, Sky Calendar tool and FOV tools. The listed edu.kde.org/kstars/ now redirects to the official site kstars.kde.org, so this is a URL-only update.</p>

<p>https://edu.kde.org/kstars/ — curl -L resolves to https://kstars.kde.org/ (200).</p>

<p>https://kstars.kde.org/ — &#x27;KStars Version 3.8.5 (released on 3 October 2026)&#x27;. Downloads for Windows, macOS and Linux. &#x27;Graphical simulation of the sky…&#x27;, &#x27;Powerful observation planner&#x27;.</p>

<p>https://kstars.kde.org/features/ — Lists the &#x27;Sky Calendar tool to see how the planets move across the sky&#x27;, &#x27;Observation Planner&#x27;, the &#x27;FOV calculator&#x27;, and field-of-view symbols computed from eyepiece and telescope.</p>

<p>Caveats: The name &#x27;FOV editor&#x27; in the description doesn&#x27;t appear word for word, but the FOV symbol and calculator features exist.</p>

<p>Independent source check: Current KDE product/features pages support the existing description and new official destination. This audit could not directly read the old edu.kde URL, so its exact redirect remains model-reported rather than independently verified.</p>

<p>https://kstars.kde.org/features/ — Official feature list read.</p>

<p>https://edu.kde.org/kstars/ — Web-tool direct fetch unavailable; no independent redirect verification.</p>

</details>

<h3>Mars Now — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -74,7 +74,7 @@
 * [Harmony of the Spheres](https://github.com/TheHappyKoala/Harmony-of-the-Spheres) - Newtonian gravity and space simulator that runs in your browser
 * [KStars](https://edu.kde.org/kstars/) - KStars is free, open source, cross-platform astronomy software. It provides many features, including a graphical simulation of the night sky, observing planner, a sky calendar tool, an FOV editor, and more.
 * [LeoLabs Visualization](https://platform.leolabs.space/visualization) - Low Earth Orbit Catalog Visualization.
-* [Mars Now](https://mars.nasa.gov/explore/mars-now/) - This visualization shows the current location and communication activity of all operating landers, rovers and orbiters at Mars that transmit data to Earth via NASA’s Mars Relay Network.
+* [Mars Relay Network](https://eyes.nasa.gov/apps/mrn/) - This visualization shows the current location and communication activity of all operating landers, rovers and orbiters at Mars that transmit data to Earth via NASA’s Mars Relay Network.
 * [NASA Eyes](https://eyes.nasa.gov/) - Immersible apps to explore the Earth and solar system
 * [Orb Viewer](https://parsecsreach.com/orbviewer) - Visualization of all the asteroids in the MPC database.
 * [Orbit Simulator](http://www.orbitsimulator.com/gravity/articles/what.html) - A powerful numerical integration tool. "By performing n-body simulations, you can study the orbits of planets, moons, asteroids, or any object in the universe."
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed mars.nasa.gov &#x27;Mars Now&#x27; URL now redirects to NASA&#x27;s Eyes app at eyes.nasa.gov/apps/mrn/, which is titled &#x27;Mars Relay Network&#x27;. NASA&#x27;s Eyes index describes that app as &#x27;Track real-time communications on Mars&#x27;. The description is still accurate; the name and URL should match the current official app.</p>

<p>https://mars.nasa.gov/explore/mars-now/ — curl -L resolves to https://eyes.nasa.gov/apps/mrn/ (200).</p>

<p>https://eyes.nasa.gov/apps/mrn/ — Title &#x27;Mars Relay Network - NASA/JPL&#x27;, &#x27;Powered by NASA&#x27;s EYES&#x27;. Meta description &#x27;NASA Mars Relay Network visualization tool.&#x27;, og:title &#x27;Mars Relay Network&#x27;.</p>

<p>https://science.nasa.gov/eyes/ — The Eyes app list includes &#x27;Mars Relay Network: Track real-time communications on Mars&#x27;.</p>

<p>Caveats: Did not load the interactive app to confirm exactly which spacecraft it currently shows.</p>

<p>Independent source check: Old NASA URL directly redirects to the Mars Relay Network app; NASA Eyes index names it and describes mission-communication visualization. Renaming/linking is supported. Exact all-spacecraft coverage was not independently executed or checked.</p>

<p>https://mars.nasa.gov/explore/mars-now/ — Redirect to eyes.nasa.gov/apps/mrn observed.</p>

<p>https://eyes.nasa.gov/apps/mrn/ — App title Mars Relay Network.</p>

<p>https://science.nasa.gov/eyes/ — Official index describes Mars mission communications.</p>

</details>

<h3>NASA Eyes — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -75,7 +75,7 @@
 * [KStars](https://edu.kde.org/kstars/) - KStars is free, open source, cross-platform astronomy software. It provides many features, including a graphical simulation of the night sky, observing planner, a sky calendar tool, an FOV editor, and more.
 * [LeoLabs Visualization](https://platform.leolabs.space/visualization) - Low Earth Orbit Catalog Visualization.
 * [Mars Now](https://mars.nasa.gov/explore/mars-now/) - This visualization shows the current location and communication activity of all operating landers, rovers and orbiters at Mars that transmit data to Earth via NASA’s Mars Relay Network.
-* [NASA Eyes](https://eyes.nasa.gov/) - Immersible apps to explore the Earth and solar system
+* [NASA Eyes](https://science.nasa.gov/eyes/) - Immersive real-time 3D web apps to explore the Earth, the solar system and beyond
 * [Orb Viewer](https://parsecsreach.com/orbviewer) - Visualization of all the asteroids in the MPC database.
 * [Orbit Simulator](http://www.orbitsimulator.com/gravity/articles/what.html) - A powerful numerical integration tool. "By performing n-body simulations, you can study the orbits of planets, moons, asteroids, or any object in the universe."
 * [Orbiter 2016](http://orbit.medphys.ucl.ac.uk/) - Open source spaceflight simulator with many addons for historical missions. [Installation Instructions.](https://www.reddit.com/r/Orbiter/comments/mx2mjz/guide_for_beginners_to_orbiter/)
```

<details>
<summary>Evidence and limitations</summary>

<p>NASA&#x27;s Eyes is still a live suite of 3D web apps covering Earth, the solar system, asteroids and exoplanets. eyes.nasa.gov now redirects to the official landing page at science.nasa.gov/eyes/. The description&#x27;s &#x27;Immersible&#x27; is a word error; NASA describes the suite as &#x27;immersive real-time 3D web-based apps&#x27;. This makes a small wording fix and updates the URL to the redirect target.</p>

<p>https://eyes.nasa.gov/ — curl -L resolves to https://science.nasa.gov/eyes/ (200).</p>

<p>https://science.nasa.gov/eyes/ — &#x27;NASA&#x27;s Eyes Experience Earth, our solar system, nearby asteroids, the universe, and the spacecraft exploring them with immersive real-time 3D web-based apps.&#x27; Apps listed: Eyes on the Solar System, Asteroids, Earth, Exoplanets, DSN Now and Mars Relay Network.</p>

<p>Caveats: eyes.nasa.gov still works as a redirect and hosts the apps. Keeping the old URL is acceptable if the maintainer prefers the shorter domain.</p>

<p>Independent source check: Official redirect and immersive3D visualization wording support the new URL and Immersible typo repair. Small correction rather than substantive change of purpose.</p>

<p>https://eyes.nasa.gov/ — Redirect to science.nasa.gov/eyes observed.</p>

<p>https://science.nasa.gov/eyes/ — Official descriptions support immersive3D web apps.</p>

</details>

<h3>SpaceXDB-Api — update</h3>

<p>0 proposed change(s); 1 held for unresolved questions.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The GitHub repo R4yGM/SpaceXDB-Api now redirects to R4yGM/SpaceXTelemetry-Api. The linked site www.spacexdb.cf no longer resolves in DNS and has no Wayback snapshot. The README says the .cf domain no longer works and points to the GitHub Pages API (r4ygm.github.io/SpaceXTelemetry-Api), which still serves data. The SpaceXDB collection now lives at r4yan.gitbook.io/spacexdb. The dataset is historic: the &#x27;latest&#x27; launch is ANASIS-II from 2020, and the repo was last pushed in 2021.</p>

<p>https://github.com/R4yGM/SpaceXDB-Api — Redirects to https://github.com/R4yGM/SpaceXTelemetry-Api. GitHub API: full_name R4yGM/SpaceXTelemetry-Api, not archived, pushed 2021-06-12, description &#x27;SpaceXTelemetry API - Open Source REST API for telemetry and predictions to rocket launches&#x27;, homepage https://r4ygm.github.io/SpaceXTelemetry-Api/.</p>

<p>https://raw.githubusercontent.com/R4yGM/SpaceXTelemetry-Api/master/README.md — &#x27;used in https://r4yan.gitbook.io/spacexdb/&#x27;. It also says &#x27;http://spacextelemetry.cf domain is not working anymore use https://r4ygm.github.io/SpaceXTelemetry-Api/&#x27;.</p>

<p>https://r4ygm.github.io/SpaceXTelemetry-Api/launch/latest.json — HTTP 200. Returns {&quot;mission_name&quot;: &quot;ANASIS-II&quot;, &quot;telemetry&quot;: [...]}.</p>

<p>https://r4yan.gitbook.io/spacexdb — Title &#x27;SpaceXDB&#x27;. A collection of SpaceX launch telemetry (Crew Dragon DM-2, Starlink 5–9, GPS III SV03, ANASIS-II) and says it also provides an API.</p>

<p>Caveats: www.spacexdb.cf: no DNS answer and no Wayback snapshot. Its original content couldn&#x27;t be checked.; The data covers only a few 2020 launches. It is useful as a historic dataset.</p>

<p>Independent source check: Official repository README verifies SpaceXTelemetry-Api identity, SpaceXDB affiliation and replacement APIhost after a dead.cf domain. GitBook/current endpoint could not be independently read here; exact2020-only dataset scope and old-domain DNS claims remain unverified. Keep qualified and avoid promoting the full proposed prose as checked.</p>

<p>https://github.com/R4yGM/SpaceXTelemetry-Api/blob/master/README.md — Repository name, GitBook affiliation and oldAPIhost replacement documented; blobf09d323a750c78ae1b284d869cf8bf38dfa576d8.</p>

<p>https://r4yan.gitbook.io/spacexdb/ — Direct web-tool fetch unavailable.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Celestia — update</h3>

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

<details>
<summary>Evidence and limitations</summary>

<p>celestia.space no longer belongs to the project. It now resolves to 0.0.0.0, uses abovedomains.com nameservers, and its Oct 2026 Wayback snapshot is a parked &#x27;This domain may be for sale&#x27; page. The official CelestiaProject/Celestia GitHub repo (active, pushed 2026-11-09) lists https://celestiaproject.space as its homepage. The Celestia Motherlode link is still a live add-on repository and should stay as it is.</p>

<p>https://celestia.space/ — DNS gives 0.0.0.0 and the connection is refused. NS records are ns1/ns2.abovedomains.com.</p>

<p>http://web.archive.org/web/20261005071525/https://celestia.space/ — Archived 2026-10-05: &#x27;celestia.space … This domain may be for sale.&#x27;</p>

<p>https://github.com/CelestiaProject/Celestia — GitHub API: full_name CelestiaProject/Celestia, not archived, pushed 2026-11-09, description &#x27;Real-time 3D visualization of space.&#x27;, homepage https://celestiaproject.space.</p>

<p>https://celestiaproject.space/ — HTTP 200 but behind an Anubis proof-of-work bot check, so the page body couldn&#x27;t be read with curl.</p>

<p>http://www.celestiamotherlode.net/ — HTTP 200: &#x27;The Celestia Motherlode is a repository for various addons like textures, models or celestial objects for Celestia … hosts over 10 GB of Celestia addons&#x27;.</p>

<p>Caveats: Couldn&#x27;t read the celestiaproject.space content because of the bot check. Ownership is supported by the official GitHub repo&#x27;s homepage field.; Motherlode is http-only.</p>

<p>Independent source check: Listed celestia.space directly serves a parked domain-for-sale page. Official project README identifies celestiaproject.space. Newsite is bot-protected, but ownership is directly supported by project source; no inference from DNS alone is needed. Companion Motherlode unchanged and not independently revalidated.</p>

<p>https://celestia.space/ — Directly read parked page with sale notice.</p>

<p>https://github.com/CelestiaProject/Celestia/blob/master/README.md — Official README links celestiaproject.space as projectwebsite; bloba5278764c33be6175505a84b4092426dc82bf98a.</p>

<p>https://celestiaproject.space/ — Anubis access-denied page; no claim to have read productpage.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Gaia Sky — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -70,7 +70,7 @@
 * [Celestia](https://celestia.space/) - Free real-time 3D visualization of space. (See also [Celestia Motherlode](http://www.celestiamotherlode.net/) for many add-ons.)
 * [Cesium.js](https://cesiumjs.org/) - An open-source JavaScript library for world-class 3D globes and maps
 * [Cosmic Timeline](https://cosmic-timeline.netlify.app/) - Interactive journey through the history of the universe, from the Planck epoch to today, with the physical values at each instant computed from the Planck 2018 cosmological model.
-* [Gaia Sky](https://zah.uni-heidelberg.de/institutes/ari/gaia/outreach/gaiasky/) - Real-time, 3D, astronomy visualization software developed in the framework of ESA's Gaia mission. Runs on Windows, Linux and macOS.
+* [Gaia Sky](https://gaiasky.space/) - Real-time, 3D, astronomy visualization software developed in the framework of ESA's Gaia mission. Runs on Windows, Linux and macOS.
 * [Harmony of the Spheres](https://github.com/TheHappyKoala/Harmony-of-the-Spheres) - Newtonian gravity and space simulator that runs in your browser
 * [KStars](https://edu.kde.org/kstars/) - KStars is free, open source, cross-platform astronomy software. It provides many features, including a graphical simulation of the night sky, observing planner, a sky calendar tool, an FOV editor, and more.
 * [LeoLabs Visualization](https://platform.leolabs.space/visualization) - Low Earth Orbit Catalog Visualization.
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed Heidelberg URL returns 404; Wayback shows it was valid in 2020. Gaia Sky now has its own official site, gaiasky.space (version 3.9.2, 27 Oct 2026). That site says Gaia Sky is a real-time 3D astronomy visualisation platform that runs on Windows, Linux and macOS and is developed in the framework of ESA&#x27;s Gaia mission. The official repo mirror points to the same homepage. The description is still accurate.</p>

<p>https://zah.uni-heidelberg.de/institutes/ari/gaia/outreach/gaiasky/ — HTTP 404. The ari.uni-heidelberg.de equivalent also returns 404.</p>

<p>https://gaiasky.space/ — &#x27;Gaia Sky is a real-time, 3D, astronomy visualisation platform for desktop and VR that runs on Windows, Linux, and macOS… developed in the framework of ESA&#x27;s Gaia mission&#x27;. Latest version 3.9.2, 27 Oct 2026.</p>

<p>https://github.com/langurmonkey/gaiasky — Description &#x27;Mirror fo the Gaia Sky repository at https://codeberg.org/gaiasky/gaiasky&#x27;, homepage https://gaiasky.space, pushed 2026-11-10.</p>

<p>Caveats: The main source repository is on Codeberg (codeberg.org/gaiasky/gaiasky, reachable).</p>

<p>Independent source check: New official product site directly supports Gaia Sky identity,3Dvisualization, platform support and ESAmission association. Old Heidelberg URL could not be fetched independently, so this audit does not confirm its HTTP404 status.</p>

<p>https://gaiasky.space/ — Official current projectpage with institutional links read.</p>

<p>https://zah.uni-heidelberg.de/institutes/ari/gaia/outreach/gaiasky/ — Webtool cachemiss; no independently confirmed404.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Orb Viewer — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -76,7 +76,7 @@
 * [LeoLabs Visualization](https://platform.leolabs.space/visualization) - Low Earth Orbit Catalog Visualization.
 * [Mars Now](https://mars.nasa.gov/explore/mars-now/) - This visualization shows the current location and communication activity of all operating landers, rovers and orbiters at Mars that transmit data to Earth via NASA’s Mars Relay Network.
 * [NASA Eyes](https://eyes.nasa.gov/) - Immersible apps to explore the Earth and solar system
-* [Orb Viewer](https://parsecsreach.com/orbviewer) - Visualization of all the asteroids in the MPC database.
+* [Orb Viewer](https://parsecsreach.org/orbviewer/) - Visualization of all the asteroids in the MPC database.
 * [Orbit Simulator](http://www.orbitsimulator.com/gravity/articles/what.html) - A powerful numerical integration tool. "By performing n-body simulations, you can study the orbits of planets, moons, asteroids, or any object in the universe."
 * [Orbiter 2016](http://orbit.medphys.ucl.ac.uk/) - Open source spaceflight simulator with many addons for historical missions. [Installation Instructions.](https://www.reddit.com/r/Orbiter/comments/mx2mjz/guide_for_beginners_to_orbiter/)
 * [Overhead](https://overheadexplorer.com/) - A browser-based real-time night sky map and interactive 3D rocket explorer (Saturn V, Artemis II, Falcon 9), part of a combined astronautics/aviation tracking site.
```

<details>
<summary>Evidence and limitations</summary>

<p>parsecsreach.com no longer resolves in DNS. The author&#x27;s GitHub Pages site (emilyselwood.github.io/orbviewer/) now redirects to parsecsreach.org/orbviewer/. That page is live and shows the same Orb Viewer: every known asteroid, using Minor Planet Center data, by Emily Selwood and collaborators. The description is still accurate.</p>

<p>https://parsecsreach.com/orbviewer — Connection failed. dig returns no A or NS records for parsecsreach.com.</p>

<p>http://web.archive.org/web/20201102115641/https://parsecsreach.com/orbviewer/ — Archived 2020 page: &#x27;Orb Viewer: This is a model of the entire solar system with every known asteroid marked… data is sourced from the Minor planets center&#x27;. It links github.com/wselwood/orbviewer.</p>

<p>https://github.com/emilyselwood/orbviewer — Former wselwood/orbviewer, now emilyselwood/orbviewer, not archived, pushed 2026-07-07. The README says it hosts OrbViewer and that the canonical code lives in emilyselwood/orbcalc.</p>

<p>https://parsecsreach.org/orbviewer/ — Reached via a 301 from https://emilyselwood.github.io/orbviewer/. HTTP 200 with the same Orb Viewer text (&#x27;every known asteroid marked… sourced from the Minor planets center… Emily Selwood and collaborators&#x27;).</p>

<p>Caveats: Did not check how recently the asteroid data was updated.</p>

<p>Independent source check: Proposed .org destination directly displays Orb Viewer and MPCdata attribution and links the author’s OrbCalc. Existing authorrepo still contains stale .comlink. GitHub Pagesredirect/CNAME could not be independently verified, so domainmigration attribution is qualified; do not cite deadDNS as established by this audit.</p>

<p>https://parsecsreach.org/orbviewer/ — Live viewer text and OrbCalc attribution read.</p>

<p>https://github.com/emilyselwood/orbviewer/blob/master/README.md — Repository identifies OrbViewer and canonical OrbCalc source, but retains stale.com link.</p>

<p>https://emilyselwood.github.io/orbviewer/ — Directwebtoolread unavailable; no redirectproof.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Orbiter 2016 — update</h3>

<p>0 proposed change(s); 1 held for unresolved questions.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The UCL host orbit.medphys.ucl.ac.uk is down: it returned 502 or timed out, and its Oct 2025 Wayback snapshot shows UCL&#x27;s &#x27;Web Application No Longer Available&#x27; notice. Orbiter 2016 was the last closed-source release. The author open-sourced Orbiter in 2021 at github.com/orbitersim/orbiter, under MIT, and that repo released &#x27;Orbiter 2024&#x27; on 2024-12-31. The listed name and URL point to a retired host, and &#x27;Open source&#x27; was never true of the 2016 release itself, so the entry should point to the official open-source project.</p>

<p>http://orbit.medphys.ucl.ac.uk/ — The live fetch returned 502 or timed out.</p>

<p>http://web.archive.org/web/20251010050418/http://orbit.medphys.ucl.ac.uk/ — Archived 2025-10-10: &#x27;Important Notice: Web Application No Longer Available… contact webhosting-support@ucl.ac.uk&#x27;.</p>

<p>https://github.com/orbitersim/orbiter — Active (pushed 2026-11-08). The README says &#x27;Orbiter is now published as an Open Source project under the MIT License&#x27;. The latest release is &#x27;Orbiter 2024&#x27; (2024-12-31). Src/Orbiter/TabAbout.cpp still links http://orbit.medphys.ucl.ac.uk/.</p>

<p>https://openorbiter.space/ — Timeline: &#x27;June 2016 Orbiter 2016 released… final release of the closed-source version&#x27;. July 2021 &#x27;Time to open-up&#x27;, quoting Martin Schweiger: &#x27;I have decided to publish the sources under an open source license&#x27;. &#x27;December 2024 First Stable Release… on GitHub&#x27;.</p>

<p>Blocking questions: The Reddit installation guide couldn&#x27;t be read, so it&#x27;s unknown whether it still applies to Orbiter 2024.</p>

<p>Caveats: Couldn&#x27;t read the Reddit installation guide (HTTP 403 for both www and old.reddit). It dates from 2021, so it may describe installing Orbiter 2016. It is kept unchanged in the proposed text, but the maintainer may want to drop or replace it with the GitHub release instructions.; UCL&#x27;s notice might be temporary, but the archived page says the application is no longer available.</p>

<p>Independent source check: Official project history identifies Orbiter2016 as last closed-source release and open-sourcing in2021. Current source README confirms MITopen-source project. The catalog’s2016label/open-source claim conflates versions. Updating toward current project is supported, but oldRedditinstallationguide applicability remains unresolved and should keep proposed patch held.</p>

<p>https://openorbiter.space/ — Official community history distinguishes2016closed-source release from2021open-sourcing.</p>

<p>https://github.com/orbitersim/orbiter/blob/main/README.md — Current official repository documents open-source MITproject; blob7bebbfebafb6c2478dd38aeaee8f871107389ba4.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>NewSpace Startup Legal Guide — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -101,7 +101,7 @@
 
 * [Awesome Assured Autonomy](https://github.com/sylvesterkaczmarek/awesome-assured-autonomy) - Curated research, tools, benchmarks, standards, and open-source systems for assuring autonomous systems.
 * [Awesome Space Autonomy](https://github.com/sylvesterkaczmarek/awesome-space-autonomy) - Curated research, flight demonstrations, software, tools, and guidance for autonomous spacecraft and space robots.
-* [NewSpace Startup Legal Guide](https://www.buzko.legal/practices-eng/space#newspace-startup-legal-guide) – A guide tailored for space industry startups. It covers licensing of space activities, public-private partnerships in space, legal intricacies of launching payloads, space risk insurance, etc.
+* [NewSpace Startup Legal Guide](https://www.buzko.legal/product/newspace-startup-legal-guide) – A guide tailored for space industry startups. It covers licensing of space activities, public-private partnerships in space, legal intricacies of launching payloads, space risk insurance, etc.
 * [NITARP](https://nitarp.ipac.caltech.edu/page/other_epo_programs) - NITARP, the NASA/IPAC Teacher Archive Research Program, gets teachers & students involved in authentic astronomical research.
 * [RDFvocab](https://github.com/chronos-pramantha/RDFvocab) - A collection of linked data ontologies (semantically linked representations) that describe astronomical and space engineering concepts. Can be used to link popular data sets like [DBPedia](https://wiki.dbpedia.org).
 * [Resources and references on the topic of space exploration](https://space.meta.stackexchange.com/questions/249/resources-and-references-on-the-topic-of-space-exploration) - StackExchange list of books, manuals, courses, and more.
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed anchor (#newspace-startup-legal-guide) no longer has a matching section on the Space Law page, whose Documents area shows &#x27;No items found&#x27;. The same firm now hosts the guide on a dedicated product page with the same description and four topics, dated 6 December 2023. The description remains accurate.</p>

<p>https://www.buzko.legal/practices-eng/space — Space Law practice page. It has no NewSpace guide section or download, and Documents shows &#x27;No items found.&#x27;</p>

<p>https://www.buzko.legal/product/newspace-startup-legal-guide — &#x27;NewSpace Startup Legal Guide — This comprehensive guide is tailored to meet the needs of space industry startups. Covering ... licensing of space activities, public-private partnerships in space, legal intricacies of launching payloads, and space risk insurance&#x27;. Dated December 6, 2023, with a download form.</p>

<p>https://www.buzko.legal/sitemap.xml — The sitemap includes /product/newspace-startup-legal-guide.</p>

<p>Caveats: Downloading requires agreeing to the privacy policy in a form. I did not download the PDF.; The guide dates from 2023. It is a dated resource, which is not a reason to remove it.</p>

</details>

<h3>NITARP — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -102,7 +102,7 @@
 * [Awesome Assured Autonomy](https://github.com/sylvesterkaczmarek/awesome-assured-autonomy) - Curated research, tools, benchmarks, standards, and open-source systems for assuring autonomous systems.
 * [Awesome Space Autonomy](https://github.com/sylvesterkaczmarek/awesome-space-autonomy) - Curated research, flight demonstrations, software, tools, and guidance for autonomous spacecraft and space robots.
 * [NewSpace Startup Legal Guide](https://www.buzko.legal/practices-eng/space#newspace-startup-legal-guide) – A guide tailored for space industry startups. It covers licensing of space activities, public-private partnerships in space, legal intricacies of launching payloads, space risk insurance, etc.
-* [NITARP](https://nitarp.ipac.caltech.edu/page/other_epo_programs) - NITARP, the NASA/IPAC Teacher Archive Research Program, gets teachers & students involved in authentic astronomical research.
+* [NITARP](https://nitarp.ipac.caltech.edu/) - NITARP, the NASA/IPAC Teacher Archive Research Program, gets teachers & students involved in authentic astronomical research.
 * [RDFvocab](https://github.com/chronos-pramantha/RDFvocab) - A collection of linked data ontologies (semantically linked representations) that describe astronomical and space engineering concepts. Can be used to link popular data sets like [DBPedia](https://wiki.dbpedia.org).
 * [Resources and references on the topic of space exploration](https://space.meta.stackexchange.com/questions/249/resources-and-references-on-the-topic-of-space-exploration) - StackExchange list of books, manuals, courses, and more.
 * [Space Jargon Cheatsheet](https://github.com/LunCoSim/lunco-space-jargon) – list of space-related terms and jargon
```

<details>
<summary>Evidence and limitations</summary>

<p>The description describes NITARP itself, and the official &#x27;What is NITARP&#x27; page supports it. The listed URL, however, points to NITARP&#x27;s &#x27;Other EPO Programs Using Real Data&#x27; list, a different resource. The program&#x27;s canonical page is the NITARP home page, which is active and shows current research teams.</p>

<p>https://nitarp.ipac.caltech.edu/page/other_epo_programs — Page title &#x27;Other EPO Programs Using Real Data&#x27;. It lists other programs, with links &#x27;updated as of October 2026&#x27;; it is not a page about NITARP.</p>

<p>https://nitarp.ipac.caltech.edu/page/about — &#x27;NITARP, the NASA/IPAC Teacher Archive Research Program, gets teachers involved in authentic astronomical research.&#x27; Applications open annually in May.</p>

<p>https://nitarp.ipac.caltech.edu/ — Home page is active (© 2026) and shows a current research team (AGNatha, WISE/Gaia).</p>

<p>Caveats: The maintainer may have linked the EPO-programs list on purpose. If so, change the description instead of the URL.</p>

</details>

<h3>RDFvocab — update</h3>

<p>0 proposed change(s); 1 held for unresolved questions.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The repo chronos-pramantha/RDFvocab is live and contains RDF ontologies for astronomy, engineering, spacecraft, subsystems, the Solar System and exploration, plus a dbpedia_predicates.ntriples file. The description holds. The inline DBpedia link wiki.dbpedia.org redirects to https://www.dbpedia.org/, so only that embedded URL needs updating.</p>

<p>https://raw.githubusercontent.com/chronos-pramantha/RDFvocab/main/README.md — It lists ontologies for Astronomy, Engineering, Spacecraft, Subsystems, SolarSystem and Exploration.</p>

<p>https://github.com/chronos-pramantha/RDFvocab/tree/main/raw — Contains dbpedia_predicates.ntriples and SpaceSensor_ttl_v2.owl.</p>

<p>https://www.dbpedia.org/ — wiki.dbpedia.org returns a redirect to https://www.dbpedia.org/ (DBpedia Association home).</p>

<p>Caveats: The repo shows little recent activity. That is not a reason to remove it.</p>

</details>

<h3>ActInSpace — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -109,7 +109,7 @@
 
 ### Space Hackathons and Challenges
 
-* [ActInSpace](https://entreprises.cnes.fr/fr/actinspace) - A hackathon about space app, every even year, launched by the french CNES.
+* [ActInSpace](https://actinspace.org/) - An international space-app innovation contest and hackathon held every two years, organized by CNES and ESA.
 * [Space Apps Challenge](https://www.spaceappschallenge.org/) - NASA-led initiative organized in collaboration with Booz Allen Hamilton, Mindgrub and SecondMuse.
 
 ### Working Groups
```

<details>
<summary>Evidence and limitations</summary>

<p>The CNES URL now redirects to the general page https://cnes.fr/entreprises, which does not mention ActInSpace. The event&#x27;s own site, actinspace.org, is live with a 2026 edition: a worldwide hackathon on 30–31 January 2026 and finals in Bordeaux on 1–2 April 2026. It says the event was &#x27;Launched in 2014 by ... CNES ... and ... ESA&#x27; and runs &#x27;every two years&#x27;. &#x27;Launched by the french CNES&#x27; leaves out ESA.</p>

<p>https://entreprises.cnes.fr/fr/actinspace — HTTP 301 to https://cnes.fr/entreprises. That page has no ActInSpace mention.</p>

<p>https://actinspace.org/ — &#x27;ActInSpace — An international innovation contest lead by CNES and ESA ... Launched in 2014 by CNES and ESA, this event takes place every two years&#x27;. Hackathon 30–31 Jan 2026, finals in Bordeaux 1–2 April 2026.</p>

<p>Caveats: actinspace.org states its CNES/ESA backing itself. I found no CNES page that links to it.</p>

</details>

<h3>SpaceEngine — update</h3>

<p>0 proposed change(s); 1 held for unresolved questions.</p>

<details>
<summary>Evidence and limitations</summary>

<p>SpaceEngine itself is current and still describes itself as a realistic virtual universe. The &#x27;free old versions&#x27; link redirects to https://spaceengine.org/load/old_versions/4, which returns 404. The official download page (WordPress content, modified 2025-08-18) only embeds the Steam store widget. Its only other download page is for official addons, and there is no free legacy download, so the &#x27;free&#x27; claim and its link are no longer supported.</p>

<p>https://spaceengine.org — Home page: &#x27;SpaceEngine is a realistic virtual Universe you can explore on your computer.&#x27; © 2011-2026.</p>

<p>http://old.spaceengine.org/load/old_versions/4 — 301 to https://spaceengine.org/load/old_versions/4, which returns HTTP 404.</p>

<p>https://spaceengine.org/wp-json/wp/v2/pages/3366 — The official /download/spaceengine/ page content is only an iframe of the Steam store widget for app 314650. The /download/ parent page links only to &#x27;SpaceEngine&#x27; and &#x27;Official addons/DLC&#x27;.</p>

<p>Caveats: Unofficial copies of the free 0.980 build may still exist on third-party sites. Those are not official sources, so I did not cite them.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Open Source Satellite — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -114,7 +114,7 @@
 
 ### Working Groups
 
-* [Open Source Satellite](https://www.opensourcesatellite.org/) - Ecosystem for sharing ideas and creating a "highly capable, flexible and affordable open source microsatellite platform." Founded by "a team of international space experts" dedicated to open source.
+* [Open Source Satellite](https://www.opensourcesatellite.org/) - Ecosystem for sharing ideas and creating an "accessible, highly capable, cost-effective, modular, microsatellite platform." Founded by "a team of international space experts" dedicated to open source.
 
 ## Data
 
```

<details>
<summary>Evidence and limitations</summary>

<p>The site is live and still relevant: it is an open source microsatellite platform programme. The second quote, &quot;a team of international space experts&quot;, still appears verbatim. The first quote, &quot;highly capable, flexible and affordable open source microsatellite platform&quot;, no longer appears on the site. The current goal text reads &quot;an accessible, highly capable, cost-effective, modular, microsatellite platform&quot;. Update the quotation so it matches the source.</p>

<p>https://www.opensourcesatellite.org/ — The homepage says &quot;Our Goal is to develop an accessible, highly capable, cost-effective, modular, microsatellite platform...&quot; and &quot;A team of international space experts with decades of first-hand experience...&quot;. It describes the community and a fully open source microsatellite platform. The phrase &quot;flexible and affordable open source microsatellite platform&quot; was not found.</p>

<p>https://www.opensourcesatellite.org/news/ — The news page lists monthly OSSAT sessions; the most recent seen is dated 19 Dec 2024.</p>

<p>Caveats: The newest news post seen is from Dec 2024. Low recent activity is not a reason for removal.</p>

</details>

<h3>Orbit Codex — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -121,7 +121,7 @@
 ### Analytics & Visualization
 
 * [obdh.space](https://obdh.space/) - An interactive, all-in-one space data platform with charts and live statistics about satellites, launches and more, updated every day.
-* [Orbit Codex](https://orbitcodex.com) - An open browser-based directory of 14,000+ spaceflight entities (satellites, launches, agencies, astronauts, landing sites, missions) paired with a CesiumJS 3D viewer. Aggregates The Space Devs, JPL Horizons, CelesTrak, Space-Track, and ESA DISCOS into a single interactive interface.
+* [Orbit Codex](https://orbitcodex.com) - A free browser-based directory of spaceflight entities (satellites, launches, agencies, astronauts, landing sites, missions) paired with a CesiumJS 3D viewer. Aggregates The Space Devs, JPL Horizons, CelesTrak, Space-Track, and ESA DISCOS into a single interactive interface.
 * [Satcat.com](https://satcat.com) - Satcat is a web application by Kayhan Space that provides search, visualizations, and orbital design tools
 
 ### Astronomy Data
```

<details>
<summary>Evidence and limitations</summary>

<p>The site is live and relevant. The CesiumJS viewer is confirmed, and the data sources page lists every aggregated source named in the entry. The &quot;14,000+ spaceflight entities&quot; count no longer matches the site: the About page says &quot;13,000+ pages&quot; and the tracker says &quot;35,000+ objects in orbit&quot;. Replace the volatile count with durable wording.</p>

<p>https://orbitcodex.com/about — The About page says &quot;13,000+ pages, free to use, without ads or an account&quot; and mentions a 3D tracker of &quot;35,000+ objects in orbit&quot;. The catalog covers rockets, spacecraft, organizations, astronauts, launch sites and space stations.</p>

<p>https://orbitcodex.com/about/data-sources — Lists Launch Library 2 (The Space Devs), CelesTrak, Space-Track.org, ESA DISCOS, NASA JPL Horizons and Cesium (CesiumJS and Cesium ion) for the 3D globe, along with NOAA SWPC and others. Last updated 26 October 2026.</p>

<p>https://orbitcodex.com — The homepage shows the live 3D tracker, launch schedule and directories for hardware, infrastructure and entities.</p>

<p>Caveats: &quot;Open&quot; in the entry most plausibly means free to use. No open source code was checked.; The site says it uses AI for research and drafting. This is noted for information only and is not a fit criterion.</p>

</details>

<h3>Data.gov - NASA — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -136,7 +136,7 @@
 ### Data Directories
 
 * [api.nasa.gov](https://api.nasa.gov/) - NASA's API portal
-* [Data.gov - NASA](https://catalog.data.gov/dataset?organization=nasa-gov) - The US Federal government's open data portal page for NASA data sets. If you search by Bureaus, Organizations, or Publishers, you'll find additional space-related data sets from NASA/GSFC, NOAA, the Space Science Technology Directorate, selected universities, and more.
+* [Data.gov - NASA](https://catalog.data.gov/organization/nasa) - The US Federal government's open data portal page for NASA data sets. Filter by publisher to find space-related data sets from NASA centers and archives such as GSFC, SPDF, HEASARC, and more.
 * [data.nasa.gov](https://data.nasa.gov/) - Continually growing catalog of publicly available NASA datasets, APIs, visualizations, and more
 * [images.nasa.gov](https://images.nasa.gov/) - Search NASA's informational image and video archive
 * [MAST](https://archive.stsci.edu/index.html) - A NASA-funded site that provides astronomical data archives focused on scientific data sets in the optical, ultraviolet, and near-IR.
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL, catalog.data.gov/dataset?organization=nasa-gov, now 301-redirects to the catalog root, which drops the NASA filter, and /organization/nasa-gov returns Page not found. The working NASA organization page is https://catalog.data.gov/organization/nasa. The rebuilt catalog offers Keyword and Publisher filters; no &quot;Bureau&quot; filter was observed. The example publishers have also changed.</p>

<p>https://catalog.data.gov/dataset?organization=nasa-gov — Returns HTTP 301 with location &quot;/&quot;. The landing page shows all 535,145 datasets with no NASA filter applied.</p>

<p>https://catalog.data.gov/organization/nasa — The page &quot;National Aeronautics and Space Administration - Organization&quot; shows 36,592 datasets. Filters: Geographic Area, Keywords, Publisher (e.g., NASA, Small Bodies, NASA/GSFC/SED/ESD/TISL/GESDISC, ORNL_DAAC, SPDF, HEASARC) and Data Access.</p>

<p>Caveats: Data.gov&#x27;s filters may change again. The proposed wording avoids dataset counts.; NOAA data remains on Data.gov under its own organization, but it is not part of the NASA organization page.</p>

</details>

<h3>Orbit Sentinel — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -140,7 +140,7 @@
 * [data.nasa.gov](https://data.nasa.gov/) - Continually growing catalog of publicly available NASA datasets, APIs, visualizations, and more
 * [images.nasa.gov](https://images.nasa.gov/) - Search NASA's informational image and video archive
 * [MAST](https://archive.stsci.edu/index.html) - A NASA-funded site that provides astronomical data archives focused on scientific data sets in the optical, ultraviolet, and near-IR.
-* [Orbit Sentinel](https://www.viventine.com/orbit-sentinel/) - Searchable database and API of 950K+ space regulatory filings from the FCC, ITU, UNOOSA, and FAA-AST, with an open-source MCP server for AI-assistant access.
+* [Orbit Sentinel](https://www.viventine.com/orbit-sentinel/) - Searchable database and API of space regulatory filings from the FCC, ITU, UNOOSA, and FAA-AST, with an open-source MCP server for AI-assistant access.
 * [Small Satellite Information Search](https://s3vi.ndc.nasa.gov/) - NASA's federated search portal for small spacecraft parts, technologies and conference proceedings.
 
 ### Data Wrangling Tools
```

<details>
<summary>Evidence and limitations</summary>

<p>Orbit Sentinel is live and relevant: it covers regulatory filings from the FCC, ITU, UNOOSA and FAA, with an API and an MIT-licensed MCP server. The &quot;950K+&quot; figure conflicts with the product page, which says &quot;418K+ Filings Extracted&quot;. The figure does appear in the MCP README. Drop the volatile count.</p>

<p>https://www.viventine.com/orbit-sentinel/ — Shows &quot;418K+ Filings Extracted&quot;, &quot;18K+ Organizations Tracked&quot; and &quot;68K+ Satellites Cataloged&quot;. Mentions cross-agency FCC, ITU, UNOOSA and FAA filings, API access, and &quot;connect directly via our MCP server&quot;.</p>

<p>https://github.com/Viventine-Space/orbit-sentinel-mcp — MIT-licensed repository: &quot;MCP server for Orbit Sentinel — space regulatory filings from FCC, ITU, UNOOSA, FAA-AST&quot;. The README claims &quot;950K+ space regulatory filings&quot;. Last pushed 2026-11-07.</p>

<p>Caveats: The two counts may measure different things (indexed versus extracted filings). Removing the number avoids the conflict.; The product is commercial and has a free plan.</p>

</details>

<h3>pyspaceweather — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -146,7 +146,7 @@
 ### Data Wrangling Tools
 
 * [orbital-cotwo-web](https://github.com/chronos-pramantha/orbital-cotwo-web) - A data processing pipeline and web server that can dump [HDF5](https://earthdata.nasa.gov/esdis/eso/standards-and-references/hdf5) files from NASA's [Orbital Carbon Observatory 2](https://www.nasa.gov/mission_pages/oco2/index.html) mission into an SQL database.
-* [pyspaceweather](https://github.com/ben-n93/pyspaceweather) - A Python wrapper for getting space weather data from Australia's Bureau of Meteorology.
+* [pyspaceweather](https://github.com/ben-nour/pyspaceweather) - A Python wrapper for getting space weather data from Australia's Bureau of Meteorology.
 * [SETU](https://github.com/pragyaangaur/SETU) - Forecasts geomagnetically induced currents in the North East Indian power grid from space weather data. Its live nowcast issued 114 forecasts with no false alarms.
 
 ### Earth
```

<details>
<summary>Evidence and limitations</summary>

<p>github.com/ben-n93/pyspaceweather redirects to github.com/ben-nour/pyspaceweather, so the owner has been renamed. The README and pyproject confirm the description: a Python wrapper for the Australian Bureau of Meteorology&#x27;s Space Weather API. Update the URL to the canonical owner.</p>

<p>https://github.com/ben-n93/pyspaceweather — An HTTP fetch resolves to https://github.com/ben-nour/pyspaceweather. The packet snapshot also records repository ben-nour/pyspaceweather, not archived, default branch main.</p>

<p>https://raw.githubusercontent.com/ben-nour/pyspaceweather/main/README.md — Says &quot;pyspaceweather is a Python wrapper for the Australian Bureau of Metererology&#x27;s Space Weather API.&quot; Badges point to ben-nour/pyspaceweather.</p>

<p>https://raw.githubusercontent.com/ben-nour/pyspaceweather/main/pyproject.toml — Package pyspaceweather 0.1.0, described as &quot;A Python wrapper for the Australian Bureau of Meteorology&#x27;s Space Weather API.&quot; project.urls still point to the old ben-n93 path.</p>

<p>Caveats: The GitHub API was rate-limited, so canonical identity was confirmed through the redirect and the packet snapshot. The code was not run.</p>

</details>

<h3>orbital-cotwo-web — update</h3>

<p>0 proposed change(s); 1 held for unresolved questions.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The repository is live and its README matches the description: an HDF5-to-SQL/PostGIS pipeline with a Falcon web server for OCO-2 data. Both inline links are dead. The earthdata HDF5 link 404s, and the working page is https://www.earthdata.nasa.gov/about/esdis/esco/standards-practices/hdf5. The nasa.gov OCO-2 mission_pages link 404s, and NASA Science hosts the mission at https://science.nasa.gov/mission/oco-2/. Also, the mission&#x27;s name is Orbiting Carbon Observatory 2, not &quot;Orbital Carbon Observatory 2&quot;.</p>

<p>https://github.com/chronos-pramantha/orbital-cotwo-web — The repository is live with no archive banner. The README describes a &quot;data pipeline from highly distributed file system (HDF5) to SQL/GIS database&quot; with a Falcon server serving OCO data as GeoJSON, and labels itself beta.</p>

<p>https://earthdata.nasa.gov/esdis/eso/standards-and-references/hdf5 — Redirects to www.earthdata.nasa.gov, which returns 404.</p>

<p>https://www.earthdata.nasa.gov/about/esdis/esco/standards-practices/hdf5 — HTTP 200, titled &quot;HDF5 Data Model, File Format, and Library | NASA Earthdata&quot;.</p>

<p>https://www.nasa.gov/mission_pages/oco2/index.html — HTTP 404.</p>

<p>https://science.nasa.gov/mission/oco-2/ — HTTP 200, titled &quot;OCO-2 - NASA Science&quot;.</p>

<p>Caveats: The repository appears old (Python 3.4+ era). Low activity is not a reason for removal. The code was not run.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>EOS Land Viewer — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -155,7 +155,7 @@
 * [Copernicus Open Access Hub](https://scihub.copernicus.eu/) - The Copernicus Open Access Hub provides complete, free and open access to Sentinel-1, Sentinel-2, Sentinel-3 and Sentinel-5P user products.
 * [Earth on AWS](https://aws.amazon.com/earth)
 * [earthdata.nasa.gov](https://earthdata.nasa.gov/earth-observation-data) - Portal to NASA's Earth observation data
-* [EOS Land Viewer](https://eos.com/products/landviewer/) - A free GIS database of the most widely used satellite images.
+* [EOS Land Viewer](https://eos.com/products/landviewer/) - Browser-based platform to search, view and analyze satellite imagery, with a limited free plan.
 * [ESA's Earth Online](https://earth.esa.int/eogateway/)
 * [ESA's GEOSS Portal](http://www.geoportal.org/) - Query for Earth imagery across a suite of space systems
 * [Global Forest Watch Open Data Portal](http://data.globalforestwatch.org/) - Identify areas of tree cover loss and gain
```

<details>
<summary>Evidence and limitations</summary>

<p>LandViewer is still EOSDA&#x27;s browser platform for searching and analyzing satellite imagery, but &#x27;A free GIS database&#x27; is now misleading. The official FAQ describes a free Starter plan limited to 5 images per month, paid subscription plans, and high-resolution commercial imagery ordered separately.</p>

<p>https://eos.com/products/landviewer/ — &#x27;Search, visualize, and analyze satellite imagery directly in your browser.&#x27; Lists Sentinel-1/2, Landsat 8/9 and MODIS, plus commercial high-resolution sources.</p>

<p>https://eos.com/products/landviewer/ — FAQ: &#x27;LandViewer offers a free Starter plan with access to up to 5 images per month.&#x27; Also: &#x27;high-resolution commercial imagery is not included in standard subscriptions. These images must be ordered separately.&#x27;</p>

<p>Caveats: Plan limits may change. The suggested wording avoids specific numbers.</p>

</details>

<h3>High Definition Earth-Viewing System (HDEV) — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -161,7 +161,7 @@
 * [Global Forest Watch Open Data Portal](http://data.globalforestwatch.org/) - Identify areas of tree cover loss and gain
 * [Google Earth](https://earth.google.com/)
 * [Google's Earth Engine](https://developers.google.com/earth-engine/datasets) - Earth Engine's public data archive includes more than forty years of historical imagery and scientific datasets, updated and expanded daily.
-* [High Definition Earth-Viewing System (HDEV)](https://eol.jsc.nasa.gov/ESRS/HDEV/) - Realtime stream of Earth from the ISS
+* [ISS High Definition Live Streaming Video of the Earth](https://eol.jsc.nasa.gov/ESRS/HDEV/) - Live stream of Earth from an external HD camera on the ISS; successor to the retired HDEV experiment.
 * [Landsat data sources](https://landsat.gsfc.nasa.gov/data/where-to-get-data/)
 * [Maxar Open Data Program](https://www.maxar.com/open-data/) - Maxar releases limited open data during major crisis events.
 * [MetaEarth](https://github.com/bair-climate-initiative/metaearth) - Download any remote sensing data from any provider using a single config.
```

<details>
<summary>Evidence and limitations</summary>

<p>The HDEV experiment reached end of life on 22 August 2019. The same NASA page is now titled &#x27;ISS High Definition Live Streaming Video of the Earth&#x27; and says it is &#x27;Formerly the site for the High Definition Earth-Viewing System (HDEV)&#x27;. Live video now comes from a different external HD camera on the ISS. The URL and the description of a live stream still hold, but the entry&#x27;s name refers to retired hardware.</p>

<p>https://eol.jsc.nasa.gov/ESRS/HDEV/ — Heading: &#x27;ISS High Definition Live Streaming Video of the Earth (HDEV)&#x27;. &#x27;Formerly the site for the High Definition Earth-Viewing System (HDEV): Operational: April 30, 2014 – End of Life: August 22, 2019 ... Currently, live video of Earth is streaming from an external HD camera mounted on the ISS.&#x27; A YouTube embed (youtube.com/embed/ROboUHfPUrU) is present.</p>

<p>Caveats: I did not watch the embedded YouTube stream to confirm it is broadcasting right now. The official page says it is.</p>

</details>

<h3>Landsat data sources — update</h3>

<p>0 proposed change(s); 1 held for unresolved questions.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The listed &#x27;where-to-get-data&#x27; URL now redirects to the general NASA Landsat mission page, not a data-access page. landsat.gsfc.nasa.gov/data/ redirects to science.nasa.gov/mission/landsat/data-overview/. That page has a &#x27;How to Access Data&#x27; section listing data sources such as Worldview, USGS cloud access via AWS, Esri Landsat Explorer and Google Earth Engine, which matches the entry&#x27;s purpose.</p>

<p>https://science.nasa.gov/mission/landsat/ — https://landsat.gsfc.nasa.gov/data/where-to-get-data/ redirects here. This is the general Landsat mission page.</p>

<p>https://science.nasa.gov/mission/landsat/data-overview/ — landsat.gsfc.nasa.gov/data/ redirects here. &#x27;How to Access Data: Landsat data and science products are publicly accessible and free of charge. Explore and download these datasets using the following map viewers, data portals...&#x27; Lists NASA Worldview, USGS Landsat Commercial Cloud Access (AWS), Esri Landsat Explorer and Google Earth Engine.</p>

<p>Caveats: The entry is a bare link with no description, so only the URL changes.</p>

</details>

<h3>MetaEarth — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -164,8 +164,8 @@
 * [High Definition Earth-Viewing System (HDEV)](https://eol.jsc.nasa.gov/ESRS/HDEV/) - Realtime stream of Earth from the ISS
 * [Landsat data sources](https://landsat.gsfc.nasa.gov/data/where-to-get-data/)
 * [Maxar Open Data Program](https://www.maxar.com/open-data/) - Maxar releases limited open data during major crisis events.
-* [MetaEarth](https://github.com/bair-climate-initiative/metaearth) - Download any remote sensing data from any provider using a single config.
 * [Moonshine](https://moonshineai.readthedocs.io) - Machine learning models pretrained on remote sensing data.
+* [MultiEarth](https://github.com/bair-climate-initiative/multiearth) - Download any remote sensing data from any provider using a single config.
 * [NASA Land-Cover and Land-Use Change (LCLUC) Program](http://lcluc.umd.edu/content/data-initiatives)
 * [National Environmental Satellite Data and Information Service](https://www.nesdis.noaa.gov/) - Explore NOAA satellite maps and imagery in 2D and 3D.
 * [NOAA Data Access Viewer](https://coast.noaa.gov/dataviewer/#/)
```

<details>
<summary>Evidence and limitations</summary>

<p>The repository was renamed. bair-climate-initiative/metaearth redirects to bair-climate-initiative/multiearth, and the package metadata names the project MultiEarth. The description is still accurate: setup.cfg says &#x27;Download remote sensing data from any provider through a single config.&#x27;</p>

<p>https://github.com/bair-climate-initiative/multiearth — The old URL redirects here. Page title: &#x27;bair-climate-initiative/multiearth: Download and access remote sensing data from any platform&#x27;.</p>

<p>https://raw.githubusercontent.com/bair-climate-initiative/multiearth/main/setup.cfg — name = multiearth. description = &#x27;MultiEarth: Download remote sensing data from any provider through a single config.&#x27; Development status: 3 - Alpha.</p>

<p>https://raw.githubusercontent.com/bair-climate-initiative/multiearth/main/README.md — Heading: &#x27;MultiEarth: Download any remote sensing data from any provider.&#x27; Warns that it is an early alpha version.</p>

<p>Caveats: The project is an early alpha. Its README says the &#x27;any provider&#x27; diagram is aspirational and more providers are still being added.</p>

</details>

<h3>Copernicus Open Access Hub — replace</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -152,7 +152,7 @@
 ### Earth
 
 * [Bhuvan](https://bhuvan.nrsc.gov.in/bhuvan_links.php) - ISRO's Geoportal
-* [Copernicus Open Access Hub](https://scihub.copernicus.eu/) - The Copernicus Open Access Hub provides complete, free and open access to Sentinel-1, Sentinel-2, Sentinel-3 and Sentinel-5P user products.
+* [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/) - Free and open access to Copernicus Sentinel mission data, with browser, APIs and processing tools; successor to the Copernicus Open Access Hub.
 * [Earth on AWS](https://aws.amazon.com/earth)
 * [earthdata.nasa.gov](https://earthdata.nasa.gov/earth-observation-data) - Portal to NASA's Earth observation data
 * [EOS Land Viewer](https://eos.com/products/landviewer/) - A free GIS database of the most widely used satellite images.
```

<details>
<summary>Evidence and limitations</summary>

<p>The Copernicus Open Access Hub&#x27;s own archived home page states that it ceased operations at the end of October 2023. Users were told to register on the Copernicus Data Space Ecosystem, which is the officially documented successor. scihub.copernicus.eu did not connect, while dataspace.copernicus.eu is live and provides free access to Sentinel data.</p>

<p>http://web.archive.org/web/20250206181930/https://scihub.copernicus.eu/ — &#x27;The Copernicus Open Access Hub will be exceptionally extended for another month and will cease operations at the end of October 2023. To continue accessing Copernicus Sentinel data users will need to self-register on the new Copernicus Data Space Ecosystem.&#x27;</p>

<p>https://dataspace.copernicus.eu/ — &#x27;an open ecosystem that provides free instant access to a wide range of data and services from the Copernicus Sentinel missions ... ensures the continuity of the open and free access to Copernicus data.&#x27;</p>

<p>https://scihub.copernicus.eu/ — The connection failed (proxy CONNECT 502), so no current response was obtained.</p>

<p>Caveats: Today&#x27;s scihub response could not be retrieved. The replacement rests on the official shutdown notice, not on the failed connection.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Maxar Open Data Program — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -163,9 +163,9 @@
 * [Google's Earth Engine](https://developers.google.com/earth-engine/datasets) - Earth Engine's public data archive includes more than forty years of historical imagery and scientific datasets, updated and expanded daily.
 * [High Definition Earth-Viewing System (HDEV)](https://eol.jsc.nasa.gov/ESRS/HDEV/) - Realtime stream of Earth from the ISS
 * [Landsat data sources](https://landsat.gsfc.nasa.gov/data/where-to-get-data/)
-* [Maxar Open Data Program](https://www.maxar.com/open-data/) - Maxar releases limited open data during major crisis events.
 * [MetaEarth](https://github.com/bair-climate-initiative/metaearth) - Download any remote sensing data from any provider using a single config.
 * [Moonshine](https://moonshineai.readthedocs.io) - Machine learning models pretrained on remote sensing data.
+* [Vantor Open Data Program](https://vantor.com/company/open-data-program/) - Vantor (formerly Maxar Intelligence) releases limited open satellite imagery during major crisis events.
 * [NASA Land-Cover and Land-Use Change (LCLUC) Program](http://lcluc.umd.edu/content/data-initiatives)
 * [National Environmental Satellite Data and Information Service](https://www.nesdis.noaa.gov/) - Explore NOAA satellite maps and imagery in 2D and 3D.
 * [NOAA Data Access Viewer](https://coast.noaa.gov/dataviewer/#/)
```

<details>
<summary>Evidence and limitations</summary>

<p>maxar.com and the listed /open-data/ path now redirect to vantor.com. Vantor&#x27;s site states its business &#x27;was known as Maxar Intelligence&#x27;. The program continues as the Vantor Open Data Program, which releases imagery for free (CC BY-NC 4.0) when it is activated for major sudden-onset disasters, so the description is still accurate.</p>

<p>https://vantor.com/company/open-data-program/ — https://www.maxar.com/open-data/ redirects here. Title: &#x27;Vantor Open Data Program – Disaster Response Satellite Imagery&#x27;. Activation criteria: &#x27;The event is a sudden onset disaster. It is categorized as a major event...&#x27;. Imagery is released under CC BY-NC 4.0.</p>

<p>https://vantor.com/ — https://www.maxar.com/ redirects here. The page text says a report &#x27;was published in May 2023, when our business was known as Maxar Intelligence.&#x27;</p>

<p>Caveats: The rename changes where the entry sorts alphabetically.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>NASA Land-Cover and Land-Use Change (LCLUC) Program — update</h3>

<p>0 proposed change(s); 1 held for unresolved questions.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The listed data-initiatives page returns 404 (after redirecting to https). The NASA LCLUC program site is live and its &#x27;Data&#x27; menu now links to &#x27;Data for LCLUC Research&#x27;, which covers NASA datasets for land-cover and land-use research. The program is still relevant; only the deep link is broken.</p>

<p>https://lcluc.umd.edu/content/data-initiatives — HTTP 404.</p>

<p>https://lcluc.umd.edu/ — The NASA LCLUC Program website is live. Its Data menu has &#x27;Data for LCLUC Research&#x27;, &#x27;Satellite Sensing Systems&#x27; and &#x27;Other Related Data&#x27;.</p>

<p>https://lcluc.umd.edu/content/data-lcluc-research — Titled &#x27;Data for LCLUC Research&#x27;. &#x27;NASA Data Sets For LCLUC Research&#x27; describes ESDIS, MODIS/VIIRS land products, LAADS DAAC and other sources.</p>

<p>http://web.archive.org/web/20191227103639/http://lcluc.umd.edu:80/content/data-initiatives — The 2019 archived &#x27;Data Initiatives&#x27; page described related data efforts such as GEOSS and the Global Geo-Referenced Field Photo Library.</p>

<p>Caveats: The new page is the program&#x27;s current data section, not a documented one-to-one replacement for the old &#x27;Data Initiatives&#x27; page. Its content focuses on NASA datasets rather than the external initiatives the old page listed.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Planet API — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -170,7 +170,7 @@
 * [National Environmental Satellite Data and Information Service](https://www.nesdis.noaa.gov/) - Explore NOAA satellite maps and imagery in 2D and 3D.
 * [NOAA Data Access Viewer](https://coast.noaa.gov/dataviewer/#/)
 * [Office for Coastal Management's Digital Coast](https://coast.noaa.gov/digitalcoast/data/)
-* [Planet API](https://developers.planet.com/docs/api/) - Programmatic support for searching, clipping, ordering, and viewing satellite imagery on a map. Currently offers a free plan with access to low-resolution imagery worldwide.
+* [Planet API](https://docs.planet.com/develop/apis/) - APIs for searching, ordering, processing, and visualizing Planet and public satellite imagery, with cloud delivery and tile/OGC streaming. Offers a 30-day free trial.
 * [Remotepixel](https://remotepixel.ca/) - A collection of tools, including the RemotePixel Viewer, Satellite Search tool, and Disasterwatch, for exploring and downloading satellite imagery, maintained by one hardworking volunteer.
 * [Sentinelhub](https://www.sentinel-hub.com/explore/) - ESA's EO Browser and Sentinel Playground offer a complete archive of Sentinel-1, Sentinel-2, Sentinel-3, Sentinel-5P, ESA's archive of Landsat 5, 7 and 8, global coverage of Landsat 8, Envisat Meris, MODIS, Proba-V and GIBS products in one place.
 * [USGS EarthExplorer](https://earthexplorer.usgs.gov/) - A tool that provides users the ability to query, search, and retrieve satellite images, aerial photographs, and cartographic products from several sources
```

<details>
<summary>Evidence and limitations</summary>

<p>Planet&#x27;s APIs are still current and relevant. However, the listed URL now redirects to the generic docs.planet.com home page, and the claim of a &#x27;free plan with access to low-resolution imagery worldwide&#x27; is not supported by current official docs. Planet now offers a 30-day trial that includes open Sentinel/Landsat collections and sample PlanetScope data. Recommend pointing to the APIs overview page and dropping the outdated free-plan claim.</p>

<p>https://developers.planet.com/docs/api/ — HTTP redirect resolves to https://docs.planet.com/ (the generic Planet Documentation home), not an API page.</p>

<p>https://docs.planet.com/develop/apis/ — APIs overview lists the Data API (search), Orders API (download/delivery), Subscriptions, Basemaps, Tiles/OGC visualization, Processing, Statistical, and Tasking APIs.</p>

<p>https://docs.planet.com/guides/create-a-trial-account/ — &#x27;Start a Trial Account&#x27; guide (updated Sep 9, 2026): the trial lasts 30 days, after which services can no longer be used. Sandbox data is available for exploration. No permanent free plan is described.</p>

<p>https://www.sentinel-hub.com/explore/eobrowser/ — Offers &#x27;Planet Insights Platform free of charge for 30-days&#x27; and recommends Copernicus Data Space Ecosystem for permanently free Sentinel exploration.</p>

<p>Caveats: The planet.com pricing page is rendered client-side, so its tier text could not be read. The finding that there is no permanent free plan relies on the docs trial guide.; Did not sign up or call the APIs.</p>

</details>

<h3>Remotepixel — remove</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -171,7 +171,6 @@
 * [NOAA Data Access Viewer](https://coast.noaa.gov/dataviewer/#/)
 * [Office for Coastal Management's Digital Coast](https://coast.noaa.gov/digitalcoast/data/)
 * [Planet API](https://developers.planet.com/docs/api/) - Programmatic support for searching, clipping, ordering, and viewing satellite imagery on a map. Currently offers a free plan with access to low-resolution imagery worldwide.
-* [Remotepixel](https://remotepixel.ca/) - A collection of tools, including the RemotePixel Viewer, Satellite Search tool, and Disasterwatch, for exploring and downloading satellite imagery, maintained by one hardworking volunteer.
 * [Sentinelhub](https://www.sentinel-hub.com/explore/) - ESA's EO Browser and Sentinel Playground offer a complete archive of Sentinel-1, Sentinel-2, Sentinel-3, Sentinel-5P, ESA's archive of Landsat 5, 7 and 8, global coverage of Landsat 8, Envisat Meris, MODIS, Proba-V and GIBS products in one place.
 * [USGS EarthExplorer](https://earthexplorer.usgs.gov/) - A tool that provides users the ability to query, search, and retrieve satellite images, aerial photographs, and cartographic products from several sources
 * [Visible Earth](https://visibleearth.nasa.gov/) - A catalog of NASA images and animations of our home planet
```

<details>
<summary>Evidence and limitations</summary>

<p>The official site now shows only a closure notice. The author says RemotePixel.ca is closing because it is aging, they cannot maintain its broken parts, and the listed tools (Viewer, Satellite Search, Disasterwatch) are no longer offered. This is affirmative first-party evidence that the listed resource has lost its purpose.</p>

<p>https://remotepixel.ca/ — Page titled &#x27;Remote Pixel | Thanks The End&#x27; reads: &#x27;After years of living it&#x27;s time for RemotePixel.ca to close... Today RemotePixel is aging... and not well, I personaly don&#x27;t have time to maintain or update its broken parts. THANKS / MERCI&#x27;. No tools are offered.</p>

<p>Caveats: Did not search for the author&#x27;s open-source repositories that may have succeeded parts of RemotePixel; no successor is documented on the closure page.</p>

</details>

<h3>Sentinelhub — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -172,7 +172,7 @@
 * [Office for Coastal Management's Digital Coast](https://coast.noaa.gov/digitalcoast/data/)
 * [Planet API](https://developers.planet.com/docs/api/) - Programmatic support for searching, clipping, ordering, and viewing satellite imagery on a map. Currently offers a free plan with access to low-resolution imagery worldwide.
 * [Remotepixel](https://remotepixel.ca/) - A collection of tools, including the RemotePixel Viewer, Satellite Search tool, and Disasterwatch, for exploring and downloading satellite imagery, maintained by one hardworking volunteer.
-* [Sentinelhub](https://www.sentinel-hub.com/explore/) - ESA's EO Browser and Sentinel Playground offer a complete archive of Sentinel-1, Sentinel-2, Sentinel-3, Sentinel-5P, ESA's archive of Landsat 5, 7 and 8, global coverage of Landsat 8, Envisat Meris, MODIS, Proba-V and GIBS products in one place.
+* [Sentinelhub](https://www.sentinel-hub.com/explore/) - Sinergise's EO Browser and Sentinel Hub API for browsing, comparing, and downloading Sentinel-1, -2, -3, -5P, Landsat, MODIS, Envisat and other public and commercial satellite imagery collections.
 * [USGS EarthExplorer](https://earthexplorer.usgs.gov/) - A tool that provides users the ability to query, search, and retrieve satellite images, aerial photographs, and cartographic products from several sources
 * [Visible Earth](https://visibleearth.nasa.gov/) - A catalog of NASA images and animations of our home planet
 * [Worldview](https://worldview.earthdata.nasa.gov/) - A NASA app that provides the capability to interactively browse over 800 global, full-resolution satellite imagery layers and then download the underlying data
```

<details>
<summary>Evidence and limitations</summary>

<p>The page is reachable and relevant, but the description contains false or outdated claims. Sentinel Hub and EO Browser are owned and operated by Sinergise, not ESA. Sentinel Playground has been retired: its app URL now redirects to the Copernicus Browser. The current data list no longer includes Proba-V or GIBS. The remaining listed collections (Sentinel-1/2/3/5P, Landsat, MODIS, Envisat) are still offered.</p>

<p>https://www.sentinel-hub.com/explore/ — Explore page features EO Browser, Data, Sentinel Hub API, and a link to the Copernicus Data Space Ecosystem. Footer: &#x27;Owned and Operated by Sinergise Solutions d.o.o.&#x27;</p>

<p>https://apps.sentinel-hub.com/sentinel-playground/ — Redirects to https://browser.dataspace.copernicus.eu/ (Copernicus Browser), so Sentinel Playground is no longer a Sentinel Hub app.</p>

<p>https://www.sentinel-hub.com/explore/data/ — Collections listed: Sentinel-1, Sentinel-2 L1C/L2A, Sentinel-3 OLCI/SLSTR, Sentinel-5P, Landsat 1-9, Planet and Maxar commercial collections, DEMs, Envisat, MODIS MCD43A4, Copernicus services, and BYOD. Proba-V and GIBS are not listed.</p>

<p>https://www.sentinel-hub.com/explore/eobrowser/ — EO Browser lets users browse and compare full-resolution images from all collections, create timelapses, and download images. Some features require login.</p>

<p>Caveats: Third-party search results claim EO Browser will be deprecated in favor of Planet Insights Platform or Copernicus Browser; this was not confirmed on an official page and should be rechecked.; The Collections Catalogue was not read in full; Proba-V or GIBS might still exist there as &#x27;other public collections&#x27;.</p>

</details>

<h3>Visible Earth — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -170,11 +170,11 @@
 * [National Environmental Satellite Data and Information Service](https://www.nesdis.noaa.gov/) - Explore NOAA satellite maps and imagery in 2D and 3D.
 * [NOAA Data Access Viewer](https://coast.noaa.gov/dataviewer/#/)
 * [Office for Coastal Management's Digital Coast](https://coast.noaa.gov/digitalcoast/data/)
+* [NASA Earth Observatory](https://science.nasa.gov/earth/earth-observatory/) - NASA's images, global maps and stories of our home planet, now including the former Visible Earth image catalog
 * [Planet API](https://developers.planet.com/docs/api/) - Programmatic support for searching, clipping, ordering, and viewing satellite imagery on a map. Currently offers a free plan with access to low-resolution imagery worldwide.
 * [Remotepixel](https://remotepixel.ca/) - A collection of tools, including the RemotePixel Viewer, Satellite Search tool, and Disasterwatch, for exploring and downloading satellite imagery, maintained by one hardworking volunteer.
 * [Sentinelhub](https://www.sentinel-hub.com/explore/) - ESA's EO Browser and Sentinel Playground offer a complete archive of Sentinel-1, Sentinel-2, Sentinel-3, Sentinel-5P, ESA's archive of Landsat 5, 7 and 8, global coverage of Landsat 8, Envisat Meris, MODIS, Proba-V and GIBS products in one place.
 * [USGS EarthExplorer](https://earthexplorer.usgs.gov/) - A tool that provides users the ability to query, search, and retrieve satellite images, aerial photographs, and cartographic products from several sources
-* [Visible Earth](https://visibleearth.nasa.gov/) - A catalog of NASA images and animations of our home planet
 * [Worldview](https://worldview.earthdata.nasa.gov/) - A NASA app that provides the capability to interactively browse over 800 global, full-resolution satellite imagery layers and then download the underlying data
 * [Yale's Center for Earth Observation](https://yceo.yale.edu/image-sources) - A directory of imagry and data sources.
 
```

<details>
<summary>Evidence and limitations</summary>

<p>visibleearth.nasa.gov now redirects to NASA Earth Observatory on science.nasa.gov. Deep Visible Earth image and collection URLs map item by item to Earth Observatory pages (e.g., earthshine, Blue Marble), which shows NASA migrated the catalog there. The content remains relevant, but the listed name and URL are no longer the canonical destination.</p>

<p>https://visibleearth.nasa.gov/ — HTTP redirect resolves to https://science.nasa.gov/earth/earth-observatory/.</p>

<p>https://visibleearth.nasa.gov/images/83782/earthshine — Redirects to https://science.nasa.gov/earth/earth-observatory/earthshine-83782/, preserving the image ID.</p>

<p>https://visibleearth.nasa.gov/collection/1484/blue-marble — Redirects to https://science.nasa.gov/earth/earth-observatory/collections/blue-marble/.</p>

<p>https://science.nasa.gov/earth/earth-observatory/ — Earth Observatory offers Image of the Day (3,156 archive pages), Collections, Global Maps, World of Change, and Blue Marble: Next Generation. It describes itself as bringing &#x27;the images, stories, and discoveries about the environment, Earth systems, and climate that emerge from NASA research.&#x27;</p>

<p>Caveats: No explicit NASA announcement of the Visible Earth migration was found; the conclusion rests on the official redirects.; The completeness of the migrated catalog (e.g., animations) was not checked.</p>

</details>

<h3>Worldview — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -175,7 +175,7 @@
 * [Sentinelhub](https://www.sentinel-hub.com/explore/) - ESA's EO Browser and Sentinel Playground offer a complete archive of Sentinel-1, Sentinel-2, Sentinel-3, Sentinel-5P, ESA's archive of Landsat 5, 7 and 8, global coverage of Landsat 8, Envisat Meris, MODIS, Proba-V and GIBS products in one place.
 * [USGS EarthExplorer](https://earthexplorer.usgs.gov/) - A tool that provides users the ability to query, search, and retrieve satellite images, aerial photographs, and cartographic products from several sources
 * [Visible Earth](https://visibleearth.nasa.gov/) - A catalog of NASA images and animations of our home planet
-* [Worldview](https://worldview.earthdata.nasa.gov/) - A NASA app that provides the capability to interactively browse over 800 global, full-resolution satellite imagery layers and then download the underlying data
+* [Worldview](https://worldview.earthdata.nasa.gov/) - A NASA app for interactively browsing more than a thousand global, full-resolution satellite imagery layers and downloading the underlying data
 * [Yale's Center for Earth Observation](https://yceo.yale.edu/image-sources) - A directory of imagry and data sources.
 
 ### Extrasolar Planets
```

<details>
<summary>Evidence and limitations</summary>

<p>Worldview is live and relevant, but the &#x27;over 800&#x27; layer count is outdated. NASA Earthdata now says Worldview lets users browse, compare, animate, and download &#x27;over 1,200 visualized satellite data products.&#x27; Recommend durable wording without a volatile count.</p>

<p>https://worldview.earthdata.nasa.gov/ — Resolves (200) to the NASA Worldview app, which is client-rendered.</p>

<p>https://www.earthdata.nasa.gov/data/tools/worldview — &#x27;Worldview is an easy-to-use visualization tool that allows users to interactively browse, compare, animate, and download over 1,200 visualized satellite data products.&#x27; Also mentions near-real-time imagery, geostationary layers, and Worldview Snapshots.</p>

<p>Caveats: The app itself is JavaScript-rendered; the layer count was taken from the official Earthdata tool page.</p>

</details>

<h3>Launches and the satellites they carried — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -190,7 +190,7 @@
 
 * [Launch Dashboard API](https://github.com/shahar603/Launch-Dashboard-API) -  Open Source REST API for rocket launch telemetry
 * [Launch Library 2](https://thespacedevs.com/llapi) - A free to use API with rocket launches, astronauts, events, etc. that application developers can use. It is the successor of the original Launch Library and Space Launch Now APIs. As it is maintained by [The Space Devs](https://thespacedevs.com/), news and support are provided on their [Discord server](https://discord.gg/wxEGcWXbsD).
-* [Launches and the satellites they carried](https://mcval.org/launches/data) - Every orbital and suborbital launch since Sputnik and every payload in CelesTrak's catalogue, each satellite linked to its launch by COSPAR number, with users and operators from GCAT. Two CSVs, CC BY 4.0, rebuilt weekly.
+* [Launches and the satellites they carried](https://mcval.org/launches/data) - Every launch since Sputnik recorded by Launch Library 2 and every payload in CelesTrak's catalogue, each satellite linked to its launch by COSPAR number, with users and operators from GCAT. Two CSVs, CC BY 4.0, versioned on Zenodo.
 * [RocketLaunch.Live](https://www.rocketlaunch.live/api) - JSON API of upcoming and past rocket launches, hand-curated in real time, with launch windows, vehicles, pads, missions, and est. dates for unscheduled launches. Free tier returns the next 5 launches.
 * [Unofficial SpaceX REST API](https://docs.spacexdata.com/) - Open Source REST API for rocket, core, capsule, pad, and launch data
 
```

<details>
<summary>Evidence and limitations</summary>

<p>The dataset is live and current (version 2026-11-09; 7,658 launches and 28,304 payloads; CC BY 4.0; two CSVs; COSPAR linking; GCAT users/operators — all confirmed). Two claims are not supported. (1) &#x27;Every orbital and suborbital launch&#x27;: launches come from Launch Library 2, which says it tracks all orbital launches but only &#x27;a number of popular suborbital launches,&#x27; so not every suborbital launch is included. (2) &#x27;Rebuilt weekly&#x27; is not stated on the page or in the data dictionary, which instead give dated Zenodo versions.</p>

<p>https://mcval.org/launches/data — &#x27;7,658 launches from 1957-10-04 to 2026-11-08, and 28,304 payloads, every one linked to the launch that carried it by the COSPAR launch number.&#x27; launches.csv and satellites.csv, CC BY 4.0, version 2026-11-09, DOI 10.5281/zenodo.23184904. Built from Launch Library 2, CelesTrak, and GCAT.</p>

<p>https://mcval.org/launches/data/dictionary.md — Explains that the COSPAR join and users/operators come from GCAT. &#x27;Launches that left nothing in orbit, such as failures and suborbital flights, have no COSPAR launch number.&#x27; No rebuild cadence stated.</p>

<p>https://thespacedevs.com/llapi — Upstream source: &#x27;We track all orbital launches and a number of popular suborbital launches.&#x27;</p>

<p>https://mcval.org/launches/data/launches.csv — CSV downloads (7,658 rows) with columns launch_id, date_utc, cospar_launch, rocket, provider, outcome, orbit, payloads_catalogued, etc.</p>

<p>Caveats: Update cadence may in fact be weekly; it is simply not documented on the official pages read, so the proposed text omits it rather than contradicting it.; Whether every CelesTrak payload (vs. debris/rocket bodies) is included was not independently counted.</p>

</details>

<h3>Unofficial SpaceX REST API — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -192,7 +192,7 @@
 * [Launch Library 2](https://thespacedevs.com/llapi) - A free to use API with rocket launches, astronauts, events, etc. that application developers can use. It is the successor of the original Launch Library and Space Launch Now APIs. As it is maintained by [The Space Devs](https://thespacedevs.com/), news and support are provided on their [Discord server](https://discord.gg/wxEGcWXbsD).
 * [Launches and the satellites they carried](https://mcval.org/launches/data) - Every orbital and suborbital launch since Sputnik and every payload in CelesTrak's catalogue, each satellite linked to its launch by COSPAR number, with users and operators from GCAT. Two CSVs, CC BY 4.0, rebuilt weekly.
 * [RocketLaunch.Live](https://www.rocketlaunch.live/api) - JSON API of upcoming and past rocket launches, hand-curated in real time, with launch windows, vehicles, pads, missions, and est. dates for unscheduled launches. Free tier returns the next 5 launches.
-* [Unofficial SpaceX REST API](https://docs.spacexdata.com/) - Open Source REST API for rocket, core, capsule, pad, and launch data
+* [Unofficial SpaceX REST API](https://github.com/r-spacex/SpaceX-API) - Open Source REST API for launch, rocket, core, capsule, Starlink, launchpad, and landing pad data
 
 ### Solar System Data
 
```

<details>
<summary>Evidence and limitations</summary>

<p>docs.spacexdata.com is the Postman-hosted V3 documentation. It says &#x27;The V3 API is deprecated as of November 2020... no new data will be added or updated&#x27; and directs users to the V4 docs in the r-spacex/SpaceX-API GitHub repository. The project itself is still relevant; the canonical current documentation is the GitHub repo, whose README describes the API as covering launch, rocket, core, capsule, starlink, launchpad, and landing pad data.</p>

<p>https://docs.spacexdata.com/ — Page meta description: &#x27;NOTICE: The V3 API is deprecated as of November 2020! All existing links will continue to work, but no new data will be added or updated. I strongly encourage you to move to V4 (https://github.com/r-spacex/SpaceX-API/tree/master/docs)&#x27;.</p>

<p>https://github.com/r-spacex/SpaceX-API — Resolves (200) without redirect; this is the canonical repository referenced by the V3 docs notice.</p>

<p>https://raw.githubusercontent.com/r-spacex/SpaceX-API/master/README.md — &#x27;SpaceX REST API — Open Source REST API for launch, rocket, core, capsule, starlink, launchpad, and landing pad data.&#x27; Not affiliated with SpaceX. Usage example: GET https://api.spacexdata.com/v5/launches/latest.</p>

<p>Caveats: api.spacexdata.com/v5/launches/latest returned HTTP 522 at check time. The hosted API&#x27;s operational status and data freshness are unknown and should be rechecked; this does not affect the docs/URL correction.; Repository archive status and last commit date could not be read via the GitHub API (local TLS error).</p>

</details>

<h3>LROC QuickMap — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -199,7 +199,7 @@
 * [Asterank](http://www.asterank.com/) - Asterank is a scientific and economic database of over 600,000 asteroids.
 * [astorbDB](https://asteroid.lowell.edu/) - A database of orbital elements and observed physical properties (when available) for all known minor planets in the Solar System.
 * [IAU Minor Planet Center](https://minorplanetcenter.net/data) - Clearing house for observations of asteroids and other smaller solar system bodies
-* [LROC QuickMap](https://quickmap.lroc.asu.edu) - Quality 2D and 3D maps of the moon
+* [LROC QuickMap](https://quickmap.lroc.im-ldi.com/) - Quality 2D and 3D maps of the Moon
 * [NASA's Planetary Data System](https://pds.jpl.nasa.gov/) - A long-term archive of digital data products returned from NASA's planetary missions
 * [NASA's Solar System Treks](https://trek.nasa.gov/) - Access surface elevation profiles, sun angles, 3D print files, and VR experiences in our solar system
 * [Planetary Atlas](https://planetatlas.org) - Zoomable maps of 14 worlds built from open NASA, USGS, ESA and JAXA imagery, with IAU nomenclature and surface mission landing sites
```

<details>
<summary>Evidence and limitations</summary>

<p>The tool is still live and the description still fits. The listed asu.edu hostname now returns a permanent 301 redirect to quickmap.lroc.im-ldi.com, and the parent site lroc.asu.edu returned 502. The official LROC site now lives at lroc.im-ldi.com and links to QuickMap, so the listed URL should be updated to the redirect target. The description &#x27;2D and 3D maps of the moon&#x27; matches the page&#x27;s own meta description.</p>

<p>https://quickmap.lroc.asu.edu — Returned HTTP/2 301 with location: https://quickmap.lroc.im-ldi.com/.</p>

<p>https://quickmap.lroc.im-ldi.com/ — Meta description: &#x27;LROC QuickMap, a powerful map interface to browse Lunar data from NASA/LRO and other missions. Explore the Moon in both 2D and 3D. Developed by Applied Coherent Technology and customized for the LROC team at ASU&#x27;.</p>

<p>https://lroc.im-ldi.com/ — The LROC Science Operations Center site (Phoenix, Arizona) lists &#x27;Lunar QuickMap&#x27; under Mapping Tools and links to https://quickmap.im-ldi.com/. Its footer links to both Intuitive Machines and ASU.</p>

<p>https://quickmap.im-ldi.com/ — Returns 200 and serves the same QuickMap app with the same meta description.</p>

<p>Caveats: Two official hostnames serve the app: quickmap.lroc.im-ldi.com (target of the 301 redirect) and quickmap.im-ldi.com (linked from the LROC home page). Either works. I chose the redirect target.; The interactive app needs JavaScript and was not exercised.; Optional: capitalize &#x27;moon&#x27; as &#x27;Moon&#x27;.</p>

</details>

<h3>NASA&#x27;s Planetary Data System — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -200,7 +200,7 @@
 * [astorbDB](https://asteroid.lowell.edu/) - A database of orbital elements and observed physical properties (when available) for all known minor planets in the Solar System.
 * [IAU Minor Planet Center](https://minorplanetcenter.net/data) - Clearing house for observations of asteroids and other smaller solar system bodies
 * [LROC QuickMap](https://quickmap.lroc.asu.edu) - Quality 2D and 3D maps of the moon
-* [NASA's Planetary Data System](https://pds.jpl.nasa.gov/) - A long-term archive of digital data products returned from NASA's planetary missions
+* [NASA's Planetary Data System](https://pds.nasa.gov/) - A long-term archive of digital data products returned from NASA's planetary missions
 * [NASA's Solar System Treks](https://trek.nasa.gov/) - Access surface elevation profiles, sun angles, 3D print files, and VR experiences in our solar system
 * [Planetary Atlas](https://planetatlas.org) - Zoomable maps of 14 worlds built from open NASA, USGS, ESA and JAXA imagery, with IAU nomenclature and surface mission landing sites
 * [planetary-dem-to-stl](https://github.com/SimplySolid3D/planetary-dem-to-stl) - Turns any area of the Moon or Mars into a 3D-printable STL from NASA LOLA and MOLA elevation data
```

<details>
<summary>Evidence and limitations</summary>

<p>pds.jpl.nasa.gov permanently redirects (301) to pds.nasa.gov, which is the current PDS home page. The site still lists frequent new mission data releases (for example Artemis II, LRO, MRO and Juno in 2026), so the description is accurate. Only the URL needs updating.</p>

<p>https://pds.jpl.nasa.gov/ — Returned HTTP/2 301 with location: https://pds.nasa.gov/.</p>

<p>https://pds.nasa.gov/ — &#x27;Welcome to the Planetary Data System&#x27; page with Data Search, Tools and Data Standards. New Releases include &#x27;October 7, 2026 Artemis II Mission Data Release&#x27; and &#x27;October 1, 2026 Odyssey Data Release 97&#x27;.</p>

</details>

<h3>Celestrak — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -209,7 +209,7 @@
 
 #### Orbits
 
-* [Celestrak](http://celestrak.com) - Celestrak is the world's oldest source for orbital element sets (and related software and educational materials).
+* [Celestrak](https://celestrak.org/) - Long-running free source of orbital element sets (and related software and educational materials).
 * [JPL's HORIZONS](https://ssd.jpl.nasa.gov/horizons.cgi) - Generate ephemerides for solar-system bodies
 * [Space Physics Data Facility](https://spdf.gsfc.nasa.gov/data_orbits.html) - Web-based services for survey and high resolution data and trajectories
 
```

<details>
<summary>Evidence and limitations</summary>

<p>celestrak.com now permanently redirects (301) to celestrak.org, which also serves over HTTPS, so the URL should be updated. I could not find official support for the superlative &#x27;world&#x27;s oldest source&#x27;. CelesTrak&#x27;s own history only says its BBS predecessor started in 1985 and the website went online in 1998. I suggest durable wording without the unverified claim. The site still provides GP element sets, a software repository and tutorials.</p>

<p>http://celestrak.com — Returned HTTP/1.1 301 Moved Permanently with location: http://celestrak.org/.</p>

<p>https://celestrak.org/ — Returns 200. Offers NORAD GP Element Sets, Supplemental GP data, Documentation, a Software Repository and Orbital Mechanics Software Tutorials. It is run as a 501(c)(3) non-profit and notes 6-digit catalog numbers in use since 2026-07-11.</p>

<p>https://celestrak.org/brief-history.php — The Celestial BBS was set up in 1985 and the CelesTrak site went online on 1998 March 5. I found no &#x27;world&#x27;s oldest&#x27; claim.</p>

<p>Caveats: Removing the superlative is a wording choice. I did not prove it false, only failed to find support for it.; I did not search every CelesTrak page for an &#x27;oldest&#x27; claim.</p>

</details>

<h3>JPL&#x27;s HORIZONS — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -210,7 +210,7 @@
 #### Orbits
 
 * [Celestrak](http://celestrak.com) - Celestrak is the world's oldest source for orbital element sets (and related software and educational materials).
-* [JPL's HORIZONS](https://ssd.jpl.nasa.gov/horizons.cgi) - Generate ephemerides for solar-system bodies
+* [JPL's HORIZONS](https://ssd.jpl.nasa.gov/horizons/) - Generate ephemerides for solar-system bodies
 * [Space Physics Data Facility](https://spdf.gsfc.nasa.gov/data_orbits.html) - Web-based services for survey and high resolution data and trajectories
 
 ### Space News
```

<details>
<summary>Evidence and limitations</summary>

<p>The legacy horizons.cgi URL now 301-redirects to the new Horizons app. The canonical Horizons page is https://ssd.jpl.nasa.gov/horizons/. The description is still accurate.</p>

<p>https://ssd.jpl.nasa.gov/horizons.cgi — Returned HTTP/1.1 301 Moved Permanently with Location: https://ssd.jpl.nasa.gov/horizons/app.html.</p>

<p>https://ssd.jpl.nasa.gov/horizons/ — Returns 200. The &#x27;Horizons System&#x27; page appears under JPL SSD &#x27;Orbits &amp; Ephemerides&#x27; alongside APIs.</p>

<p>Caveats: https://ssd.jpl.nasa.gov/horizons/app.html (the web app itself) would also be a valid target.</p>

</details>

<h3>FreeFlyer — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -254,7 +254,7 @@
 * [Copernicus](https://www.nasa.gov/general/copernicus/) - Copernicus, a generalized spacecraft trajectory design and optimization system, is capable of solving a wide range of trajectory problems such as planet or moon centered trajectories, libration point trajectories, planet-moon transfers and tours, and all types of interplanetary and asteroid/comet missions. (NASA)
 * [Delta V calculator for LEO/MEO/GEO injection](http://www.satsig.net/orbit-research/delta-v-geo-injection-calculator.htm)
 * [Flight Club](https://www2.flightclub.io/) - Orbital launch simulator and trajectory visualisation software
-* [FreeFlyer](https://ai-solutions.com/freeflyer/) - A software application for space mission design, analysis, and operations.
+* [FreeFlyer](https://ai-solutions.com/freeflyer-features/) - A software application for space mission design, analysis, and operations.
 * [GMAT](https://sourceforge.net/projects/gmat/) - The General Mission Analysis Tool (GMAT) is a space trajectory optimization and mission analysis system (NASA)
 * [GO by ienai SPACE](https://go.ienai.space) - A software tool which allows for general design and optimization of missions with electric propulsion systems.
 * [NASA Ames Research Center Trajectory Browser](https://trajbrowser.arc.nasa.gov/traj_browser.php) - A tool to find spacecraft trajectories to planets and small-bodies
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL https://ai-solutions.com/freeflyer/ now returns a 301 redirect to the a.i. solutions company homepage. A dedicated FreeFlyer page still exists at /freeflyer-features/ and covers mission design, analysis and operations features (proximity ops, RF link analysis, interplanetary mission design). FreeFlyer is still an active product. Only the URL needs to change.</p>

<p>https://ai-solutions.com/freeflyer/ — A HEAD request returns &#x27;HTTP/2 301, location: https://ai-solutions.com/&#x27;.</p>

<p>https://ai-solutions.com/ — Company homepage. Navigation lists &#x27;FreeFlyer® Astrodynamics Software&#x27;, &#x27;FreeFlyer Features&#x27;, &#x27;FreeFlyer 8 - Help File&#x27;, &#x27;Order FreeFlyer&#x27;.</p>

<p>https://ai-solutions.com/freeflyer-features/ — HTTP 200. Title &#x27;FreeFlyer Astrodynamics Modeling &amp; Visualization Features&#x27;. Covers relative motion and proximity operations, RF link analysis, coverage and contact analysis, and interplanetary mission design.</p>

<p>Caveats: The maintainer may prefer a different FreeFlyer subpage (for example /freeflyer-heritage/) or the homepage itself. The features page is the most product-specific page found.</p>

</details>

<h3>Open Satellite Project — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -237,7 +237,7 @@
 
 * [FoxTelem](https://www.g0kla.com/foxtelem/) - FoxTelem is used by a network of ground stations to retrieve the telemetry and experiment data from the Fox Satellites.
 * [GRID](https://www.gridgs.com/) - Commercial network of satellite groundstations with simple to use [Python SDK](https://github.com/5OKB/grid-python-sdk).
-* [Open Satellite Project](https://limemicro.com/community/open-satellite-project/) - Ongoing effort to develop open-source software for the receipt and decoding of satellite data using software-defined radio (SDR) hardware
+* [Open Satellite Project](https://github.com/opensatelliteproject) - Open-source software for the receipt and decoding of satellite data using software-defined radio (SDR) hardware
 * [Phase 4 Ground](https://github.com/phase4ground) - Open source digital broadband satellite and terrestrial radio systems, part of Open Research Institute
 * [SatNOGS](https://satnogs.org/) - A global network of satellite ground stations, designed as an open source participatory project
 * [TinyGS](https://tinygs.com/) - Open network of ground stations to receive and operate LoRa satellites using cheap and versatile modules
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed Lime Microsystems URL now returns 404, and the /community/ section is gone from Lime&#x27;s site. A Wayback snapshot from July 2024 shows the page was a Lime community article about Lucas Teske&#x27;s Open Satellite Project, using the entry&#x27;s wording. The project has its own GitHub organization, &#x27;Open Satellite Project&#x27; (github.com/opensatelliteproject), with 16 repos of satellite receive and decode software (xritdemod, goesdump, SatHelperApp, libsathelper). Recommend pointing to the project&#x27;s own home and dropping the unverifiable &#x27;Ongoing&#x27;.</p>

<p>https://limemicro.com/community/open-satellite-project/ — HTTP 404 &#x27;Page not found&#x27;. https://limemicro.com/community/ also returns 404.</p>

<p>https://web.archive.org/web/20240727180618/https://limemicro.com/community/open-satellite-project/ — Archived Lime article: &#x27;the Open Satellite Project, an ongoing effort to develop open-source software for the receipt and decoding of satellite data using software-defined radio (SDR) hardware including the LimeSDR family&#x27;, attributed to Lucas Teske.</p>

<p>https://github.com/opensatelliteproject — HTTP 200. GitHub org titled &#x27;Open Satellite Project&#x27;, &#x27;The Open Source Satellite Project&#x27;, with 16 repositories including xritdemod, goesdump, SatHelperApp, libsathelper, tlmdemod.</p>

<p>https://raw.githubusercontent.com/opensatelliteproject/SatHelperApp/master/README.md — &#x27;The OpenSatelliteProject Satellite Helper Application! ... LRIT/HRIT Demodulator / Decoder program&#x27;. Marked WIP/Alpha.</p>

<p>https://opensatelliteproject.github.io/OpenSatelliteProject/ — Project information site, &#x27;View on GitHub&#x27;, with a compiling guide. Content is sparse (&#x27;TODO: Write this page&#x27;).</p>

<p>Caveats: Recent commit activity in the org was not checked because the GitHub API was rate-limited. The &#x27;Ongoing&#x27; wording is dropped because current activity is unverified, not because the project is confirmed inactive.; The link between the GitHub org and Lucas Teske was inferred from the matching project name and software scope. It was not checked against the org&#x27;s member list.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Phase 4 Ground — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -237,8 +237,8 @@
 
 * [FoxTelem](https://www.g0kla.com/foxtelem/) - FoxTelem is used by a network of ground stations to retrieve the telemetry and experiment data from the Fox Satellites.
 * [GRID](https://www.gridgs.com/) - Commercial network of satellite groundstations with simple to use [Python SDK](https://github.com/5OKB/grid-python-sdk).
+* [Open Research Institute](https://github.com/OpenResearchInstitute) - Open source digital broadband satellite and terrestrial radio systems (DVB-S2/S2X), formerly Phase 4 Ground
 * [Open Satellite Project](https://limemicro.com/community/open-satellite-project/) - Ongoing effort to develop open-source software for the receipt and decoding of satellite data using software-defined radio (SDR) hardware
-* [Phase 4 Ground](https://github.com/phase4ground) - Open source digital broadband satellite and terrestrial radio systems, part of Open Research Institute
 * [SatNOGS](https://satnogs.org/) - A global network of satellite ground stations, designed as an open source participatory project
 * [TinyGS](https://tinygs.com/) - Open network of ground stations to receive and operate LoRa satellites using cheap and versatile modules
 
```

<details>
<summary>Evidence and limitations</summary>

<p>The phase4ground GitHub org now contains only a .github repo. Its profile README says: &#x27;phase4ground is now OpenResearchInstitute... Please use https://github.com/OpenResearchInstitute instead&#x27;. The OpenResearchInstitute org&#x27;s description is almost identical to the entry (&#x27;Open source digital broadband satellite and terrestrial radio systems implementing DVB-S2 and DVB-S2X&#x27;), and it hosts repos such as dvb_fpga and the msk modem work. This is an official rename, so the URL and name should change.</p>

<p>https://github.com/phase4ground — HTTP 200, but &#x27;Showing 1 of 1 repositories: .github&#x27;. The only repo was last updated Feb 11, 2023.</p>

<p>https://raw.githubusercontent.com/phase4ground/.github/main/profile/README.md — &#x27;# phase4ground is now OpenResearchInstitute. We&#x27;ve renamed this organization on GitHub... Please use https://github.com/OpenResearchInstitute instead of phase4ground from now on.&#x27;</p>

<p>https://github.com/OpenResearchInstitute — HTTP 200. Org &#x27;Open Research Institute&#x27;. Meta description: &#x27;Open source digital broadband satellite and terrestrial radio systems implementing DVB-S2 and DVB-S2X.&#x27; Repos include dvb_fpga, pluto_msk, msk_modulator, msk_demodulator, opv-cxx-demod.</p>

<p>https://www.openresearch.institute/ — Open Research Institute site: a non-profit open source and open access R&amp;D organization, with current amateur radio and satellite news.</p>

<p>Caveats: The ORI org now holds broader projects (EME, Ribbit and others) beyond the original Phase 4 Ground scope. Its stated focus is still satellite and terrestrial radio systems.; The maintainer could keep the &#x27;Phase 4 Ground&#x27; name with only the URL changed. Renaming follows the official rename of the org.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Flight Club — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -253,7 +253,7 @@
 
 * [Copernicus](https://www.nasa.gov/general/copernicus/) - Copernicus, a generalized spacecraft trajectory design and optimization system, is capable of solving a wide range of trajectory problems such as planet or moon centered trajectories, libration point trajectories, planet-moon transfers and tours, and all types of interplanetary and asteroid/comet missions. (NASA)
 * [Delta V calculator for LEO/MEO/GEO injection](http://www.satsig.net/orbit-research/delta-v-geo-injection-calculator.htm)
-* [Flight Club](https://www2.flightclub.io/) - Orbital launch simulator and trajectory visualisation software
+* [Flight Club](https://flightclub.io/) - Orbital launch simulator and trajectory visualisation software
 * [FreeFlyer](https://ai-solutions.com/freeflyer/) - A software application for space mission design, analysis, and operations.
 * [GMAT](https://sourceforge.net/projects/gmat/) - The General Mission Analysis Tool (GMAT) is a space trajectory optimization and mission analysis system (NASA)
 * [GO by ienai SPACE](https://go.ienai.space) - A software tool which allows for general design and optimization of missions with electric propulsion systems.
```

<details>
<summary>Evidence and limitations</summary>

<p>www2.flightclub.io could not be reached (the proxy reported a CONNECT 502, which is consistent with DNS or host failure). The Wayback CDX index for www2.flightclub.io shows captures from Aug to Oct 2026 resolving to https://flightclub.io/, so the www2 host now leads to the apex domain. flightclub.io is live and its own metadata matches the entry: &#x27;Flight Club is the rocket launch simulator and orbital trajectory visualiser&#x27;.</p>

<p>https://www2.flightclub.io/ — Fetch failed: &#x27;CONNECT tunnel failed, response 502&#x27;. No HTTP response from the host.</p>

<p>https://web.archive.org/cdx/search/cdx?url=www2.flightclub.io&amp;output=txt&amp;limit=-4 — Captures recorded under www2.flightclub.io (2026-08-31, 2026-09-18, 2026-10-13) list https://flightclub.io/ as the original URL. www.flightclub.io gives a 308.</p>

<p>https://flightclub.io/ — HTTP 200. Title &#x27;Flight Club&#x27;. og:url https://flightclub.io. Meta description: &#x27;Flight Club is the rocket launch simulator and orbital trajectory visualiser for all things space!&#x27;</p>

<p>Caveats: www2 failed through the sandbox proxy, so a live redirect from www2 could not be confirmed directly. This may be a temporary DNS or proxy issue. The canonical apex URL is still confirmed by the site&#x27;s own og:url.; flightclub.io is a JavaScript app, and only its metadata was read.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>GO by ienai SPACE — replace</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -253,10 +253,10 @@
 
 * [Copernicus](https://www.nasa.gov/general/copernicus/) - Copernicus, a generalized spacecraft trajectory design and optimization system, is capable of solving a wide range of trajectory problems such as planet or moon centered trajectories, libration point trajectories, planet-moon transfers and tours, and all types of interplanetary and asteroid/comet missions. (NASA)
 * [Delta V calculator for LEO/MEO/GEO injection](http://www.satsig.net/orbit-research/delta-v-geo-injection-calculator.htm)
+* [360 by IENAI Space](https://ienai.space/ienai-360/) - Mission and space mobility analysis software (successor to IENAI's GO) for designing and optimizing missions and maneuvers with in-space propulsion, available as a Python library and web studio.
 * [Flight Club](https://www2.flightclub.io/) - Orbital launch simulator and trajectory visualisation software
 * [FreeFlyer](https://ai-solutions.com/freeflyer/) - A software application for space mission design, analysis, and operations.
 * [GMAT](https://sourceforge.net/projects/gmat/) - The General Mission Analysis Tool (GMAT) is a space trajectory optimization and mission analysis system (NASA)
-* [GO by ienai SPACE](https://go.ienai.space) - A software tool which allows for general design and optimization of missions with electric propulsion systems.
 * [NASA Ames Research Center Trajectory Browser](https://trajbrowser.arc.nasa.gov/traj_browser.php) - A tool to find spacecraft trajectories to planets and small-bodies
 * [Nyx](https://github.com/nyx-space/nyx) - Nyx is a high fidelity astrodynamics toolkit for mission design and orbit determination in Rust and Python, used on several lunar missions.
 * [Open Space Toolkit](https://github.com/open-space-collective/open-space-toolkit) - Collection of versatile software libraries for space engineering applications (e.g., environment modeling, orbit and access computation).
```

<details>
<summary>Evidence and limitations</summary>

<p>go.ienai.space currently returns 502. An October 2025 Wayback capture of the official GO page says GO &#x27;has been discontinued&#x27; and that IENAI has &#x27;launched a powerful new solution designed to take its place&#x27;: 360™, a mission analysis tool with space mobility analysis, thruster models and propulsive phase optimization. IENAI&#x27;s current site promotes 360™ as its mission and space mobility analysis software at ienai.space/ienai-360/. This is an officially documented successor from the same vendor.</p>

<p>https://go.ienai.space — HTTP 502 at fetch time.</p>

<p>https://web.archive.org/web/20251006145938/https://go.ienai.space/ — Official GO page (Oct 2025): &#x27;Sorry, has been discontinued. But good news: we&#x27;ve launched a powerful new solution designed to take its place... What is 360™ software? 360™ is a mission analysis tool with a cutting-edge space mobility analysis capability... Space Mobility analysis and optimization through state-of-the-art thruster models, propulsive phase definition&#x27;.</p>

<p>https://ienai.space/ — HTTP 200. &#x27;360™ MISSION &amp; SPACE MOBILITY ANALYSIS SUITE: Advanced mission and space mobility analysis tool, streamlining space systems design, operations planning and maneuvering strategies&#x27;. Links to /ienai-360/ and the i360.ienai.space login.</p>

<p>https://ienai.space/ienai-360/ — HTTP 200. 360 product page: available as a Python &#x27;360-library&#x27; to install locally or as the web-based &#x27;360-studio&#x27;. Customer case studies cover propulsion architecture and maneuvering feasibility studies. Paid tiers are listed.</p>

<p>Caveats: 360 appears to be a paid, tiered commercial product. GO&#x27;s access model is unknown.; 360&#x27;s description emphasizes broader mission and space-mobility analysis, not only electric propulsion. The proposed wording reflects that.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Systems Tool Kit (STK) — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -266,7 +266,7 @@
 * [SPENVIS](https://www.spenvis.oma.be/) - SPENVIS is ESA's SPace ENVironment Information System, a web interface to models of the space environment and its effects; including galactic cosmic rays, solar energetic particles, natural radiation belts, plasmas, gases, meteoroids and debris.
 * [SPICE](https://naif.jpl.nasa.gov/naif/toolkit.html) - Ephemerides library used by JPL for their missions. [SpiceyPy](https://github.com/AndrewAnnex/SpiceyPy) is a Python wrapper.
 * [SpOCK](https://github.com/deflorio/SpOCK/) - The Spacecraft Orbital Computations Kit is an open source tool for spacecraft mission analysis and simulation.
-* [Systems Tool Kit (STK)](https://www.agi.com/products/stk) - Simulate missions and create reports, graphs, and 3D animations (paid). From Analytical Graphics, Inc.
+* [Systems Tool Kit (STK)](https://ansys.synopsys.com/products/missions/ansys-stk) - Simulate missions and create reports, graphs, and 3D animations (paid). Now Ansys STK; originally from Analytical Graphics, Inc. (AGI).
 
 ### Simulation
 
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed agi.com URL now redirects to an Ansys page on ansys.synopsys.com. The product is now branded &#x27;Ansys STK&#x27; within Synopsys/Ansys, so &#x27;From Analytical Graphics, Inc.&#x27; is out of date. The described capabilities (simulation, reports, graphs, 3D animations) are still supported.</p>

<p>https://www.agi.com/products/stk — Redirects (200) to https://ansys.synopsys.com/products/missions/ansys-stk.</p>

<p>https://ansys.synopsys.com/products/missions/ansys-stk — Title &#x27;Ansys STK | Digital Mission Engineering Software&#x27;; header and breadcrumbs show Synopsys/Ansys. &#x27;Systems Tool Kit (STK) provides a physics-based modeling environment...&#x27;; &#x27;Prepare reports and graphs... 2D and 3D renderings and animations.&#x27; The page still mentions that &#x27;AGI maintains a GitHub repository of code samples&#x27;.</p>

<p>Caveats: Did not verify current pricing or license tiers. &#x27;Free Trials&#x27; and student software links appear in site navigation, but &#x27;paid&#x27; remains broadly accurate for the commercial product.; Corporate branding may change again.</p>

</details>

<h3>Gazebo — replace</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -272,7 +272,7 @@
 
 * [42](https://software.nasa.gov/software/GSC-16720-1) - Attitude and trajectory simulation of Spacecraft (NASA)
 * [Basilisk](https://github.com/AVSLab/basilisk) - C/C++ astrodynamics and attitude control simulation (includes Python scripting).
-* [Gazebo](https://github.com/osrf/gazebo) - Robotics simulator often used for planetary rovers
+* [Gazebo](https://github.com/gazebosim/gz-sim) - Robotics simulator often used for planetary rovers
 * [LunCo](https://lunco.space) – An open-source full-cycle  Lunar Colony & space operations sim tool for engineers and enthusiasts
 * [NodalArc](https://github.com/dotchance/nodalarc) - Satellite network emulator running real Linux routing stacks (FRR with IS-IS, OSPF, BGP, and MPLS) against moving LEO topology. Each satellite is a Linux network namespace; orbital mechanics drive interface state, link latency, and ground-station handoffs.
 * [NOS3](https://github.com/nasa/nos3) - NASA Operational Simulator for Small Satellites
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed osrf/gazebo now redirects to gazebosim/gazebo-classic, which is archived. Its README says Gazebo Classic reached end-of-life in January 2025 and points to the new Gazebo (gz-sim) as the successor with migration guides. That is an officially documented successor, not a competitor. The entry name and description still apply to the successor.</p>

<p>https://github.com/osrf/gazebo — Redirects to https://github.com/gazebosim/gazebo-classic. The page shows the repository is archived; default branch gazebo11.</p>

<p>https://raw.githubusercontent.com/gazebosim/gazebo-classic/gazebo11/README.md — &#x27;A new version of Gazebo (formerly known as Ignition) is now available. Please visit https://gazebosim.org or https://github.com/gazebosim/gz-sim&#x27;; &#x27;Gazebo Classic will reach End-Of-Life in January 2025. Users are highly encouraged to migrate to the new Gazebo using our migration guides.&#x27;</p>

<p>https://github.com/gazebosim/gz-sim — Live. README: &#x27;Gazebo Sim is an open source robotics simulator... derived from Gazebo Classic... part of the Gazebo project.&#x27;</p>

<p>Caveats: Did not independently verify the &#x27;often used for planetary rovers&#x27; claim for gz-sim.; https://gazebosim.org is an equally valid project-level URL if the maintainer prefers a homepage over a repo.</p>

</details>

<h3>LunCo — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -273,7 +273,7 @@
 * [42](https://software.nasa.gov/software/GSC-16720-1) - Attitude and trajectory simulation of Spacecraft (NASA)
 * [Basilisk](https://github.com/AVSLab/basilisk) - C/C++ astrodynamics and attitude control simulation (includes Python scripting).
 * [Gazebo](https://github.com/osrf/gazebo) - Robotics simulator often used for planetary rovers
-* [LunCo](https://lunco.space) – An open-source full-cycle  Lunar Colony & space operations sim tool for engineers and enthusiasts
+* [LunCoSim](https://lunco.space/) – Open-source collaborative multiphysics co-simulator for lunar and space missions (rovers, landers, subsystems and operations) for engineers, researchers and students.
 * [NodalArc](https://github.com/dotchance/nodalarc) - Satellite network emulator running real Linux routing stacks (FRR with IS-IS, OSPF, BGP, and MPLS) against moving LEO topology. Each satellite is a Linux network namespace; orbital mechanics drive interface state, link latency, and ground-station handoffs.
 * [NOS3](https://github.com/nasa/nos3) - NASA Operational Simulator for Small Satellites
 * [OpenFLUME](https://github.com/OpenFLUME/OpenFLUME) - Open-source thermo-fluid network solver (GFSSP / SINDA-FLUINT class) for propulsion feed systems, tank pressurization and blowdown, and cryogenic chilldown, with validation reports against NASA benchmarks. Use the no-install browser UI, the TypeScript library, or the Python package (`pip install openflume`).
```

<details>
<summary>Evidence and limitations</summary>

<p>The official site now presents the product as &#x27;LunCoSim&#x27;, described as a collaborative multiphysics co-simulator for space missions. &#x27;LunCo&#x27; is the organization name in the footer. The source repo LunCoSim/lunco-sim describes it as a simulation workbench for space engineers, researchers and students. The &#x27;full-cycle Lunar Colony&#x27; framing no longer appears in official wording. Fits Simulation.</p>

<p>https://lunco.space/ — Title &#x27;LunCoSim | Multiphysics Co-Simulation for Space Missions&#x27;. &#x27;LunCoSim is an open-source space-mission simulator for system-level robotics and multiphysics studies&#x27;; ecosystem lists &#x27;LunCoSim: Open-source lunar mission simulator for collaborative engineering.&#x27; Footer: &#x27;© 2022–2026 LunCo&#x27;. Links to github.com/LunCoSim/lunco-sim.</p>

<p>https://github.com/LunCoSim/lunco-sim — Repo title &#x27;Collaborative Multiphysics Cosimulator For Space Missions&#x27;; not archived. README: &#x27;LunCoSim is an open-source simulation workbench for space engineers, researchers, and students&#x27; with rover/lander scenes, Modelica subsystem models (electrical, thermal, mechanical) and scripted operations. Apache-2.0.</p>

<p>Caveats: Did not download or run the simulator.; The double space in the original description (&#x27;full-cycle  Lunar&#x27;) is a minor typo that this update also fixes.; The original entry uses an en dash separator; keep or normalize per the list&#x27;s formatting.</p>

</details>

<h3>NodalArc — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -274,7 +274,7 @@
 * [Basilisk](https://github.com/AVSLab/basilisk) - C/C++ astrodynamics and attitude control simulation (includes Python scripting).
 * [Gazebo](https://github.com/osrf/gazebo) - Robotics simulator often used for planetary rovers
 * [LunCo](https://lunco.space) – An open-source full-cycle  Lunar Colony & space operations sim tool for engineers and enthusiasts
-* [NodalArc](https://github.com/dotchance/nodalarc) - Satellite network emulator running real Linux routing stacks (FRR with IS-IS, OSPF, BGP, and MPLS) against moving LEO topology. Each satellite is a Linux network namespace; orbital mechanics drive interface state, link latency, and ground-station handoffs.
+* [NodalArc](https://github.com/dotchance/nodalarc) - Space network emulator running real routing and DTN software (FRR with IS-IS, OSPF and SR-MPLS; ION, HDTN, uD3TN) against moving orbital topology from LEO to the Moon and Mars. Each node is a Linux container; orbital mechanics drive link state, light-time latency, and ground-station handoffs.
 * [NOS3](https://github.com/nasa/nos3) - NASA Operational Simulator for Small Satellites
 * [OpenFLUME](https://github.com/OpenFLUME/OpenFLUME) - Open-source thermo-fluid network solver (GFSSP / SINDA-FLUINT class) for propulsion feed systems, tank pressurization and blowdown, and cryogenic chilldown, with validation reports against NASA benchmarks. Use the no-install browser UI, the TypeScript library, or the Python package (`pip install openflume`).
 * [Orbital Compute](https://github.com/ShipItAndPray/orbital-compute) - Satellite constellation compute simulator with orbital mechanics, power/thermal, eclipse-aware scheduling, ISL networking, radiation, data pipeline, cost modeling, and interactive web demos.
```

<details>
<summary>Evidence and limitations</summary>

<p>Still relevant, but two concrete claims are now inaccurate. (1) BGP: the README lists &#x27;BGP routing domains&#x27; under &#x27;Where NodalArc Is Going&#x27; (not yet in the runtime). Shipped FRR support is IS-IS, OSPF, static, SR-MPLS, LDP and TE. (2) Each node is now a Linux container/session pod on Kubernetes, not just a namespace. Scope has also grown from LEO to Moon and Mars, with DTN and QUIC stacks.</p>

<p>https://github.com/dotchance/nodalarc — Resolves without redirect. Repo description: &#x27;Satellite network emulator for orbital routing, handoffs, and moving topology.&#x27;</p>

<p>https://raw.githubusercontent.com/dotchance/nodalarc/main/README.md — &#x27;Every satellite, relay, ground station and surface base is a Linux container on a Kubernetes cluster.&#x27; &#x27;FRR is the router NodalArc ships with, running IS-IS, OSPF and static routing over IPv4 and IPv6, with SR-MPLS, LDP and traffic engineering.&#x27; DTN runs ION, HDTN, uD3TN; QUIC runs picoquic. Under &#x27;Where NodalArc Is Going&#x27;: &#x27;BGP routing domains, which the grammar already defines&#x27;. Covers Earth orbit, Moon and Mars with light-time delays.</p>

<p>https://raw.githubusercontent.com/dotchance/nodalarc/main/docs/dev/architecture.md — &#x27;Session pods - one per satellite, relay, ground node&#x27;; Node Agent &#x27;moves the pod ends into namespaces&#x27;, drives carrier state and shapes links; VXLAN across Kubernetes nodes.</p>

<p>Caveats: BGP support may land soon and would need rechecking.; Did not deploy or run the emulator.</p>

</details>

<h3>space-ml-sim — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -279,7 +279,7 @@
 * [OpenFLUME](https://github.com/OpenFLUME/OpenFLUME) - Open-source thermo-fluid network solver (GFSSP / SINDA-FLUINT class) for propulsion feed systems, tank pressurization and blowdown, and cryogenic chilldown, with validation reports against NASA benchmarks. Use the no-install browser UI, the TypeScript library, or the Python package (`pip install openflume`).
 * [Orbital Compute](https://github.com/ShipItAndPray/orbital-compute) - Satellite constellation compute simulator with orbital mechanics, power/thermal, eclipse-aware scheduling, ISL networking, radiation, data pipeline, cost modeling, and interactive web demos.
 * [Space Robotics Bench](https://github.com/AndrejOrsula/space_robotics_bench) - Simulation environments and tasks for developing and validating autonomous systems in orbital and planetary robotics scenarios.
-* [space-ml-sim](https://github.com/orbital-sim-lab/space-ml-sim) - Simulate AI inference on orbital satellite constellations under space radiation. PyTorch/ONNX fault injection, TMR & distributed fault tolerance, ground station/ISL network modeling, link budget, ECSS/MIL-STD report generation, 7 hardware chip profiles. Python.
+* [space-ml-sim](https://github.com/orbital-sim-lab/space-ml-sim) - Simulate AI inference on orbital satellite constellations under space radiation. PyTorch/ONNX fault injection, TMR & distributed fault tolerance, ground station/ISL network modeling, link budget, ECSS/MIL-STD report generation, and rad-hard/COTS chip profiles. Python.
 * [Trick](https://github.com/nasa/trick) - End-to-end physics simulation package, useful for simulating missions (but requires orbital dynamics models). C, C++, with Python (SWIG) interface.
 
 ### Spacecraft Hardware
```

<details>
<summary>Evidence and limitations</summary>

<p>The entry says &#x27;7 hardware chip profiles&#x27;. The README chip table and source (ALL_CHIPS in chip_profiles.py) now define 11 profiles, so the count is outdated. All other claims are confirmed: PyTorch/ONNX fault injection, TMR, distributed inference over ISL, ground station scheduling, link budget, ECSS/MIL-STD reports, Python. The update replaces the volatile count with durable wording.</p>

<p>https://github.com/orbital-sim-lab/space-ml-sim — Resolves without redirect. Repo description: &#x27;Simulation framework for AI inference on orbital satellite constellations under space radiation&#x27;.</p>

<p>https://raw.githubusercontent.com/orbital-sim-lab/space-ml-sim/main/README.md — Chip Profiles table lists 11 chips (TERAFAB D3, Trillium v6e, Jetson AGX Orin, Versal AI Core, Zynq UltraScale+, RAD5500, NOEL-V FT, SAMRH71, GR740, XQRKU060, AURIX TC4x). The features section still names 7. ONNX import, full/selective TMR, and the v0.5 roadmap (marked current) include &#x27;Distributed inference across constellation, ISL communication delays, ground station scheduling, link budget, ECSS/MIL-STD reports&#x27;.</p>

<p>https://raw.githubusercontent.com/orbital-sim-lab/space-ml-sim/main/src/space_ml_sim/models/chip_profiles.py — ALL_CHIPS list contains 11 ChipProfile constants.</p>

<p>https://raw.githubusercontent.com/orbital-sim-lab/space-ml-sim/main/docs/API_REFERENCE.md — Documents GroundStation, ContactWindow, ISLNetwork, InferenceScheduler with ISL routing, compute_link_budget, FaultInjector, and space_ml_sim.reports.</p>

<p>Caveats: Did not run the package.; The README itself is internally inconsistent (feature list says 7 chips, table shows 11). The source code was used as the deciding evidence.</p>

</details>

<h3>FossaSat-1 — update</h3>

<p>0 proposed change(s); 1 held for unresolved questions.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The primary URL https://fossa.systems/fossasat/ returns 404. FOSSA&#x27;s site now covers its commercial FOSSASat 3U/6U/FEROX products, and /fossasat-1/ redirects to a company history page. The GitHub link Bambofy/FossaSat-1 redirects to the canonical FOSSASystems/FOSSASAT-1, which is not archived and still has the Hardware and Code directories. The update makes the canonical repo the primary URL and keeps the satellite&#x27;s history (launched December 2019).</p>

<p>https://fossa.systems/fossasat/ — HTTP 404.</p>

<p>https://fossa.systems/our-history/ — /fossasat-1/ redirects here. Says &#x27;A team of worldwide contributors developed FOSSASAT-1 as an open-source radio LoRa IoT repeater&#x27; and &#x27;December 2019 First spanish Picosatellite, FOSSA-Sat1 launched by FOSSA Systems on an Electron rocket&#x27;.</p>

<p>https://github.com/Bambofy/FossaSat-1 — Redirects to https://github.com/FOSSASystems/FOSSASAT-1. No &#x27;archived by the owner&#x27; banner. Top-level directories include Code, Hardware, FOSSA Documents, FOSSA STK, FossaCube Files.</p>

<p>https://raw.githubusercontent.com/FOSSASystems/FOSSASAT-1/master/README.md — Describes FossaSat-1, a 5x5x5 cm PocketQube with LoRa, written before launch (&#x27;Set to launch in Q3 of 2019&#x27;). Hardware in KiCad/EasyEDA.</p>

<p>https://fossa.systems/satellites/ — Current satellites page lists FOSSASat 3U/6U/FEROX commercial platforms; there is no dedicated FossaSat-1 page.</p>

<p>Caveats: The 404 could theoretically be temporary, but the redirect of /fossasat-1/ to a history page suggests a deliberate site restructure.; The repo README is pre-launch and historical; the entry describes historic hardware/software, which stays relevant.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>NASA Outgassing Db — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -285,7 +285,7 @@
 ### Spacecraft Hardware
 
 * [FossaSat-1](https://fossa.systems/fossasat/) - Hardware designs and software for the FossaSat-1 Pocketqube satellite ([GitHub](https://github.com/Bambofy/FossaSat-1))
-* [NASA Outgassing Db](https://data.nasa.gov/resource/r588-f7pr.json) - A dataset of materials intended for spacecraft use from the Goddard Space Flight Center, the Stanford Research Institute, and the Jet Propulsion Laboratory.
+* [NASA Outgassing Db](https://data.nasa.gov/dataset/outgassing-db) - A dataset of materials intended for spacecraft use from the Goddard Space Flight Center, the Stanford Research Institute, and the Jet Propulsion Laboratory.
 * [Oresat](https://github.com/oresat) - An open source cubesat developed at Oregon Small Satellite Project.
 * [ProjectInertia](https://github.com/chrismolli/ProjectInertia) - An open source hardware platform to achieve a FRAM-based radiation-tolerant microcontroller for space application. The firmware is being developed in Rust.
 * [PyCubed](https://www.notion.so/PyCubed-4cbfac7e9b684852a2ab2193bd485c4d) - An Open-Source, Radiation-Tested CubeSat Framework Programmable Entirely in Python.
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed Socrata endpoint data.nasa.gov/resource/r588-f7pr.json returns 404 because data.nasa.gov moved to a CKAN catalog. The same dataset (legacy JSON metadata still shows view id &#x27;r588-f7pr&#x27;, name &#x27;Outgassing Db&#x27;) is now at data.nasa.gov/dataset/outgassing-db, with CSV/JSON/XML/RDF downloads. Dataset notes still describe GSFC data obtained with SRI equipment under JPL contract, which matches the entry.</p>

<p>https://data.nasa.gov/resource/r588-f7pr.json — HTTP 404.</p>

<p>https://data.nasa.gov/dataset/outgassing-db — HTTP 200. CKAN package &#x27;outgassing-db&#x27; titled &#x27;Outgassing Db&#x27; (modified 2025-05-29). Notes: &#x27;This tenth compilation of outgassing data of materials intended for spacecraft use... obtained at the Goddard Space Flight Center (GSFC), utilizing equipment developed at Stanford Research Institute (SRI) under contract to the Jet Propulsion Laboratory (JPL).&#x27;</p>

<p>https://data.nasa.gov/docs/legacy/Outgassing_Db/Outgassing_Db_rows.json — 200 application/json (~2.9 MB) via S3 redirect. meta.view.id = &#x27;r588-f7pr&#x27;, name &#x27;Outgassing Db&#x27;, attributionLink https://outgassing.nasa.gov/.</p>

<p>https://outgassing.nasa.gov/ — Redirects to https://etd.gsfc.nasa.gov/capabilities/outgassing-database/, the GSFC-hosted outgassing database. This is an alternative authoritative destination.</p>

<p>Caveats: A second CKAN record &#x27;spacecraft-material-outgassing-data&#x27; exists; its page timed out and it listed no resources via the API.; The description slightly simplifies the provenance (SRI built equipment under JPL contract; testing was at GSFC). The wording is acceptable but a maintainer could tighten it.; The maintainer may prefer the GSFC outgassing database page as the URL instead.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Oresat star tracker — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -307,7 +307,7 @@
 #### Star Trackers
 
 * [MIT Tetra](https://github.com/brownj4/Tetra) and its fork, [ESA Tetra](https://github.com/esa/tetra3) - Open source star tracker which relies more extensively on hashes for faster lookups
-* [Oresat star tracker](https://github.com/oresat/oresat-star-tracker) - Open star tracker hardware [with software](https://github.com/oresat/oresat-star-tracker-software), based on UPNanosatLab's [openstartracker](https://github.com/UBNanosatLab/openstartracker) (which doesn't compile or have hardware)
+* [Oresat star tracker](https://github.com/oresat/oresat-star-tracker-hardware) - Open star tracker hardware [with software](https://github.com/oresat/oresat-star-tracker-software), originally based on UBNanosatLab's [openstartracker](https://github.com/UBNanosatLab/openstartracker) and now using UWCubeSat's [LOST](https://github.com/UWCubeSat/lost) solver
 
 ### Spacecraft Software
 
```

<details>
<summary>Evidence and limitations</summary>

<p>Two confirmed changes. (1) github.com/oresat/oresat-star-tracker now redirects to the renamed repo oresat/oresat-star-tracker-hardware. (2) oresat-star-tracker-software now solves with UW HuskySat&#x27;s LOST, not openstartracker: the README says so, LOST is the only git submodule, and CMake builds &#x27;oresat_lost_core&#x27;. The hardware README says the software was originally based on OpenStarTracker. The parenthetical claim that openstartracker &#x27;doesn&#x27;t compile or have hardware&#x27; is an unsupported editorial statement, since its README gives Ubuntu and Docker build instructions. The repo&#x27;s GitHub description still says &#x27;openstartracker-based&#x27;, but the code and README show LOST.</p>

<p>https://github.com/oresat/oresat-star-tracker — Redirects to https://github.com/oresat/oresat-star-tracker-hardware (&#x27;Hardware for OreSat&#x27;s Star Tracker&#x27;).</p>

<p>https://raw.githubusercontent.com/oresat/oresat-star-tracker-hardware/master/README.md — Custom Octavo OSD3358 card with AR0130 camera for the OreSat bus. The software, &#x27;based on OpenStarTracker&#x27;, moved to oresat-star-tracker-software on 2/21/2020.</p>

<p>https://raw.githubusercontent.com/oresat/oresat-star-tracker-software/master/README.md — &#x27;Algorithmic solving implemented with University of Washington HuskySat&#x27;s LOST star tracker program.&#x27; Built on the OLAF framework.</p>

<p>https://raw.githubusercontent.com/oresat/oresat-star-tracker-software/master/.gitmodules — The only submodule is third_party/lost → https://github.com/UWCubeSat/lost.git. CMakeLists project name: oresat_lost_core.</p>

<p>https://raw.githubusercontent.com/UBNanosatLab/openstartracker/master/README.md — Gives apt build instructions, a unit-test script and a Dockerfile-based build. Nothing in it confirms that it &#x27;doesn&#x27;t compile&#x27;.</p>

<p>Caveats: UWCubeSat/lost itself was not inspected beyond the submodule reference.; I did not attempt to compile openstartracker; the removal of the &#x27;doesn&#x27;t compile&#x27; claim rests on it being unverified, not disproven.</p>

</details>

<h3>JPL F Prime — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -314,7 +314,7 @@
 * [cFS Basecamp](https://github.com/cfs-tools/cfs-basecamp) - Provides a lightweight environment to help you learn NASA’s cFS and create app-based solutions for your projects. The built-in hands-on tutorials shorten the path to productivity.
 * [Core Flight System](https://github.com/nasa/cfs) - NASA portable and extendable flight software framework with extensive flight heritage and a growing suite of applications and platform ports
 * [FossaSat-1](https://fossa.systems/fossasat/) - Hardware designs and software for the FossaSat-1 Pocketqube satellite ([GitHub](https://github.com/Bambofy/FossaSat-1))
-* [JPL F Prime](https://github.com/nasa/fprime) - F Prime (FÊ¹) is a component-driven framework that enables rapid development and deployment of spaceflight and other embedded software applications, originally developed at the Jet Propulsion Laboratory.
+* [JPL F Prime](https://github.com/nasa/fprime) - F Prime (F´) is a component-driven framework that enables rapid development and deployment of spaceflight and other embedded software applications, originally developed at the Jet Propulsion Laboratory.
 * [KubOS](https://www.kubos.com/kubos/) - An open-source flight software framework for satellites
 * [LibreCube](https://librecube.org/) - Open source space and Earth exploration. Defining a generic architecture of system of systems that have standardized interfaces makes it possible to combine and reuse elements for various applications
 * [Linux4Space](https://linux4space.org/) - Open source Yocto based Linux distribution suitable for space applications
```

<details>
<summary>Evidence and limitations</summary>

<p>The project and description are accurate and match the upstream README. However, the catalog text contains mojibake: the bytes for &#x27;FÊ¹&#x27; (C3 8A C2 B9) appear where upstream writes &#x27;F´&#x27; (F Prime). This is a confirmed text-encoding error in the description.</p>

<p>https://raw.githubusercontent.com/nasa/fprime/devel/README.md — &#x27;F´ (F Prime) is a component-driven framework that enables rapid development and deployment of spaceflight and other embedded software applications. Originally developed at the Jet Propulsion Laboratory…&#x27;</p>

<p>https://github.com/nasa/fprime — Returns 200 with no redirect. Description: &#x27;F´ - A flight software and embedded systems framework&#x27;.</p>

<p>Caveats: The encoding error was confirmed with od on README.md line 317 of the pinned checkout.</p>

</details>

<h3>FossaSat-1 — update</h3>

<p>0 proposed change(s); 1 held for unresolved questions.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The primary URL fossa.systems/fossasat/ now returns 404. FOSSA Systems&#x27; site is now a commercial satellite IoT company page; its history page still describes FOSSASAT-1 as an open-source LoRa IoT repeater. The GitHub link github.com/Bambofy/FossaSat-1 redirects to the canonical github.com/FOSSASystems/FOSSASAT-1. That repo contains Code, Hardware and FOSSA Documents directories, plus a README describing the PocketQube satellite. The repo should become the primary URL.</p>

<p>https://fossa.systems/fossasat/ — Returns HTTP 404. A Wayback capture exists from 2019-10-14.</p>

<p>https://github.com/Bambofy/FossaSat-1 — Redirects to https://github.com/FOSSASystems/FOSSASAT-1.</p>

<p>https://raw.githubusercontent.com/FOSSASystems/FOSSASAT-1/master/README.md — Describes FossaSat-1, Spain&#x27;s first picosatellite, as a 5x5x5 cm pocketqube with LoRa. Repo directories include Code, Hardware, FOSSA Documents and FossaCube Files.</p>

<p>https://fossa.systems/our-history/ — &#x27;A team of worldwide contributors developed FOSSASAT-1 as an open-source radio LoRa IoT repeater.&#x27;</p>

<p>Caveats: The README still uses pre-launch wording (&#x27;Set to launch in Q3 of 2019&#x27;). This is a historic resource and is not grounds for removal.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>SUCHAI FS — replace</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -322,7 +322,7 @@
 * [OpenSatKit](https://github.com/OpenSatKit/OpenSatKit) - A complete [Core Flight System](https://github.com/nasa/cfs) training and application development environment that includes [COSMOS](https://cosmosrb.com/) and [42](https://software.nasa.gov/software/GSC-16720-1)
 * [SatCat5](https://github.com/the-aerospace-corporation/satcat5) - A mixed-media Ethernet switch for connecting smallsat payloads
 * [Space ROS](https://github.com/space-ros/space-ros) - ROS 2-based framework for space robotics software, testing, and interoperability.
-* [SUCHAI FS](https://gitlab.com/spel-uchile/suchai-flight-software) - The SUCHAI Flight Software is a FOSS framework for developing flight and ground software for nanosatellites. It has been used in the SUCHAI-1, SUCHAI-2, SUCHAI-3 and PlantSat CubeSat missions.
+* [SUCHAI FS](https://gitlab.com/spel-uchile/flight-software/suchai-flight-software-v2) - The SUCHAI Flight Software is a FOSS framework for developing flight and ground software for nanosatellites. It has been used in the SUCHAI-1, SUCHAI-2, SUCHAI-3, PlantSat and SUCHAI-4 CubeSat missions.
 * [SYNOPSIS](https://github.com/NASA-AMMOS/synopsis) - NASA-AMMOS framework for onboard data-product generation and downlink prioritization, including autonomous science products and cFS integration.
 * [UPSat](https://upsat.gr/) - Open source satellite software and hardware
 
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed GitLab project&#x27;s official description says &#x27;This repository is no longer maintained. Please check the new version: https://gitlab.com/spel-uchile/flight-software/suchai-flight-software-v2&#x27;. The README on its default branch says the same. The v2 project is public, active (last activity 2026-10-29) and run by the same SPEL group. It describes itself as the evolution of the same framework, with flight heritage on SUCHAI, SUCHAI-2, SUCHAI-3, PlantSat and SUCHAI-4. That is an officially documented successor.</p>

<p>https://gitlab.com/api/v4/projects/spel-uchile%2Fsuchai-flight-software — Project description: &#x27;Flight Software developed for SUCHAI space program nanosatellites. This repository is no longer maintained. Please check the new version: https://gitlab.com/spel-uchile/flight-software/suchai-flight-software-v2&#x27;. The default branch is feature/framework.</p>

<p>https://gitlab.com/spel-uchile/suchai-flight-software/-/raw/feature/framework/README.md — The README header reads &#x27;:new: Check the new version SUCHAI Flight Software v2 ... This repository is no longer maintained.&#x27;</p>

<p>https://gitlab.com/spel-uchile/flight-software/suchai-flight-software-v2 — The project is public with last activity on 2026-10-29. Its description reads &#x27;Flight Software developed for SUCHAI space program nanosatellites. This is the new version of the flight software.&#x27; The README calls it an evolution of the framework, links back to the previous repo, says it &#x27;Can be used as Flight Software, Ground Station Software&#x27;, and lists &#x27;Flight inheritance: SUCHAI (2017), SUCHAI 2 (2022), SUCHAI 3 (2022), PlantSat (2022), and SUCHAI 4 (2026).&#x27;</p>

<p>Caveats: The original repository is still reachable and is not formally archived. It is labeled unmaintained, and it still has historic value as the code behind SUCHAI-1.; The SUCHAI-4 heritage claim comes from the project&#x27;s own README.</p>

</details>

<h3>AstriaGraph — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -332,7 +332,7 @@
 
 ### Tracking & Orbit Determination
 
-* [AstriaGraph](http://astria.tacc.utexas.edu/AstriaGraph/) - Open source data and visualization of all known objects in Earth’s orbit
+* [AstriaGraph](http://astria.tacc.utexas.edu/AstriaGraph/) - Visualization and data on Earth-orbiting objects compiled from multiple public and private catalogs (hosted dataset last refreshed in March 2024)
 * [Astro::Coord::ECI::TLE](https://metacpan.org/pod/Astro::Coord::ECI::TLE) - Perl implementation of NORAD progation models
 * [azmth](https://azmth.space/) - A web-based, real-time 3D satellite tracker that propagates ~15,000 active satellites via SGP4 in the browser, with pass predictions for any location, orbital data, and filtering by country and orbit type.
 * [Gpredict](http://gpredict.oz9aec.net/) - Open source, real-time satellite tracking and orbit prediction application.
```

<details>
<summary>Evidence and limitations</summary>

<p>The AstriaGraph page is reachable and still renders a Cesium globe of Earth-orbiting objects from several catalogs. However, its intact-object dataset (OD_stats/intactData.js) was last modified 2024-03-08, and the newest element epoch across its 43,429 records is 2024-03-08. So &#x27;all known objects&#x27; is no longer accurate as a current claim. The page&#x27;s own notice restricts data reuse to non-commercial use without permission, which does not support the unqualified &#x27;open source data&#x27; wording. I recommend a description that keeps the resource but drops the currency and open-data claims.</p>

<p>http://astria.tacc.utexas.edu/AstriaGraph/ — Returns HTTP 200. The page shows filters for data source, country, orbit regime and debris. Its notice says: &#x27;AstriaGraph is a public-private partnership in which the partners have agreed to limit commercial uses by third parties. You can copy, modify, distribute, or display AstriaGraph information for non-commercial uses without permission.&#x27; Listed sources include JSC Vimpel, Planet, SeeSat-L, SpaceX and UCS.</p>

<p>http://astria.tacc.utexas.edu/AstriaGraph/OD_stats/intactData.js — The Last-Modified header is Fri, 08 Mar 2024. Across 43,429 epoch fields, the latest epoch is 2024-03-08T05:16:48Z.</p>

<p>http://astria.tacc.utexas.edu/AstriaGraph/main.js — The client code is GPL-licensed. It loads the static OD_stats data and propagates from each record&#x27;s epoch. I found no live data feed URL.</p>

<p>Caveats: I did not check whether ASTRIA publishes a refreshed dataset or a successor elsewhere.; I checked only the intact-object data file, not the debris data loaded on demand.</p>

</details>

<h3>azmth — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -334,7 +334,7 @@
 
 * [AstriaGraph](http://astria.tacc.utexas.edu/AstriaGraph/) - Open source data and visualization of all known objects in Earth’s orbit
 * [Astro::Coord::ECI::TLE](https://metacpan.org/pod/Astro::Coord::ECI::TLE) - Perl implementation of NORAD progation models
-* [azmth](https://azmth.space/) - A web-based, real-time 3D satellite tracker that propagates ~15,000 active satellites via SGP4 in the browser, with pass predictions for any location, orbital data, and filtering by country and orbit type.
+* [azmth](https://azmth.space/) - A web-based, real-time 3D satellite tracker that propagates every active satellite via SGP4 in the browser, with pass predictions for any location, orbital data, and filtering by country and orbit type.
 * [Gpredict](http://gpredict.oz9aec.net/) - Open source, real-time satellite tracking and orbit prediction application.
 * [ISSview](https://issview.com) - Simulated live view from the International Space Station, propagating its position via SGP4 and rendering the ground below in real time with live weather, city lights, and aurora.
 * [jspredict](https://github.com/nsat/jspredict) - A Javascript port of the popular predict satellite tracking library.
```

<details>
<summary>Evidence and limitations</summary>

<p>azmth.space is live. Its FAQ confirms positions are computed in the browser with SGP4/SDP4 from CelesTrak TLEs, with pass predictions for any location, orbital element data, and country attribution. But the site now advertises &#x27;16,900+&#x27; active satellites, not &#x27;~15,000&#x27;. I recommend replacing the volatile count with durable wording.</p>

<p>https://azmth.space/ — Meta description: &#x27;Every active satellite (16,900+) live on a free 3D globe.&#x27; FAQ: &#x27;Positions are computed in your browser with the SGP4/SDP4 orbital propagation model.&#x27; Feature list includes &#x27;Pass predictions for any location&#x27; and &#x27;Orbital element data&#x27;. Data comes from CelesTrak and refreshes every 2 hours.</p>

<p>https://azmth.space/about — The About page says CelesTrak SATCAT is used for operator and country attribution. The site&#x27;s stats page breaks the count down by country, network and orbit.</p>

<p>Caveats: The interactive filtering UI is client-rendered. I could not directly confirm filtering by country and orbit type, though country and orbit attribution data are present. The proposed text keeps that claim unchanged.</p>

</details>

<h3>Orb Calc — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -339,7 +339,7 @@
 * [ISSview](https://issview.com) - Simulated live view from the International Space Station, propagating its position via SGP4 and rendering the ground below in real time with live weather, city lights, and aurora.
 * [jspredict](https://github.com/nsat/jspredict) - A Javascript port of the popular predict satellite tracking library.
 * [KeepTrack](https://keeptrack.space) - Open-source TypeScript and WebGl app for visualizing satellites, radars, telescopes, missiles, and breakups.
-* [Orb Calc](https://github.com/wselwood/orbcalc) - Generate positions of objects from orbital parameters.
+* [Orb Calc](https://github.com/emilyselwood/orbcalc) - Generate positions of objects from orbital parameters.
 * [Orbinauts](https://orbinauts.com) - Live satellite tracking map with pass predictions for any location and naked-eye pass times for cities worldwide, a schedule of upcoming rocket launches with an orbit sketch that draws where a launch flies over in its first orbits, and Space-Track's close-approach reports. Its data is also available through a REST API with a free, key-less tier ([OpenAPI docs](https://api.orbinauts.com/v1/docs)).
 * [Orbit Determination Tool Kit (ODTK)](https://www.agi.com/products/odtk) - Processes traditional and non-traditional measurements using a sequential filter & matched smoother to generate orbits with realistic covariance (paid). From Analytical Graphics, Inc.
 * [Orbital Object Toolkit](https://github.com/thkruz/ootk) - TypeScript port of python-sgp4 plus additional features for working with TLEs, satellites, and sensors.
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed GitHub URL permanently redirects (301) from wselwood/orbcalc to emilyselwood/orbcalc, so the canonical owner has changed. The README still describes a Go library to &#x27;work out the position in space of an object after some time given the normal orbital elements&#x27;, so the description stays accurate. Only the URL needs updating.</p>

<p>https://github.com/wselwood/orbcalc — HTTP 301, Location: https://github.com/emilyselwood/orbcalc.</p>

<p>https://github.com/emilyselwood/orbcalc — Returns HTTP 200. The description reads &#x27;Orbital mechanics on minor planets using golang&#x27;.</p>

<p>https://raw.githubusercontent.com/emilyselwood/orbcalc/master/README.md — &#x27;This project is designed to alow you to work out the position in space of an object after some time given the normal orbital elements. The main usecase is to be able to plot the locations of asteroids over time.&#x27;</p>

<p>Caveats: The README calls the project &#x27;very basic and work in progress&#x27;. That alone is not a reason to remove it.</p>

</details>

<h3>Orbit Determination Tool Kit (ODTK) — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -341,7 +341,7 @@
 * [KeepTrack](https://keeptrack.space) - Open-source TypeScript and WebGl app for visualizing satellites, radars, telescopes, missiles, and breakups.
 * [Orb Calc](https://github.com/wselwood/orbcalc) - Generate positions of objects from orbital parameters.
 * [Orbinauts](https://orbinauts.com) - Live satellite tracking map with pass predictions for any location and naked-eye pass times for cities worldwide, a schedule of upcoming rocket launches with an orbit sketch that draws where a launch flies over in its first orbits, and Space-Track's close-approach reports. Its data is also available through a REST API with a free, key-less tier ([OpenAPI docs](https://api.orbinauts.com/v1/docs)).
-* [Orbit Determination Tool Kit (ODTK)](https://www.agi.com/products/odtk) - Processes traditional and non-traditional measurements using a sequential filter & matched smoother to generate orbits with realistic covariance (paid). From Analytical Graphics, Inc.
+* [Orbit Determination Tool Kit (ODTK)](https://ansys.synopsys.com/products/missions/ansys-odtk) - Processes traditional and non-traditional measurements using a sequential filter & matched smoother to generate orbits with realistic covariance (paid). From Ansys (formerly Analytical Graphics, Inc.).
 * [Orbital Object Toolkit](https://github.com/thkruz/ootk) - TypeScript port of python-sgp4 plus additional features for working with TLEs, satellites, and sensors.
 * [Orbital Radar](https://orbitalradar.com) - A real-time, browser-based satellite tracking and space situational awareness platform. Visualises every catalogued object in Earth orbit on an interactive 3D globe using TLE data, with constellation filtering, live re-entry forecasting, conjunction screening, and a space encyclopaedia.
 * [OrbitalWiki](https://orbitalwiki.com) - Public satellite catalog fusing CelesTrak, GCAT, and Wikidata into one source-cited dataset of ~16,000 objects, with a free REST API.
```

<details>
<summary>Evidence and limitations</summary>

<p>The listed AGI URL redirects (302) through ansys.com to https://ansys.synopsys.com/products/missions/ansys-odtk. The product is now branded &#x27;Ansys Orbit Determination Tool Kit&#x27; (AGI was acquired by Ansys, and the page is now hosted on Synopsys). The functional claims are still supported: traditional and non-traditional measurements, an optimal sequential filter and matched smoother, and realistic covariance. But &#x27;From Analytical Graphics, Inc.&#x27; and the agi.com URL are outdated.</p>

<p>https://www.agi.com/products/odtk — HTTP 302 to https://www.ansys.com/products/missions/ansys-odtk, then to https://ansys.synopsys.com/products/missions/ansys-odtk, which returns 200.</p>

<p>https://ansys.synopsys.com/products/missions/ansys-odtk — Title: &#x27;Ansys Orbit Determination Tool Kit | Orbit Simulation Software&#x27;. &#x27;With Ansys ODTK, you can process a wide variety of traditional and non-traditional measurements to generate orbits with realistic covariance.&#x27; &#x27;ODTK&#x27;s state-of-the-art optimal sequential filter and matched smoother&#x27;. Publisher listed as Ansys, copyright 2026.</p>

<p>Caveats: Corporate hosting may keep changing (ansys.com now redirects to ansys.synopsys.com). I chose the vendor-neutral wording &#x27;From Ansys (formerly Analytical Graphics, Inc.)&#x27; for durability.; I did not verify paid status on a pricing page. ODTK is a commercial product with no free tier advertised on the page.</p>

</details>

<h3>OrbitalWiki — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -344,7 +344,7 @@
 * [Orbit Determination Tool Kit (ODTK)](https://www.agi.com/products/odtk) - Processes traditional and non-traditional measurements using a sequential filter & matched smoother to generate orbits with realistic covariance (paid). From Analytical Graphics, Inc.
 * [Orbital Object Toolkit](https://github.com/thkruz/ootk) - TypeScript port of python-sgp4 plus additional features for working with TLEs, satellites, and sensors.
 * [Orbital Radar](https://orbitalradar.com) - A real-time, browser-based satellite tracking and space situational awareness platform. Visualises every catalogued object in Earth orbit on an interactive 3D globe using TLE data, with constellation filtering, live re-entry forecasting, conjunction screening, and a space encyclopaedia.
-* [OrbitalWiki](https://orbitalwiki.com) - Public satellite catalog fusing CelesTrak, GCAT, and Wikidata into one source-cited dataset of ~16,000 objects, with a free REST API.
+* [OrbitalWiki](https://www.orbitalwiki.com) - Public satellite catalog fusing CelesTrak, GCAT, and Wikidata into one source-cited dataset of every tracked object, with a free REST API.
 * [OrbitNight](https://orbitnight.com) - Free browser-based satellite tracker: a live map of every catalogued object propagated with SGP4 in the browser, naked-eye pass predictions and alerts for any city, a sky radar with Doppler correction and Web Serial rotator/radio control for amateur radio, plus launch, re-entry and Starlink-train pages.
 * [Orekit](https://www.orekit.org) - An accurate and efficient core layer for space flight dynamics applications written in Java.
 * [perturb](https://github.com/gunvirranu/perturb) - A modern C++ library for SGP4 orbit propagation of TLEs
```

<details>
<summary>Evidence and limitations</summary>

<p>OrbitalWiki is live at its canonical host www.orbitalwiki.com (308 from the apex). Cloudflare returns 403 to non-browser user agents, but it loads with a browser user agent. It still merges CelesTrak, GCAT and Wikidata with per-field sourcing and offers a free read-only API. But it now reports 17,338 objects rather than ~16,000. I recommend replacing the volatile count with durable wording.</p>

<p>https://orbitalwiki.com — HTTP 308 to https://www.orbitalwiki.com/ (Cloudflare).</p>

<p>https://www.orbitalwiki.com/ — Meta description: &#x27;Search 17,338 tracked satellites with the source of every field shown... Free read-only API for elements, operators and NORAD/COSPAR IDs.&#x27; Body: &#x27;Orbits come from CelesTrak, launch history from GCAT, extra detail from Wikidata, radio from SatNOGS... merges what each source knows into one record for each of 17,338 objects&#x27;. Navigation includes Developers, Pricing and /license.</p>

<p>Caveats: The site also uses SatNOGS as a fourth source. That is an expansion, not a correction.; A pricing page exists, so paid tiers may exist alongside the free API. I did not read it.</p>

</details>

<h3>UPSat — update</h3>

```diff
--- a/README.md
+++ b/README.md
@@ -324,7 +324,7 @@
 * [Space ROS](https://github.com/space-ros/space-ros) - ROS 2-based framework for space robotics software, testing, and interoperability.
 * [SUCHAI FS](https://gitlab.com/spel-uchile/suchai-flight-software) - The SUCHAI Flight Software is a FOSS framework for developing flight and ground software for nanosatellites. It has been used in the SUCHAI-1, SUCHAI-2, SUCHAI-3 and PlantSat CubeSat missions.
 * [SYNOPSIS](https://github.com/NASA-AMMOS/synopsis) - NASA-AMMOS framework for onboard data-product generation and downlink prioritization, including autonomous science products and cFS integration.
-* [UPSat](https://upsat.gr/) - Open source satellite software and hardware
+* [UPSat](https://gitlab.com/librespacefoundation/upsat) - Open source satellite software and hardware
 
 #### Legacy
 
```

<details>
<summary>Evidence and limitations</summary>

<p>https://upsat.gr/ fails today (proxy 502 for both http and https). The most recent Wayback capture, from 2025-11-20, shows a parked domain (&#x27;upsat.gr Buy this domain&#x27;), so the official site is gone. The UPSat hardware and software are still published by Libre Space Foundation in the public GitLab group librespacefoundation/upsat, described as &#x27;The first open source satellite&#x27;. It holds OBC, EPS, COMMS and ADCS hardware and software repos. The description is still accurate; only the URL should move.</p>

<p>https://upsat.gr/ — The request failed with a 502 Bad Gateway from the egress proxy for both https and http (likely DNS or connection failure).</p>

<p>http://web.archive.org/web/20251120120124/https://upsat.gr/ — The 2025-11-20 snapshot shows only &#x27;upsat.gr Buy this domain. We&#x27;re getting things ready&#x27;. The domain is parked and no longer the UPSat project site.</p>

<p>https://gitlab.com/api/v4/groups/librespacefoundation%2Fupsat — Group librespacefoundation/upsat is public, with description &#x27;The first open source satellite&#x27; and web URL https://gitlab.com/groups/librespacefoundation/upsat.</p>

<p>https://gitlab.com/api/v4/groups/librespacefoundation%2Fupsat/projects?per_page=50 — The group contains upsat-obc-software, upsat-obc-hardware, upsat-eps-software, upsat-eps-hardware, upsat-comms-software, upsat-comms-hardware, upsat-adcs-software, upsat-adcs-hardware, upsat-structural and others. None are archived. Most last activity is 2017, with upsat-org in 2020.</p>

<p>Caveats: The UPSat repositories are historic (mostly last active in 2017). That is expected for a completed 2016 mission and is not a reason to remove the entry.; I could not reach upsat.gr directly today, so its current state relies on the 2025 Wayback snapshot.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Predict — update</h3>

<p>0 proposed change(s); 1 held for unresolved questions.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The Predict repository README still describes it as a partial PHP port of Gpredict supporting the SGP4 and SDP4 models, so the description is accurate. However, the inline Gpredict link http://gpredict.oz9aec.net/ now redirects to https://oz9aec.dk/gpredict/, the official Gpredict page maintained by Alexandru Csete (updated June 2026). Recommend updating only that inline link; the repository URL is unchanged.</p>

<p>https://raw.githubusercontent.com/shupp/Predict/master/README.md — &#x27;Predict is a partial PHP port of the Gpredict program that allows real-time tracking and orbit prediction of satellites from two line element sets. It supports the SGP4 and SDP4 models&#x27;; &#x27;Only the prediction routines have been ported.&#x27;</p>

<p>https://github.com/shupp/Predict — Resolves (HTTP 200) to the same owner/name; no redirect.</p>

<p>https://oz9aec.dk/gpredict/ — http://gpredict.oz9aec.net/ redirects here. The page is &#x27;Gpredict: Free, Real-Time Satellite Tracking and Orbit Prediction Software&#x27;, updated Thursday, 18 Jun 2026 by Alexandru Csete.</p>

<p>Caveats: Repository activity could not be checked via the GitHub API (rate limited); low activity would not affect relevance.; Did not run the PHP code.</p>

</details>

## Uncertain findings

<h3>ANISE — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>README calls it an alternative and lists unsupported kernel types, while Cargo metadata still calls it a replacement. The catalog never claims complete or drop-in compatibility. This does not establish a factual error requiring replacement→alternative; treat wording as optional and exclude it from confirmed changes.</p>

<p>https://github.com/nyx-space/anise — Canonical repo nyx-space/anise, not archived, pushed 2026-11-08. GitHub description: &#x27;A thread-safe alternative to NASA SPICE toolkit…&#x27;.</p>

<p>https://raw.githubusercontent.com/nyx-space/anise/master/README.md — &#x27;ANISE is a fresh, Rust-powered alternative to the NAIF SPICE toolkit&#x27;. The supported-kernel table shows BSP/SPK and BPC supported, TK/LSK/GM after transformation, and CK, SCLK, DSK and IK/EK &#x27;Yet to be supported&#x27;.</p>

<p>https://raw.githubusercontent.com/nyx-space/anise/master/Cargo.toml — Workspace members are anise, anise-cli, anise-gui, anise-py, anise/fuzz and anise-cpp, version 1.0.0-beta. The description reads: &#x27;ANISE provides a toolkit and files for Attitude, Navigation, Instrument, Spacecraft, and Ephemeris data. It&#x27;s a modern replacement of NAIF SPICE file.&#x27;</p>

<p>Blocking questions: README calls it an alternative and lists unsupported kernel types, while Cargo metadata still calls it a replacement. The catalog never claims complete or drop-in compatibility. This does not establish a factual error requiring replacement→alternative; treat wording as optional and exclude it from confirmed changes.</p>

<p>Caveats: The Cargo.toml description still uses the word &#x27;replacement&#x27;, so the project&#x27;s own wording is mixed. The README and GitHub description are the newer statements.; The entry sits under Visualization although ANISE is mainly a toolkit; anise-gui exists. Moving it to another section is optional and up to the maintainer.</p>

<p>Independent source check: README calls it an alternative and lists unsupported kernel types, while Cargo metadata still calls it a replacement. The catalog never claims complete or drop-in compatibility. This does not establish a factual error requiring replacement→alternative; treat wording as optional and exclude it from confirmed changes.</p>

<p>https://github.com/nyx-space/anise/blob/master/README.md — Alternative terminology and kernel limitations verified; bloba2ed18d5ae4e4e6c0f1f0ff2d51f185cb355e79a.</p>

<p>https://github.com/nyx-space/anise/blob/master/Cargo.toml — Project metadata retains replacement terminology; blob5bb466dc7584e1670c81b99995b5a2015559e14c.</p>

</details>

<h3>Orbit Simulator — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>Direct source failed in this audit. Raw model already holds the rename because alternate naming is unresolved and another Gravity Simulator exists. Retain hold; not an outreach example.</p>

<p>http://www.orbitsimulator.com/gravity/articles/what.html — HTTP 200. Headings &#x27;Gravity Simulator&#x27; and &#x27;What is Gravity Simulator?&#x27;. Contains the quoted sentence. It says there is a Windows-only original version and a newer version that runs in the web browser.</p>

<p>Blocking questions: Direct source failed in this audit. Raw model already holds the rename because alternate naming is unresolved and another Gravity Simulator exists. Retain hold; not an outreach example.</p>

<p>Caveats: There is an unrelated &#x27;Gravity Simulator&#x27; (gravitysimulator.org, Harmony of the Spheres, entry 74). Consider whether the rename could confuse readers.; The site is http-only; https wasn&#x27;t tested.</p>

<p>Independent source check: Direct source failed in this audit. Raw model already holds the rename because alternate naming is unresolved and another Gravity Simulator exists. Retain hold; not an outreach example.</p>

<p>http://www.orbitsimulator.com/gravity/articles/what.html — Direct web-tool read failed; no independent name verification.</p>

</details>

<h3>obdh.space — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>obdh.space could not be read. curl timed out on https, the http redirect to www.obdh.space failed through the proxy, and WebFetch reported a DNS failure for www.obdh.space. Search-engine listings show live-looking pages (Explore Space Data, Space Launches Database, search), but no page content was read, so current availability and the daily-update claim are unconfirmed.</p>

<p>Blocking questions: The current content of obdh.space could not be read, so the description cannot be confirmed or corrected.</p>

<p>Caveats: The access failures may be caused by the local network or proxy; they are not proof the site is dead.; Search-engine snippets suggest the site offers satellite and launch databases, charts and daily updates, but these were not verified at the source.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>SIMBAD Astronomical Database — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>The listed simbad.u-strasbg.fr host failed through the proxy (502). The CDS host simbad.cds.unistra.fr/simbad/ returned 404. The simbad.cds.unistra.fr root shows a notice of a cybersecurity incident affecting the main CDS servers in Strasbourg and points users to mirrors at CfA Harvard and IDIA. SIMBAD remains relevant. Whether the legacy u-strasbg.fr URL still redirects to the canonical cds.unistra.fr path cannot be determined during the outage.</p>

<p>https://simbad.cds.unistra.fr/ — An incident notice directs users to the mirrors https://simbad.cfa.harvard.edu/simbad/ (data current through 14 October 2026) and https://simbad.idia.ac.za/, and explains how to reconfigure astroquery.</p>

<p>Blocking questions: The CDS main servers are down after an incident. Neither the canonical post-restoration URL (likely https://simbad.cds.unistra.fr/simbad/) nor the status of the legacy u-strasbg.fr redirect can be verified until service is restored.</p>

<p>Caveats: This is a temporary outage. It is not a reason to remove the entry or to switch to a mirror.; The purpose statement in the description was not re-read from the main server.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>ESA&#x27;s GEOSS Portal — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>geoportal.org did not respond: http returned 502 through the proxy, and https did not connect. An archived copy shows the GEOSS Portal still served on 22 December 2025. re3data marks the repository &#x27;Offline: 2025&#x27;. A web search summary reports a geoportal.org notice that GEO EXCOM dismissed the portal, with access ending 20 December 2025, but I could not read that notice directly. The archived page is a JavaScript shell without the text. GEO&#x27;s current home page promotes the GEO Knowledge Hub, but I found no official statement naming it the successor.</p>

<p>http://www.geoportal.org/ — http returned 502, and the https request failed to connect (curl exit 7 / 000).</p>

<p>https://www.re3data.org/repository/r3d100011734 — &#x27;Caution: This entry is annotated as &quot;Offline: 2025&quot;&#x27; and &#x27;This repository is offline&#x27;. Lists ESA as the institution with technical responsibility.</p>

<p>http://web.archive.org/web/20251222101011/https://www.geoportal.org/ — The latest archived capture (22 Dec 2025) is titled &#x27;GEOSS Portal&#x27;. It is a JavaScript shell, and no shutdown text could be extracted.</p>

<p>https://earthobservations.org/ — The GEO site references the GEO Knowledge Hub as its open-data infrastructure. No GEOSS Portal successor statement was found in the fetched page.</p>

<p>Blocking questions: The official GEO/ESA discontinuation notice (reportedly dated around December 2025) was not read directly, so removal lacks first-hand official evidence.; No officially documented successor service was found, so a replace is not supported.</p>

<p>Caveats: The connection failure could be partly due to the sandbox proxy. A maintainer should recheck from a normal network.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Yale&#x27;s Center for Earth Observation — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>The listed page is gone. yceo.yale.edu/image-sources redirects to geospatial.yale.edu/image-sources, which returns 404. The Yale Center for Earth Observation appears to have been folded into the Yale Center for Geospatial Solutions (YCGS), which has an Earth Observation Lab. YCGS&#x27;s current Data &amp; Tools page mainly covers Yale-licensed resources (e.g., CONNECTExplorer, PolicyMap) and is not shown to be an equivalent public directory of imagery sources. No documented replacement was found, so neither an update nor a removal is supported yet.</p>

<p>https://yceo.yale.edu/image-sources — Redirects to https://geospatial.yale.edu/image-sources, which returns HTTP 404.</p>

<p>https://geospatial.yale.edu/ — Yale Center for Geospatial Solutions home page with an &#x27;Earth Observation Lab&#x27; (&#x27;a research and teaching space for studying Earth with satellite imagery&#x27;) and Support &amp; Services &gt; Data &amp; Tools.</p>

<p>https://geospatial.yale.edu/data-tools — Data &amp; Tools page lists Yale-access datasets and software (MyApps GIS, CONNECTExplorer, PolicyMap); it was not confirmed to contain the former public imagery-source directory.</p>

<p>Blocking questions: Whether YCGS officially maintains a successor public imagery/data source directory is unknown.; Whether the 404 is permanent or a site-migration gap is unknown.</p>

<p>Caveats: Did not check the Wayback Machine for the former page content or its last valid date.; Only part of the Data &amp; Tools page was read.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>NASA Exoplanet Archive — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>Both the listed data.html page and the archive home page currently return HTTP 503 with an official &#x27;temporarily offline for maintenance&#x27; notice. This is a temporary outage, not evidence of retirement. The specific page&#x27;s content could not be verified, so it needs a recheck. Relevance of the NASA Exoplanet Archive itself is not in question.</p>

<p>https://exoplanetarchive.ipac.caltech.edu/docs/data.html — HTTP 503: &#x27;NASA ExoPlanet Archive | Under Maintenance — The NASA Exoplanet Archive is temporarily offline for maintenance. The services will be back online as soon as possible.&#x27;</p>

<p>https://exoplanetarchive.ipac.caltech.edu/ — Same maintenance notice on the archive home page.</p>

<p>Blocking questions: The content and continued existence of /docs/data.html could not be verified while the archive is offline for maintenance.</p>

<p>Caveats: No archived copy of data.html was consulted to confirm the page still exists at that path.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Radiation Test Database — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>CERN RADWG still runs a radiation test database of components. CERN presentations through 2025 cite radwg.web.cern.ch, with 500+ reports. However, the listed URL (and the radwg.web.cern.ch root) now redirects to the CERN SSO login page. I could not determine whether the database is still publicly readable or now limited to CERN accounts. Relevance to spacecraft hardware is not in doubt.</p>

<p>http://radwg.web.cern.ch/content/radiation-test-database — Redirects to auth.cern.ch, the OpenID Connect sign-in page for client webframeworks-app-catalogue-radwg-wp. No database content was visible.</p>

<p>https://indico.cern.ch/event/1383997/contributions/5817837/attachments/2806162/4896544/RADWG%20Activities%20Overview%202024-02-2final.pdf — Search results show RADWG overview slides describing the test service and a database of tested components at radwg.web.cern.ch, open to CERN equipment groups. Found via search snippet; the PDF was not opened directly.</p>

<p>Blocking questions: Unknown whether the radiation test database remains publicly accessible without a CERN account or is now restricted to CERN personnel.</p>

<p>Caveats: Only the search-engine summary of the CERN slides was read, not the PDFs themselves.; The SSO redirect may also apply to the whole web-framework site, not just the database.</p>

</details>

<h3>KubOS — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL no longer documents KubOS. www.kubos.com/kubos/ redirects to the Xplore homepage, which covers Xplore&#x27;s constellation and Major Tom operations software and does not mention KubOS. The official repo github.com/kubos/kubos now returns 404; a Wayback capture from 2025-07-20 shows it existed then, with a last commit in April 2020. The kubos GitHub org now mostly hosts Major Tom repos. A community &#x27;KubOS-Preservation-Group&#x27; keeps a KubOS copy and docs site, but it is not an officially documented successor. KubOS itself remains relevant, open-source satellite flight software, but no official current home was found.</p>

<p>https://www.kubos.com/kubos/ — Redirects to https://www.xplore.com/, whose content covers hyperspectral data, compute and operations services and Major Tom. KubOS is not mentioned.</p>

<p>https://github.com/kubos/kubos — Returns 404 on GitHub.</p>

<p>http://web.archive.org/web/20250720105606/https://github.com/kubos/kubos — July 2025 capture: &#x27;An open source platform for satellites&#x27;, with commit datetime 2020-04-02.</p>

<p>https://github.com/KubOS-Preservation-Group — Community org: &#x27;Bringing together an inclusive community around the KubOS operating system&#x27;. Repos include kubos, kubos-linux-build and a docs site.</p>

<p>https://raw.githubusercontent.com/KubOS-Preservation-Group/kubos/master/README.md — &#x27;KubOS is an open-source software stack for satellites.&#x27; Links the community website and kubos-preservation-group.github.io/kubos docs.</p>

<p>Blocking questions: The current URL no longer describes KubOS, but the only maintained copy found (KubOS-Preservation-Group) is a community preservation effort with no official Kubos/Xplore endorsement. A replacement URL would need maintainer judgment.; Unknown whether Kubos/Xplore deleted or privatized the official kubos/kubos repo, or moved it somewhere unfound.</p>

<p>Caveats: docs.kubos.com could not be reached from this environment.; Whether Xplore or Kubos officially endorses any KubOS home is unknown.</p>

</details>

<h3>Linux4Space — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>The description is confirmed by the project&#x27;s official GitLab repo: &#x27;an open source Yocto based Linux distribution suitable for space applications&#x27;. However, linux4space.org (and wiki.linux4space.org) refused or timed out on every connection from this environment, including via a second fetch tool. The latest website capture found is from June 2025 and is JS-only. The official GitLab group was last active in November 2024 (requirements repo) and May 2024 (yocto repo). Whether the listed website still serves the project is unresolved.</p>

<p>https://gitlab.com/linux4space/linux4space-yocto/-/raw/main/README.md — &#x27;Linux4Space is a collaborative open source project founded with the intention of creating an open source Yocto based Linux distribution suitable for space applications… compliant with ESA… Standards.&#x27;</p>

<p>https://gitlab.com/api/v4/groups/linux4space — Projects: linux4space-management (last activity 2024-10-08), linux4space-yocto (2024-05-23) and linux4space_requirements (2024-11-20). None archived.</p>

<p>https://linux4space.org/ — Connection refused or timed out on https (ECONNREFUSED 147.230.21.191:443 via WebFetch, timeout via curl).</p>

<p>http://web.archive.org/web/20250623022412/https://www.linux4space.org/ — June 2025 capture exists; the page body is a JS app shell (&#x27;You need to enable JavaScript&#x27;).</p>

<p>Blocking questions: Unknown whether linux4space.org is still online. If it is permanently gone, https://gitlab.com/linux4space/linux4space-yocto would be the official alternate URL, but that has not been decided.</p>

<p>Caveats: The connection failure may be temporary or specific to this network; it does not by itself indicate the project is dead.; The GitHub org linux4space now shows a single &#x27;documentation&#x27; repo with no README.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>SYNOPSIS — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>https://github.com/NASA-AMMOS/synopsis currently returns HTTP 404 on the HTML page, the API and raw README paths, and there is no rename redirect. The ecosyste.ms index last synced the repo on 2026-10-29 and showed it as public and not archived (&#x27;Science Yield improvemeNt via Onboard Prioritization and Summary of Information System&#x27;). So it disappeared recently, or became private or restricted. I can&#x27;t tell whether this is temporary, a visibility change, or a move. No successor location was found.</p>

<p>https://github.com/NASA-AMMOS/synopsis — HTTP 404 on repeated requests. No redirect. The nasa-jpl/synopsis and raw.githubusercontent paths also return 404.</p>

<p>https://repos.ecosyste.ms/api/v1/hosts/GitHub/repositories/NASA-AMMOS%2Fsynopsis — Indexed as NASA-AMMOS/synopsis. Description: &#x27;Science Yield improvemeNt via Onboard Prioritization and Summary of Information System (SYNOPSIS)&#x27;. archived=false, default_branch main, last pushed 2024-09-03, last synced 2026-10-29.</p>

<p>http://web.archive.org/web/20241004230247/https://github.com/NASA-AMMOS/synopsis — A Wayback snapshot from 2024-10-04 exists. Per search summaries, the README described downlink prioritization of raw and autonomous science data products with cFS build instructions.</p>

<p>Blocking questions: The current location and availability of the NASA-AMMOS/synopsis repository are unknown. No official rename, move or retirement notice was found.; Recheck the URL later and look for an official NASA-AMMOS announcement before changing the entry.</p>

<p>Caveats: A 404 may be temporary or caused by a visibility change. It is not evidence the project ended.; I did not read the archived README directly. The description check relies on ecosyste.ms metadata and search summaries.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Where the ISS at? — uncertain</h3>

<details>
<summary>Evidence and limitations</summary>

<p>wheretheiss.at is live with real-time ISS tracking, and its documented REST API works: api.wheretheiss.at/v1/satellites/25544 returned a current position. The About page confirms it was built by Bill Shupp, owner of the shupp/Predict repo. However, the &#x27;email push notifications for upcoming passes&#x27; claim could not be verified. The homepage only offers &#x27;Sign In with Twitter to get visible passes and notifications&#x27;, and that login endpoint returned HTTP 403. The blog that might confirm the Predict basis also returned 403.</p>

<p>https://wheretheiss.at/ — Live real-time ISS position (altitude, velocity, lat/lon); text &#x27;Sign In with Twitter to get visible passes and notifications for my location&#x27;; footer © 2013 Linzig, LLC.</p>

<p>https://wheretheiss.at/w/developer — WTIA REST API documentation: current, past or future ISS position, timezone info and TLE data; no auth; ~1 req/s rate limit.</p>

<p>https://api.wheretheiss.at/v1/satellites/25544 — Returned live JSON with ISS latitude, longitude, altitude and velocity, so the API works.</p>

<p>https://wheretheiss.at/w/about — &#x27;Where the ISS at was built by Bill Shupp (me)&#x27;, built to learn how satellite tracking and predictions work.</p>

<p>https://wheretheiss.at/w/login/prepare?ezrpd=twitter — Twitter login endpoint returned HTTP 403 Forbidden; could not reach the notification sign-up flow.</p>

<p>Blocking questions: Unresolved whether pass notifications (and specifically email notifications) still work: the homepage advertises Twitter-based sign-in for notifications, but the login endpoint returned 403.; Not confirmed from a current official source that the site is still based on shupp/Predict (the blog returned 403).</p>

<p>Caveats: The 403 may be bot-blocking rather than a removed feature; it is not evidence that notifications are gone.; Did not confirm from an official source that the site currently uses shupp/Predict; author identity makes it plausible.</p>

</details>

<details>
<summary>37 unresolved keeps</summary>

These entries were not added to the baseline.

<h3>VIRGO — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The README supports the existing spectrometer description. Virgo capitalization is official, but GitHub URLs are case-insensitive and the all-caps label is a cosmetic variant, not a demonstrated identity or freshness defect. Exclude this optional casing-only change from the recommended-change inventory.</p>

<p>https://github.com/0xCoto/Virgo — The GitHub API returns full_name &#x27;0xCoto/Virgo&#x27;, not archived, description &#x27;📡 Virgo: A Versatile Spectrometer for Radio Astronomy&#x27;, homepage https://virgo.readthedocs.io/en/latest/, last pushed 2023-07-23.</p>

<p>https://raw.githubusercontent.com/0xCoto/Virgo/master/README.md — &#x27;Virgo is an easy-to-use open-source spectrometer and radiometer based on Python and GNU Radio … applicable to any radio telescope working with a GR-supported software-defined radio&#x27;. It is published in JOSS and on PyPI as astro-virgo.</p>

<p>https://virgo.readthedocs.io/en/latest/ — The documentation site is reachable (HTTP 200).</p>

<p>Caveats: The repository has had no pushes since 2023. That isn&#x27;t a reason for removal.; The old mixed-case URL still resolves on GitHub.</p>

<p>Independent source check: The README supports the existing spectrometer description. Virgo capitalization is official, but GitHub URLs are case-insensitive and the all-caps label is a cosmetic variant, not a demonstrated identity or freshness defect. Exclude this optional casing-only change from the recommended-change inventory.</p>

<p>https://github.com/0xCoto/Virgo/blob/master/README.md — Open-source spectrometer/radiometer identity verified; blobd519087415d0e8e1a314608d4b033a6bc73804d2.</p>

</details>

<h3>ASCL.net — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The ASCL describes itself as &#x27;a free online registry and repository for source codes of interest to astronomers and astrophysicists&#x27;, and new codes were added as recently as 9 November 2026.</p>

<p>https://ascl.net/ — http://ascl.net/ redirects to https. The page reads &#x27;The Astrophysics Source Code Library (ASCL) is a free online registry and repository...&#x27; and lists recent additions dated 2026 Nov 09.</p>

<p>Caveats: Updating the URL from http to https is optional; the redirect works.</p>

</details>

<h3>Resources and references on the topic of space exploration — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>Direct fetches return HTTP 403, a bot block rather than a dead page. The official StackExchange API shows the question is open, score 38, with 7 answers listing reference books, launch vehicle manuals, free online courses and textbooks, and NASA monographs. Last activity was in 2026. This matches the description.</p>

<p>https://space.meta.stackexchange.com/questions/249/resources-and-references-on-the-topic-of-space-exploration — curl returns 403. Through api.stackexchange.com (site=meta.space): title matches, not closed, 7 answers, score 38. The answers cover SMAD and other books, launch vehicle user manuals, online courses and textbooks, and NASA design-criteria monographs.</p>

<p>Caveats: I read the page through the StackExchange API, not the rendered page, because of the 403. Recheck the link before acting on it.; Individual links inside the answers were not checked.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Satcat.com — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>satcat.com redirects to www.satcat.com. The site is still branded by Kayhan Space and offers search, visualizations (3D globe, launch stats) and design tools (orbit designer, maneuver designer).</p>

<p>https://www.satcat.com/ — Titled &quot;Satcat | Spaceflight Intelligence Exchange&quot; with Kayhan Space branding. Navigation includes Directory, 3D Globe, Conjunctions, Space weather, Launch stats and a Design Sandbox containing an Orbit designer and a Maneuver designer. Shows &quot;77,452 searchable objects&quot;.</p>

<p>Caveats: The site redirects to the www host. The listed URL still works, so no change is needed.</p>

</details>

<h3>Gaia Data Releases — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The ESA Cosmos Gaia release page is live and lists Gaia data releases (DR4, FPR and earlier) with data access.</p>

<p>https://www.cosmos.esa.int/web/gaia/release — The page title is &quot;Gaia Data Release Scenario&quot;. Navigation includes Data Release 4 (overview, content, papers, tools), the Focused Product Release and the Gaia ESA Archive.</p>

<p>Caveats: The entry is not editable.</p>

</details>

<h3>Small Satellite Information Search — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The S3VI federated search is live. Its text matches the entry almost verbatim: it lets the public search databases &quot;for small spacecraft parts, technologies and conference proceedings&quot;.</p>

<p>https://s3vi.ndc.nasa.gov/ — States &quot;S3VI has established this federated search capability that serves as an entry point to the SmallSat Parts On Orbit Now (SPOON) database and other ... databases to allow the public to search multiple databases for small spacecraft parts, technologies and conference proceedings.&quot; Sources include TechPort, SBIR/STTR, NEPP, SPOON, satsearch and SmallSat/CubeSat proceedings.</p>

</details>

<h3>Space Apps Challenge — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The official Space Apps About page (read with TLS verification disabled after a local certificate error) says Space Apps is funded by NASA&#x27;s Science Mission Directorate through a contract with Booz Allen Hamilton, Mindgrub and SecondMuse. A 2026 event is running, so the description is supported.</p>

<p>https://www.spaceappschallenge.org/about/ — States &quot;NASA Space Apps is funded by NASA&#x27;s Science Mission Directorate through a contract with Booz Allen Hamilton, Mindgrub, and SecondMuse. The NASA Space Apps Global Organizing (GO) Team is composed of members of these three organizations.&quot; Copyright 2026 NASA.</p>

<p>https://astrobiology.com/2026/09/04/registration-is-now-open-for-the-2026-nasa-space-apps-challenge/ — This is a search result only; the page was not opened. Its title says registration is open for the 2026 Space Apps Challenge, which a search summary places on November 14–15, 2026.</p>

<p>Caveats: The certificate failure is local to this environment (&quot;unable to get local issuer certificate&quot;) and is not evidence that the site is broken. Lychee should recheck.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>data.nasa.gov — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>data.nasa.gov is live as the NASA Open Data Portal. It catalogs NASA datasets and links to APIs (api.nasa.gov), code and a visualization page, which matches the description.</p>

<p>https://data.nasa.gov/ — Describes itself as &quot;NASA&#x27;s publicly available metadata repository, providing information about datasets related to science, space exploration, aeronautics, and more.&quot; Links to api.nasa.gov, code.nasa.gov and a visualizations page.</p>

<p>Caveats: Fetched through WebFetch after curl through the proxy failed. Notes that the site describes datasets rather than hosting them, which is consistent with &quot;catalog&quot;.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Bhuvan — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The listed URL redirects to the Bhuvan home page, titled &#x27;Indian Geo Platform of ISRO&#x27;. The site is active, with 2026 training announcements and a NextGen portal. &#x27;ISRO&#x27;s Geoportal&#x27; is accurate.</p>

<p>https://bhuvan.nrsc.gov.in/home/index.php — bhuvan_links.php redirects here. The page is titled &#x27;Indian Geo Platform of ISRO&#x27; and lists current updates, including in-person training on 16-18 December 2026 and the Bhuvan NextGen Portal.</p>

<p>Caveats: The old bhuvan_links.php path now redirects to home/index.php. A maintainer may optionally update the link to the canonical URL.</p>

</details>

<h3>Earth on AWS — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The Earth on AWS page is live and still about planetary-scale applications built on open geospatial data, including the Registry of Open Data on AWS. The entry has no description to check.</p>

<p>https://aws.amazon.com/earth/ — Page titled &#x27;Earth on AWS&#x27;: &#x27;Build planetary-scale applications in the cloud with open geospatial data. Registry of Open Data on AWS...&#x27;</p>

<p>Caveats: The trailing-slash redirect is cosmetic.</p>

</details>

<h3>Global Forest Watch Open Data Portal — keep</h3>

<p>Source or watched-source coverage changed since research.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The GFW Open Data Portal is live: the http URL redirects to https. Its dataset search returns tree cover loss datasets and a &#x27;Tree cover gain (2000-2012)&#x27; dataset, so the description is still supported.</p>

<p>https://data.globalforestwatch.org/ — Page titled &#x27;Global Forest Watch Open Data Portal&#x27;. The http link redirects to https.</p>

<p>https://data.globalforestwatch.org/api/search/v1/collections/dataset/items?q=tree%20cover%20gain&amp;limit=5 — Returns datasets including &#x27;Tree cover gain (2000-2012)&#x27;. A &#x27;tree cover loss&#x27; search returns 10 matches, including &#x27;Countries with greatest tree cover loss 2001 to 2015&#x27;.</p>

<p>Caveats: The portal is JavaScript-rendered, so I checked datasets through its search API rather than the rendered UI.; The link could optionally be switched to https.</p>

</details>

<h3>Google Earth — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>Google Earth is reachable: the URL redirects to earth.google.com/web/. The entry has no description.</p>

<p>https://earth.google.com/web/ — earth.google.com redirects here. The page is titled &#x27;Google Earth&#x27;. The non-browser client got a browser-support notice with launch options.</p>

<p>Caveats: The app was not run in a supported browser.</p>

</details>

<h3>Google&#x27;s Earth Engine — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The description matches the current Earth Engine Data Catalog text word for word.</p>

<p>https://developers.google.com/earth-engine/datasets — &#x27;Earth Engine&#x27;s public data archive includes more than forty years of historical imagery and scientific datasets, updated and expanded daily.&#x27;</p>

</details>

<h3>Launch Library 2 — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The Launch Library 2 page confirms it is the official successor of Launch Library and Space Launch Now. Data is free (15 unauthenticated requests per hour) and covers launches, events, agencies, astronauts, space stations, and more. The Space Devs home page and the Discord invite (guild &#x27;The Space Devs&#x27;) both resolve. All claims are supported.</p>

<p>https://thespacedevs.com/llapi — &#x27;The Launch Library 2 API is the official successor of the popular Launch Library API... including everything the broader Space Launch Now API had to offer... the entire database is accessible to everyone, for free.&#x27; Free tier: 15 non-authenticated requests/hour. Endpoints: launches, events, agencies, astronauts, space stations, expeditions, dockings, and more.</p>

<p>https://thespacedevs.com/ — Resolves (200); The Space Devs site with Launch Library 2 and Spaceflight News API.</p>

<p>https://discord.gg/wxEGcWXbsD — Redirects to discord.com/invite/wxEGcWXbsD. The Discord invite API reports the guild name &#x27;The Space Devs&#x27;, so the invite is valid.</p>

<p>Caveats: &#x27;Free to use&#x27; is subject to a 15 requests/hour limit; higher rates require Patreon support. The entry&#x27;s wording remains accurate.</p>

</details>

<h3>RocketLaunch.Live — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The official API page confirms a read-only JSON API of manually curated launch data, updated throughout the day. Entities include companies, launches, locations, missions, pads, tags, and vehicles. Free access covers the next five launches, and full access requires Premium. This matches the description.</p>

<p>https://www.rocketlaunch.live/api — &#x27;Our data is manually curated... Data for upcoming launches is updated regularly throughout each day.&#x27; &#x27;Full access to the API is available to our Premium Members only.&#x27; &#x27;The next five launches are accessible freely&#x27; via https://fdo.rocketlaunch.live/json/launches/next/5. Entities: Companies, Launches, Locations, Missions, Pads, Tags, Vehicles. JSON responses.</p>

<p>Caveats: Did not call the API to verify launch-window or estimated-date fields.</p>

</details>

<h3>IAU Minor Planet Center — keep</h3>

<p>Source or watched-source coverage changed since research.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The MPC data page is live and actively updated (files dated 2026/11/10). It provides orbit files for minor planets, NEAs, PHAs, TNOs, and comets. The MPC home page restates its role as &#x27;the single worldwide location for receipt and distribution of positional measurements of minor planets, comets and outer irregular natural satellites.&#x27; An initial 403 was bot filtering; a browser-like request returned 200.</p>

<p>https://minorplanetcenter.net/data — Returns 200 with browser headers (403 with a minimal user agent). Lists MPCORB extended files, NEA.txt, PHA.txt, DAILY.DAT, Distant.txt, Unusual.txt, CometEls.txt, and AllCometEls.txt with last updates on 2026/11/10.</p>

<p>https://www.minorplanetcenter.net/ — &#x27;The Minor Planet Center (MPC) is the single worldwide location for receipt and distribution of positional measurements of minor planets, comets and outer irregular natural satellites of the major planets.&#x27; Banner: &#x27;The MPC is in preparation mode&#x27; (dated 2026 09 28).</p>

<p>Caveats: The meaning of the MPC &#x27;preparation mode&#x27; notice was not investigated; recheck if it affects data services.</p>

</details>

<h3>Spaceflight News API — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>All three linked resources resolve. Spaceflight News API is live and links to The Space Devs. The listed Discord invite (wxEGcWXbsD) does not expire and points to &#x27;The Space Devs&#x27; server, the same server as the invite currently linked from both official sites.</p>

<p>https://spaceflightnewsapi.net/ — Title &#x27;The Most Complete Spaceflight Related News API&#x27;. Offers news, blogs and reports, and links to Discord, GitHub and The Space Devs. Copyright 2026 Spaceflight News API &amp; The Space Devs.</p>

<p>https://thespacedevs.com/ — Lists Launch Library 2 and Spaceflight News API under APIs. Describes itself as space enthusiast developers providing free public APIs.</p>

<p>https://discord.com/api/v9/invites/wxEGcWXbsD — Invite resolves to guild &#x27;The Space Devs&#x27; (id 676725644444565514) with expires_at null. The site-linked invite p7ntkNA resolves to the same guild.</p>

<p>Caveats: The official sites now link Discord invite p7ntkNA. Switching to it is optional because both reach the same server.; Whether the API is free is based on site wording; I did not check its terms.</p>

</details>

<h3>SUCHAI-2 — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The GitLab project exists under spel-uchile with the same path. Its README (default branch &#x27;framework&#x27;) says it contains the flight and ground software for SUCHAI-2, SUCHAI-3 and PlantSat, built on the SUCHAI Flight Software framework.</p>

<p>https://gitlab.com/spel-uchile/suchai-2-software — Project spel-uchile/suchai-2-software, description &#x27;SUCHAI 2, 3 and PlantSat flight software&#x27;, default branch &#x27;framework&#x27;, last activity 2026-03-13.</p>

<p>https://gitlab.com/spel-uchile/suchai-2-software/-/raw/framework/README.md — &#x27;This repository contains the source code of the SUCHAI-2, SUCHAI-3 and PlantSat satellites onboard software (aka flight software), and the ground segment software.&#x27; Includes apps/groundstation and apps/plantsat, with build scripts for suchai2 and suchai3.</p>

<p>Caveats: The README says building the actual flight software needs the Nanomind A3200 SDK, which is available only on request. &#x27;Complete&#x27; is the entry&#x27;s framing.; Other branches exist: master (last commit 2021-09-17), framework-sim (2026-03-13) and framework-sim-log-mongdb (2024-03-28). The master README is a template stub. I did not assess the maintenance status of these branches.</p>

</details>

<h3>Hackaday.io Satellite Projects — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The curated Hackaday.io list is live and still covers satellite projects and ground stations.</p>

<p>https://hackaday.io/list/4321-satellite-projects — &#x27;Satellite Projects — High flying orbital projects, and the ground stations to communicate with them&#x27;, curated by Adam Fabio, Mike Szczys and Jasmine Brackett. It shows 32.9k views, 495 followers and 9 projects.</p>

<p>Caveats: I did not review the individual projects. The list is small.; The entry is marked non-editable.</p>

</details>

<h3>Quetzal-1 — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The packet snapshot fetch failed, but the GitHub org page loaded fine. Its official profile README confirms every claim: a 1U CubeSat from a UVG engineering team, which operated for 211 days. The org hosts flight-software, hardware and telemetry repositories.</p>

<p>https://github.com/Quetzal-1-CubeSat-Team — Org &#x27;Quetzal-1 CubeSat Team&#x27;: &#x27;Engineering Team from Universidad del Valle de Guatemala (UVG) that developed the Quetzal-1 CubeSat, the first Guatemalan nanosatellite to operate in space&#x27;. Repos: quetzal1-flight-software, quetzal1-hardware, quetzal1-telemetry and .github.</p>

<p>https://raw.githubusercontent.com/Quetzal-1-CubeSat-Team/.github/main/profile/README.md — &#x27;Quetzal-1 was a 1U CubeSat developed by an engineering team from Universidad del Valle de Guatemala (UVG)... Quetzal-1 operated successfully in space from the day of deployment to November 2020. This amounted to 211 days of operation&#x27;.</p>

<p>Caveats: The GitHub API was rate-limited, so I could not get repository activity or archive flags. This is historic mission material either way.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>European Space Agency GitHub Repository — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The packet snapshot fetch failed, but https://github.com/esa loaded fine. It is the European Space Agency GitHub organization, hosting active space software such as pykep, pygmo2, nanosat-mo-framework and asn1scc.</p>

<p>https://github.com/esa — og:title &#x27;European Space Agency&#x27;. Description: &#x27;Research code from communities linked to The European Space Agency (ESA).&#x27; Repos listed include pagmo2, pygmo2, pykep, nanosat-mo-framework, asn1scc, opengeode, torchquad and euclid-jupyter-notebooks.</p>

<p>Caveats: The GitHub API was rate-limited, so I could not read the org&#x27;s verified-domain status. I identified it as ESA&#x27;s from its name, description and repositories.; The entry is marked non-editable.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>GRID — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The GRID site is live and still describes an on-demand ground station service with a global network and an API. The linked Python SDK repo (5OKB/grid-python-sdk) resolves without a redirect and is not archived. Its README and pyproject describe the SDK as a client for GRID&#x27;s auth, REST API, event and MQTT services. The description is accurate.</p>

<p>https://www.gridgs.com/ — HTTP 200. Page reads &#x27;Your personal on-demand ground station service&#x27;, &#x27;Global network of ground stations&#x27;, &#x27;Easy Software Integration... via the GRID API&#x27;, &#x27;Fixed rates per minute of communication&#x27;.</p>

<p>https://raw.githubusercontent.com/5OKB/grid-python-sdk/main/README.md — &#x27;A Python SDK to simplify integration with GRID services&#x27;. Lists GridAuthClient, GridApiClient, GridEventSubscriber and GridMQTTClient, and links to gridgs.com and the PyPI package gridgs-sdk. Notes that the SDK is in beta.</p>

<p>https://raw.githubusercontent.com/5OKB/grid-python-sdk/main/pyproject.toml — Package gridgs-sdk version 1.1.1, author 5OKB, MIT license, depends on paho-mqtt and python-keycloak.</p>

<p>https://github.com/5OKB/grid-python-sdk — HTTP 200 with no redirect. Canonical name is 5OKB/grid-python-sdk.</p>

<p>Caveats: The SDK says it is in beta. The homepage still shows &#x27;Early Access&#x27; and small deployment figures (&#x27;4 ground stations already deployed&#x27;).; The GitHub API was rate-limited, so archive status comes from the packet snapshot and the rendered page.</p>

</details>

<h3>SatNOGS — keep</h3>

<p>Source or watched-source coverage changed since research.</p>

<details>
<summary>Evidence and limitations</summary>

<p>SatNOGS.org is live, run by the Libre Space Foundation, and describes its Network project with wording that matches the entry almost exactly.</p>

<p>https://satnogs.org/ — HTTP 200. Title &#x27;SatNOGS – Open Source global network of satellite ground-stations&#x27;. The Network project is described as &#x27;A global network of satellite ground stations, designed as an open source participatory project&#x27;. Also links to DB, Documentation and the Libre Space Foundation.</p>

<p>Caveats: Did not inspect the network dashboard or station counts.</p>

</details>

<h3>TinyGS — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>TinyGS is live and describes itself as an open-source global satellite ground-station network that uses cheap ESP32 LoRa boards. It supports satellite operators and offers real-time telemetry. The description is accurate.</p>

<p>https://tinygs.com/ — HTTP 200. &#x27;TinyGS is the open-source global satellite network&#x27;. &#x27;turns a $20 LoRa board into a fully functional satellite ground station&#x27;. &#x27;Any ESP32 LoRa board ($20–30)&#x27;. &#x27;Over 2,200 active stations&#x27;. Includes a section for satellite operators.</p>

<p>Caveats: The &#x27;operate&#x27; part of the description (uplink/telecommand) was not checked in detail. The homepage stresses receiving telemetry and support for operators.</p>

</details>

<h3>COSMOS — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>openc3.com is live and promotes OpenC3 COSMOS v7.2. COSMOS Core is described as free and open source, and it covers command and control for hardware from integration and test through mission operations. The entry&#x27;s &#x27;open source mission control and satellite test &amp; development framework&#x27; still fits.</p>

<p>https://openc3.com/ — HTTP 200. &#x27;OpenC3 COSMOS v7.2&#x27;, &#x27;COSMOS Core Free &amp; open-source&#x27;, &#x27;Satellite Integration &amp; Test&#x27;, &#x27;from integration &amp; test through launch, mission ops, and de-orbit&#x27;, telemetry and commanding, Script Runner, plugins.</p>

<p>Caveats: There is also a commercial COSMOS Enterprise edition. The listed open-source Core still exists.; The GitHub repo (OpenC3/cosmos) could not be checked through the API because of rate limiting.</p>

</details>

<h3>GMAT — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The SourceForge HTML page returns 403 to the client because of a Cloudflare &#x27;Just a moment&#x27; challenge. That is bot protection, not a dead page. The SourceForge REST API and file metadata were readable: the project is &#x27;active&#x27;, and GMAT R2026a was released in April 2026. NASA&#x27;s official GitHub repo (nasa/GMAT) describes GMAT as an open-source system for space mission design, optimization and navigation. The description is accurate.</p>

<p>https://sourceforge.net/rest/p/gmat — JSON: name GMAT, status &#x27;active&#x27;, &#x27;open-source tool for space mission design and navigation... developed by a team of NASA, private industry...&#x27;, announces release R2026a, external homepage gmat.atlassian.net.</p>

<p>https://sourceforge.net/projects/gmat/best_release.json — The best release is /GMAT/GMAT-R2026a/gmat-win-R2026a.zip, dated 2026-04-03. A macOS R2026a build is also listed.</p>

<p>https://github.com/nasa/GMAT — Official NASA repo, HTTP 200. &#x27;The General Mission Analysis Tool (GMAT) is the world&#x27;s leading enterprise, multi-mission, open source software system for space mission design, optimization, and navigation.&#x27;</p>

<p>https://sourceforge.net/projects/gmat/ — Returns HTTP 403 with a Cloudflare &#x27;Just a moment... Enable JavaScript and cookies&#x27; challenge to curl. Lychee may hit the same block.</p>

<p>Caveats: The SourceForge HTML page could not be rendered directly because of the anti-bot challenge. A link checker may report it as failing. Recheck rather than change it.; The maintainer could choose the GMAT wiki (gmat.atlassian.net) or nasa/GMAT as the link. Either would be optional.</p>

</details>

<h3>NASA Ames Research Center Trajectory Browser — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The NASA Ames Trajectory Browser is live. Its page text matches the entry exactly.</p>

<p>https://trajbrowser.arc.nasa.gov/traj_browser.php — HTTP 200. &#x27;This page features a tool to find spacecraft trajectories to planets and small-bodies.&#x27; The search form takes NEO, comet and planet destinations and mission types (one-way, round-trip, flyby, rendezvous).</p>

<p>Caveats: How current the underlying small-body dataset is was not checked.</p>

</details>

<h3>Oresat — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The GitHub org page https://github.com/oresat is live as &#x27;OreSat Open Source CubeSat Project&#x27;, with active-looking hardware/software repos. The official site oresat.org describes OreSat as fully open-source CubeSats from Portland State Aerospace Society, two of which are in low Earth orbit. Fits Spacecraft Hardware.</p>

<p>https://github.com/oresat — 200, title &#x27;OreSat Open Source CubeSat Project&#x27;. Repos include oresat-c3-hardware, oresat-batteries, oresat-star-tracker-hardware/software, oresat-firmware, oresat-olaf, oresat-configs.</p>

<p>https://www.oresat.org/ — &#x27;All of our satellites rely on the fully open source OreSat bus... a DIY platform for designing and building your own CubeSat. We&#x27;re the Portland State Aerospace Society (PSAS)... OreSat is a completely open source project.&#x27; Lists OreSat0, OreSat0.5 and mission pages.</p>

<p>Caveats: The snapshot failure was likely due to the URL being an org rather than a repo; the page itself is reachable.; No official source found that uses the exact phrase &#x27;Oregon Small Satellite Project&#x27;. OreSat is run by PSAS at Portland State. This is an optional wording clarification, not a confirmed error.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>PyCubed — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>PyCubed is still an open-source CubeSat hardware and software platform. The official GitHub org (pycubed) keeps its hardware, software, firmware and documentation repos, and their READMEs still link to the maintainer&#x27;s Notion resource pages. The description matches the title of the project&#x27;s 2019 SmallSat paper. The listed Notion URL resolves (200, redirects to app.notion.com).</p>

<p>https://www.notion.so/PyCubed-4cbfac7e9b684852a2ab2193bd485c4d — Returns 200 after redirecting to app.notion.com/p/PyCubed-4cbfac7e9b684852a2ab2193bd485c4d. The page renders with client-side JS, so its body text could not be extracted.</p>

<p>https://github.com/pycubed — The org lists the hardware, software, firmware, documentation, library_pycubed.py, library_pycubed_rfm9x.py, software_example_beepsat and forums repos.</p>

<p>https://raw.githubusercontent.com/pycubed/hardware/master/README.md — Describes a 4-layer flight PCB (FR408HR for flight) ported to KiCad &#x27;to maintain the open-source nature of the project&#x27;. Links the 2019 SmallSat paper and an &#x27;All PyCubed Resources&#x27; Notion page.</p>

<p>https://raw.githubusercontent.com/pycubed/software/master/README.md — &#x27;Default files for PyCubed boards.&#x27; Hardware is CC BY-SA 4.0; software and firmware are MIT.</p>

<p>Caveats: The Notion page body could not be read because it is JS-rendered and the Notion API returned an empty recordMap. Its exact content is unverified.; pycubed.org, which the hardware README&#x27;s changelog links to, now serves a NameBright &#x27;Coming Soon&#x27; parking page. This does not affect the listed Notion URL.; The radiation-tested claim rests on the project&#x27;s own paper title. The test data was not re-read.</p>

</details>

<h3>Qubik — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The URL is the Libre Space Foundation GitLab group for QUBIK, described as a &#x27;Pocketqube mission for LEOP satellite identification and tracking&#x27;. It has active subprojects for comms software, structure, docs and assembly guide, licensed GPL-3.0 (software) and CERN OHL v1.2 (hardware). The open-source software and hardware PocketQube description holds.</p>

<p>https://gitlab.com/librespacefoundation/qubik — Returns 200. The group title is QUBIK: &#x27;Pocketqube mission for LEOP satellite identification and tracking&#x27;.</p>

<p>https://gitlab.com/api/v4/groups/librespacefoundation%2Fqubik — Projects include qubik-comms-sw (last activity 2026-11-04), qubik-structural, qubik-spb, qubik-docs, qubik-assembly-guide and qubik-org. Only pqws-power-hw is archived.</p>

<p>https://gitlab.com/api/v4/projects/librespacefoundation%2Fqubik%2Fqubik-comms-sw?license=true — qubik-comms-sw is GPL-3.0-only. qubik-structural and qubik-spb are CERN Open Hardware Licence v1.2.</p>

<p>Caveats: The URL is a GitLab group page, not a single repository.</p>

</details>

<h3>Vesper — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>Vesper is a spacecraft design tool and component database: &#x27;Rapid spacecraft design and iteration… discovering space hardware, designing spacecraft, and planning missions&#x27;, &#x27;most detailed spacecraft hardware library and design suite on the web&#x27;. It offers power analysis and interface-incompatibility alerts, so the design/analysis toolkit and hardware library claims hold. Sign-up is open, and I found no pricing page or paid tier.</p>

<p>https://vesperastro.com/ — The homepage describes a component database, design tools with power analysis, and interface or budget alerts. Footer: © 2026 Vesper.</p>

<p>https://vesperastro.com/roadmap/ — Roadmap items include component database expansion and telecom subsystem analysis, showing active development.</p>

<p>https://vesperastro.com/accounts/signup/ — The sign-up form asks for name, username, email and occupation. No payment or plan selection is shown.</p>

<p>Caveats: No page explicitly says the service is &#x27;free&#x27;. The claim is consistent with open sign-up and the absence of a pricing page but is not affirmatively stated, and the terms of service had no pricing language.</p>

</details>

<h3>LibreCube — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>librecube.org is live. It describes LibreCube as &#x27;an international community with the goal of creating an entire ecosystem of open-source hardware and software components for space exploration systems&#x27;, based on open source, standards and &#x27;reusable, modular elements with standardized interfaces&#x27;. This supports the description of a generic architecture with standardized interfaces for combining and reusing elements.</p>

<p>https://librecube.org/ — Homepage: &#x27;Build, Operate, Learn open-source space systems&#x27;. Principles: Open Source, Standards, Modularity (&#x27;ecosystem of reusable, modular elements with standardized interfaces&#x27;). Links to Repos and Docs.</p>

<p>Caveats: The entry&#x27;s &#x27;Open source space and Earth exploration&#x27; tagline is older wording; the current site emphasizes space systems. This is not a factual conflict.</p>

</details>

<h3>OpenSatKit — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>OpenSatKit still describes itself as a cFS platform combining Ball&#x27;s COSMOS, NASA cFS and the 42 simulator for training and app development. The entry&#x27;s description stays accurate. The official wiki now says &#x27;The Ball Aerospace version of COSMOS used in OpenSatKit is no longer maintained&#x27; and points users to the author&#x27;s newer cFS Basecamp project, which is already listed as entry 314. Linked resources: nasa/cfs resolves to nasa/cFS; cosmosrb.com redirects to openc3.com (OpenC3 COSMOS, the successor home of COSMOS); software.nasa.gov/software/GSC-16720-1 is the NASA catalog page for 42.</p>

<p>https://raw.githubusercontent.com/OpenSatKit/OpenSatKit/master/README.md — &#x27;OpenSatKit is a multi-facet platform for working with NASA&#x27;s open-source core Flight System (cFS)… combines… Ball Aerospace Corporation&#x27;s COSMOS… NASA&#x27;s cFS… and Eric Stoneking&#x27;s 42 Simulator.&#x27;</p>

<p>https://github.com/OpenSatKit/OpenSatKit/wiki — Wiki home, edited January 22, 2024: &#x27;The Ball Aerospace version of COSMOS used in OpenSatKit is no longer maintained… I have a new project called cFS Basecamp that provides a cFS training and application development environment.&#x27;</p>

<p>https://cosmosrb.com/ — Redirects to https://openc3.com/.</p>

<p>https://software.nasa.gov/software/GSC-16720-1 — Title: &#x27;42: A Comprehensive General-Purpose Simulation of Attitude and Trajectory Dynamics and Control of Multiple Spacecraft…&#x27; (GSC-16720-1), NASA Software Catalog.</p>

<p>Caveats: The wiki points users to cFS Basecamp but does not formally declare OpenSatKit superseded. Basecamp is already listed separately, so a replace action would duplicate it.; Optional caveat for maintainers: the COSMOS link now lands on OpenC3, a newer COSMOS version than the Ball COSMOS bundled in OSK. A note that OSK&#x27;s bundled COSMOS is unmaintained could be added.</p>

</details>

<h3>SatSearch — keep</h3>

<p>Source snapshot unavailable.</p>

<details>
<summary>Evidence and limitations</summary>

<p>satsearch.co (redirects to https) is live as &#x27;the global marketplace for the space industry&#x27;, where users find space products and suppliers by category. CubeSatShop.com could not be reached directly: https timed out or refused the connection, and http returned 502. A Wayback capture from 2026-06-14 shows its About page live, describing an ISIS-launched webshop that lists off-the-shelf CubeSat components from 25+ vendors with key subsystem information. Both still fit &#x27;search engines for satellite parts&#x27;. The CubeSatShop access failure looks temporary and warrants a recheck.</p>

<p>https://satsearch.co/ — &#x27;Find products and services for your next space mission&#x27;, with a product, supplier and mission search across many subsystem categories.</p>

<p>http://web.archive.org/web/20260614094130/https://www.cubesatshop.com/about/ — June 2026 capture: &#x27;CubeSatShop.com was launched in 2009 by ISIS… comprehensive overview of readily available components and subsystems… standard method of providing key subsystem information.&#x27;</p>

<p>https://www.cubesatshop.com/ — Live fetch from this environment: connection refused or timed out on https; http://www.cubesatshop.com/ returned 502.</p>

<p>Caveats: CubeSatShop&#x27;s live state as of November 2026 is unverified because of the connection failure; the evidence is a June 2026 archive capture plus search-index results.; CubeSatShop is a webshop/catalog rather than a pure search engine. This is a nuance, not a false claim.</p>

<p>Source snapshot incomplete; excluded from the saved baseline.</p>

</details>

<h3>Gpredict — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>Gpredict&#x27;s official site still describes it as a &#x27;real-time satellite tracking and orbit prediction application&#x27; for Linux, macOS and Windows, which matches the entry. The listed URL redirects to https://oz9aec.dk/gpredict/, but the first cross-host hop is a 307 Temporary Redirect, and the page has no canonical link. So I can&#x27;t confirm a permanent URL change yet.</p>

<p>http://gpredict.oz9aec.net/ — Redirects 307 to https://gpredict.oz9aec.net/, then 307 to https://oz9aec.dk/gpredict, then 301 to https://oz9aec.dk/gpredict/, which returns 200.</p>

<p>https://oz9aec.dk/gpredict/ — Title: &#x27;Gpredict: Free, Real-Time Satellite Tracking and Orbit Prediction Software&#x27;. Body: &#x27;Gpredict is a real-time satellite tracking and orbit prediction application... for Linux, Mac OS X and Windows&#x27;.</p>

<p>https://github.com/csete/gpredict — The source repository resolves: &#x27;Gpredict satellite tracking application&#x27;.</p>

<p>Caveats: A maintainer may later choose to switch to https://oz9aec.dk/gpredict/ if the redirect becomes permanent. Currently the gpredict.oz9aec.net hop is a 307.</p>

</details>

<h3>Orbital Radar — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>orbitalradar.com is live as a real-time tracking and space situational awareness platform. It tracks 32,000+ objects on a 3D globe using Space-Track and CelesTrak data, and has a Satellite Re-entry Tracker, conjunction/close-approach alerts, constellation trackers (Starlink, OneWeb, GPS, Galileo, Amazon LEO) and a &#x27;Space Library&#x27; of reference articles. The description is supported.</p>

<p>https://orbitalradar.com — Title: &#x27;Orbital Radar — Live Satellite Tracking &amp; Space Intelligence&#x27;. Description: &#x27;real-time satellite tracking, space situational awareness&#x27;. Second description: &#x27;Track 32,000+ objects in real time. Live 3D globe, space debris map... powered by Space-Track and CelesTrak.&#x27; Navigation includes Satellite Re-entry Tracker, a &#x27;Close approach / conjunction&#x27; alert type, Space Library, and per-constellation trackers.</p>

<p>Caveats: The page does not use the word &#x27;encyclopaedia&#x27;. That claim corresponds to the &#x27;Space Library&#x27; explainer pages.; I did not check how &#x27;live&#x27; the re-entry forecasting and conjunction screening are beyond the UI labels.</p>

</details>

<h3>Space-Track.org — keep</h3>

<p>Source or catalog stability was not confirmed for this review.</p>

<details>
<summary>Evidence and limitations</summary>

<p>The Space-Track documentation page is live and documents its REST API (&#x27;allows users to access data on this site programmatically&#x27;). It covers the GP (TLE/mean elements), GP_HISTORY, SATCAT, SATCAT_DEBUT, DECAY, TIP and BOXSCORE classes, which support the entry&#x27;s description of programmatic access to TLEs, mean elements, catalog and debris data.</p>

<p>https://www.space-track.org/documentation — API tab says the API &#x27;allows users to access data on this site programmatically&#x27;; documented classes include Boxscore, Decay, Gp (&#x27;GP (aka TLEs)&#x27;), GpHistory, Satcat, SatcatDebut and Tip; usage throttling guidelines are listed.</p>

<p>Caveats: The API requires a free Space-Track account and has rate guidelines; that is not a factual error in the entry.; The #api fragment is client-side; the page itself resolved with HTTP 200.</p>

</details>

</details>

The complete research records remain local. This inventory contains all recommendations and unresolved entries from the saved initial review.

[One-entry integration example](https://github.com/bromanko/awesome-space/blob/codex/catalog-inventory-preview/.um/catalog-inventory/checked-example.md). Saved research with real discussion-history and patch checks.
