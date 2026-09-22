# Issue #7 - Verification report

Date: 2026-09-22

## SEO

Audited the eight primary public route variants plus the public `curriculum.html` page generated under `dist/`:

- `/`
- `/proyectos/`
- `/proyectos/3d-cost-manager/`
- `/proyectos/explorersaga/`
- `/sobre-mi/`
- `/experiencia/`
- `/formacion/`
- `/contacto/`
- `/curriculum.html`

Results:

- 9 unique and descriptive `<title>` values.
- 9 unique meta descriptions.
- `lang="es"` and viewport metadata present on every page.
- Open Graph `title`, `description`, and `type` present.
- Twitter card, title, and description present.
- No `og:image` or `twitter:image` was added because the project has no real image asset suitable for sharing.
- Canonical tags and `og:url` are intentionally omitted until a public deployment URL is verified. Both are generated automatically when `public_url` is configured in `data.json`.
- `robots.txt` is generated with normal crawl access.
- `sitemap.xml` is not generated because no valid public base URL is currently configured.
- Legacy duplicate `sobre.html` and `proyectos.html` outputs are no longer generated.
- 9 same-origin internal links were checked from the served site; no broken responses were found.

## Performance

Measured generated output after the build:

| Resource | Size |
| --- | ---: |
| CSS | 29,626 bytes |
| JavaScript | 2,078 bytes |
| HTML pages | 3,909 to 10,564 bytes |
| robots.txt | 25 bytes |
| Images | none |
| External fonts | none |

The site has no frontend framework, CDN, external font, analytics script, or image dependency. No compression or CSS rewrite was added because the measured assets are already small and no evidence justified extra tooling.

## GitHub API

The generator uses the public unauthenticated GitHub repositories endpoint with a five-second timeout and no private credential. API failures return an empty list. A real data-flow issue was corrected: the homepage now reads `project_cards`, and the generator normalizes the curated projects from `data.json` as a fallback when GitHub is unavailable. The generator completed successfully after this correction.

## Security

- Secret-pattern scan found no API keys, tokens, passwords, private keys, or AWS access-key patterns in tracked source files.
- `.gitignore` excludes `.env`, virtual environments, build output, and Python cache files.
- Jinja autoescaping remains enabled for HTML/XML templates.
- All `_blank` links now use `rel="noopener noreferrer"`.
- No unsafe `innerHTML`, `eval`, or inline `onclick` patterns were found in the audited source.
- GitHub API access requires no credentials.

## GitHub Pages

The repository remote is `https://github.com/AsKrueger/webportfolio.git`, but the candidate GitHub Pages URLs checked returned 404 and the Pages API did not expose an active deployment. No canonical domain was invented. The static output remains suitable for publishing from `dist/`; once the actual HTTPS URL is known, set `public_url` in `data.json` and regenerate.

## Regression validation

- Static generation completed successfully with Python 3.12.
- All expected routes and CSS/JS assets exist physically in `dist/`.
- Browser sweep: 40 route/viewport checks across 320, 375, 768, 1024, and 1440px; no horizontal overflow, missing title, or missing description was found.
- Browser sweep found no console errors and no HTTP responses with status `400` or higher.
- Issue #6 responsive layout remained intact.
- Mobile menu click/ARIA behavior remained intact; `aria-expanded` and `hidden` update correctly.
- Focus styles remain present from Issue #6.
- No Lighthouse, axe, Node.js, npm, or npx executable is available in the environment, so no automated Lighthouse/axe score is reported.
- Native keyboard activation through the integrated browser automation was inconsistent during this pass; the menu remains a semantic button and the previous Issue #6 keyboard sequence was verified before these head-only/API-fallback changes.

## Changes

- Updated shared metadata in `templates/base.html`.
- Added page-specific titles and descriptions across templates.
- Added conditional canonical and social URL support.
- Added generated `robots.txt` and conditional `sitemap.xml` support.
- Removed generated duplicate legacy page outputs.
- Added explicit external-link security attributes.
- Corrected GitHub project-card data flow and offline fallback.
- Documented the optional `public_url` configuration in `README.md`.

## Status

- SEO technical structure: verified
- Performance/resource audit: verified
- Security audit: verified for the checks listed above
- Static generation: verified
- Routes/assets: verified
- Responsive regression: verified
- Automated audit: unavailable in this environment
- Canonical/sitemap public URL: pending actual deployment URL
