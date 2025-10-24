# Repository Guidelines

## Project Structure & Module Organization
The repository currently hosts three high-fidelity prototypes: `index (1).html` for the marketing home, `r2 (1).html` for the partnership flow, and `restaurant_app_prototype.html` for in-product journeys. Keep new variants in the repo root under descriptive, kebab-case filenames (for example `partner-dashboard-v1.html`) and document their purpose in the file header. Shared assets live on CDNs today; if you add local images, place them in `assets/` and update relative paths.

## Build, Test, and Development Commands
These pages are static and can be served locally without a build step. Recommended options:
- `python -m http.server 8000` - quick preview with any Python.
- `npx serve . --listen 5000` - Node-based server with caching disabled.
Run the command from the repository root and open `http://localhost:<port>`; confirm each prototype route loads as expected.

## Coding Style & Naming Conventions
Use 4-space indentation for HTML and inline scripts. Favor semantic HTML5 elements and descriptive class names; when using Tailwind utility classes, group them by layout -> spacing -> color for readability. Custom CSS should live in an embedded `<style>` block near the top of the file; if it grows beyond 200 lines, extract to `styles/<feature>.css`. JavaScript snippets should be modularized into functions with camelCase names and guarded against null selectors.

## Testing Guidelines
Automated testing is not configured; rely on manual verification. Validate responsive breakpoints at 320px, 768px, and 1280px widths, and run Lighthouse or Chrome Performance audits before sign-off. When adding interactive scripts, include a temporary console assertion verifying critical selectors resolve, then remove it before merging. Keep exploratory test notes in `docs/testing.md` if the scenario is reusable.

## Commit & Pull Request Guidelines
There is no existing Git history, so begin with Conventional Commits (`feat: add partner dashboard prototype`). Each PR should include: one-sentence summary, checklist of tested browsers/devices, and screenshots or short screen recordings for UI updates. Link any product requirements or issue IDs in the description, and request review from the design owner plus one developer peer.

## Security & Configuration Tips
Do not commit API keys; reference them via placeholders like `YOUR_API_KEY` and document retrieval steps in a separate secure channel. When embedding third-party scripts, pin exact versions and note the source URL justification in an HTML comment for future audits.
