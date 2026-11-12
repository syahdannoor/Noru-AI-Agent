---
name: user-chrome-automation
description: Use when driving the user's own Chrome via browse CLI.
version: 1.0.0
author: Noru
license: MIT
metadata:
  hermes:
    tags: [browser, chrome, playwright, gmail, forms]
    related_skills: [google-workspace, tinyfish-browser, blocked-page-recovery]
---

# Driving the user's own Chrome (opencode `browse`)

`browse` attaches to the user's real Chrome through an extension: their cookies, logins, WhatsApp Web, Gmail session and tabs all apply. Use it when the task needs the user's authenticated browser or the user says "pakai Chrome saya". For anonymous scraping use plain fetch/first-party browser instead.

## When to Use

- The task needs the user's logged-in session (Gmail send, SaaS dashboards, operator/booking sites).
- The user asks to "pakai Chrome saya" / "pakai opencode browser".
- A site renders only after JS and a headless fetch returns nothing useful.
- You must send mail and `gws` / Google API access is restricted.

Do NOT use for anonymous reading — plain `web_extract` is cheaper.

## Install and verify (once per machine)

```bash
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "irm https://opencode.ai/browse/install.ps1 | iex"
```

Installs `~/.local/bin/browse.exe`, adds the MCP server to `~/AppData/Local/hermes/config.yaml`, launches Chrome to pair the extension. Read the served `install.ps1` before piping it to `iex` — it verifies downloads against the npm registry / release-manifest checksums, so a mismatch means stop.

Verify with two calls, not with the installer's own output:

```bash
"$USERPROFILE/.local/bin/browse.exe" status          # Extension: connected, Relay reachable
"$USERPROFILE/.local/bin/browse.exe" execute --rm 'await page.goto("https://example.com"); return await page.title()'
```

MCP tools (`browse_*`) only load after a session restart; the CLI covers the same surface, so never block or restart just for MCP.

## Core loop

Inspect → act → verify. Every `execute` is a fresh JS realm: no variables survive between calls (use `state` for continuity). There is no `ctx` — the injected globals are `page`, `context`, `browser`, `state`, `files`, plus helpers `snapshot()`, `ref()`, `fillInput()`, `handoff()`, `screenshotWithLabels()`.

```bash
browse execute --rm --file ./step.js --json          # one-shot
browse execute --session shop --file ./step.js       # sticky page across calls
browse execute --target-url mail.google.com 'return page.url()'   # act on a specific existing tab
```

- Put multi-line JS in a file and pass `--file`. Inlining in bash single quotes breaks on apostrophes, and `--json` output mixes the JSON envelope with a trailing `browse:` stderr line, so parse the JSON block only rather than the whole stream.
- `page` is the SELECTED tab (default: the session's), not the newest tab you opened. After opening another tab in an earlier call, target it explicitly with `--target-index N` / `--target-url` (`browse status` lists the indices) or the next script silently drives the old page.
- `--timeout-ms` defaults to 60000. Long `keyboard.type()` bodies and slow SPAs exceed it and the error surfaces as a misleading locator timeout — raise it to 120000-180000 for form fills.
- `--session <name>` keeps a half-filled form alive across calls; start a new session per site rather than one global session.

## Reading a page before acting

One call should return enough to plan the whole flow: `url`, `title`, headings, every input's `type/name/placeholder/value`, buttons, and a sliced `body.innerText`. Most forms have no `label[for]`, so resolve labels by walking ancestors and taking the nearest preceding label text.

Vision is for layout only. Do not read exact field values, addresses, or recipients off a screenshot — it misreads small UI text. Confirm those from DOM (`[email]` attributes, `inputValue()`, `innerText`).

## Money and commitments — hard gates

Stop before any step that moves money or creates a real obligation on a third party: payment buttons, "Pay now", final submit to a vendor, booking confirmation. Fill through to the review step, screenshot it, report the exact values, and ask.

- Never type card numbers, CVC, OTP, or passwords. Credential and payment entry is the user's; if the flow needs it, hand off offline.
- Forms demanding a passport/ID/national number: put an explicit marker (`TEST-BOOKING-NO-PASSPORT`), never a plausible fabricated number, and say so in the report.
- "Test booking" authorises the walkthrough, not the charge. Continuing past the gate needs a fresh, specific instruction for that action.
- Report the downstream cost explicitly (amount, currency, who receives it) so the user can decide.

## Reporting

Terse, Indonesian or English to match. List `field: value` for everything filled, state exactly where the flow stopped and why, name the one missing option, then one question that unblocks it. Attach the review screenshot as `MEDIA:`.

## References

- `references/gmail-compose-playwright.md` — sending mail from the user's logged-in Gmail when the `gws` CLI is unavailable or restricted.
