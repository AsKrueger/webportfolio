# Issue #6 - Verification report

Date: 2026-09-22

## Scope

The generated site was served from `dist/` at `http://localhost:8000` and checked across the eight requested routes:

- `/`
- `/proyectos/`
- `/proyectos/3d-cost-manager/`
- `/proyectos/explorersaga/`
- `/sobre-mi/`
- `/experiencia/`
- `/formacion/`
- `/contacto/`

## Results

| Area | Result | Evidence |
| --- | --- | --- |
| 320 x 800 | PASS | 8 routes checked; no horizontal overflow; one H1 per route |
| 375 x 812 | PASS | 8 routes checked; no horizontal overflow; one H1 per route |
| 768 x 1024 | PASS | 8 routes checked; no horizontal overflow; mobile menu visible |
| 1024 x 768 | PASS | 8 routes checked; no horizontal overflow; desktop navigation visible |
| 1440 x 900 | PASS | 8 routes checked; no horizontal overflow; desktop navigation visible |
| Mobile keyboard menu | PASS | Enter opens; `aria-expanded` changes; Tab reaches `Inicio`; Escape closes and restores focus |
| Keyboard focus | PASS | Tab focus has a visible 2px outline on links and the menu button |
| HTML semantics | PASS | One `header`, `nav`, `main`, and `footer` per generated page; one H1 per route; headings remain ordered |
| Images | PASS | No images are currently generated; no missing image resources |
| Console and resources | PASS | No console errors and no HTTP responses with status >= 400 across all routes |
| Assets and nested routes | PASS | CSS and JavaScript load from root and project-detail routes |
| Zoom simulation | PASS | 32 route/zoom combinations checked at 100%, 125%, 150%, and 200% |
| Reduced motion | PASS | Existing `prefers-reduced-motion` rule remains active; no new animation introduced |
| Contrast sample | PASS | Primary text 16.66:1, muted text 8.23:1, button 9.99:1, focus 13.6:1 |
| Automated audit | NOT AVAILABLE | Lighthouse/axe could not be run because Node.js, npm, and npx are not installed |

## Corrections applied

- Wrapped the home code panel and allowed hero children to shrink at narrow widths.
- Allowed long contact URLs to wrap inside the contact card at 320px.
- Put the mobile menu button before its links in DOM order so keyboard focus enters the opened menu correctly.
- Added an explicit semantic `header` landmark around the shared navigation.

## Limitations

The automated Lighthouse/axe audit was not available in the environment. Contrast values are reproducible samples from the CSS token colors, not a complete WCAG audit of every rendered text/background combination. Browser zoom was tested through a layout zoom simulation in Playwright; a manual DevTools zoom session was not available.

## Status

- Generation: verified
- Routes: verified
- Responsive behavior: verified for the listed viewports
- Manual accessibility checks: verified for keyboard, focus, semantics, images, and reduced motion
- Automated audit: unavailable in this environment
- Corrections: applied and rechecked
