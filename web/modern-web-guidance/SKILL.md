---
name: modern-web-guidance
description: Use when building client-side HTML/CSS/JS UI.
---

# Modern Web Guidance

Google's 200+ vetted web-platform guides, cloned locally. Consult **before** writing custom JS for UI, or adding a library that reimplements a platform primitive (dialog, popover, tooltip, carousel, table, dropdown).

**Corpus:** `C:/Users/syahd/modern-web-guidance/skills/modern-web-guidance/guides/`

## Workflow

1. **Find** — grep titles + headings, one capability per query:
```sh
cd C:/Users/syahd/modern-web-guidance/skills/modern-web-guidance/guides
rg -l -i 'anchor position' .        # or: grep -ril
ls ui-components ui-behaviors       # browse when unsure
```
2. **Read** the matching `.md` in full. Each guide = overview, decision rules, runnable HTML/CSS/JS, pitfalls, fallbacks.
3. **Apply**, then check the code against the guide's rules before answering.

## Categories

`accessibility` `built-in-ai` `css` `forms` `html` `js` `performance` `privacy` `pwa` `security` `ui-atoms` `ui-behaviors` `ui-components` `user-experience` `visual-design` `wasm` `webmcp`

Category `*.md` files (e.g. `css/css.md`, `forms/forms.md`) are the discipline overviews — read those first for broad tasks.

## Retrieval patterns

- "confirm before delete" → `ui-components/dialog.md`
- "tab bar sliding highlight" → `ui-behaviors/anchor-positioning-tab-underline.md`
- "card adapts to its own width" → `css/size-aware-styling.md` (container queries)
- "tooltip" → `ui-atoms/position-aware-tooltips.md`
- "INP is bad / long tasks" → `performance/identify-inp-causes.md`, `performance/break-up-long-tasks.md`
- "sanitize HTML" → `security/sanitize-untrusted-html.md`, `security/trusted-types.md`
- "passkey login" → `security/passkeys.md`

## Fallbacks

- Corpus missing → `git clone --depth 1 https://github.com/GoogleChrome/modern-web-guidance.git C:/Users/syahd/modern-web-guidance`
- Corpus stale → `git -C C:/Users/syahd/modern-web-guidance pull` (guides track new Baseline features)
- Need Google's own search ranking → `npx -y modern-web-guidance@latest search "<2-5 word query>"` then `retrieve "<id>"` (network required)

## Common mistakes

- Writing a JS click-outside/`Esc`/focus-trap handler instead of `<dialog>` + `showModal()` / Popover API.
- `IntersectionObserver` + transform math instead of scroll-driven animations (`animation-timeline: view()`).
- `window.matchMedia` JS instead of `prefers-color-scheme` / `light-dark()`.
- Hand-rolled dropdown positioning instead of CSS Anchor Positioning.
- Custom `<div role="dialog">`, `aria-modal`, manual focus management — the native element already supplies all three.
- Reaching for a library (popper, focus-trap, swiper) before checking whether the platform now covers it.
