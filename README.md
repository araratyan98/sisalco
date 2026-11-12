# Սիս Ալկո — new website

Single-file site (`web/sis-alco.html`) with 3D bottles (three.js), GSAP/ScrollTrigger, Lenis.
Languages: HY / EN / RU. Hash routing: `#catalog`, `#p-<id>`, `#home`.

- `web/` — the page plus assets (`logo.png`, `ph/` photos, `tex/` bottle textures, `profiles.json` bottle silhouettes)
- `test/` — Playwright scripts (`npm i` first; they serve three/gsap/lenis from node_modules)
- `tools/` — one-off patch/data helpers used while building

The HTML is a fragment (no doctype): it was published as a Claude Artifact, which wraps it in a document skeleton.
To open it locally, wrap it as `test/shot.js` does.

TODO: set `FORM_ENDPOINT` in the page to a real form endpoint; verify messenger phone number (+374 44 449 244 vs +374 44 44 92 44 on Facebook).
