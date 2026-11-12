# Sending from the user's Gmail via Playwright (browse)

Use when the agent must actually send mail and the `google-workspace` / `gws` path is unavailable (restricted Google Cloud project) or the account is only logged in interactively.

## Steps

1. Confirm the account: open `https://mail.google.com/mail/u/0/#inbox`, check `document.title` contains the expected address. Do not assume `/u/0` is the right account.
2. Target that tab explicitly (`--target-index` / `--target-url mail.google.com`). The compose tab is a separate page; a script run without a target drives the previously selected page and times out waiting for a Compose button that was never on it.
3. Open compose — either click the button (name is `Tulis` on Indonesian Gmail, `Compose` on English: match `/^(Tulis|Compose)$/`) or go straight to `https://mail.google.com/mail/u/0/#inbox?compose=new`.
4. Fill recipient, press Enter to commit the chip, then fill subject, then body.
5. Verify, send, verify again (below).

## Selectors that actually match

- Compose dialog: `div[role="dialog"]` last.
- Subject: `input[name="subjectbox"]`.
- Body: `div[contenteditable="true"][role="textbox"]` last.
- Send: `[role=button][aria-label^="Kirim"]` (or `^="Send"`). The full aria-label carries invisible bidi marks — `getByRole('button', { name: /^Kirim$/ })` never matches.

## Pitfalls

- **Recipient chip is not `inputValue()`.** Once a chip exists the text input is `size=0`, invisible, `aria-label="Kepada penerima"`. Filling it through a `*="Kepada"` selector times out on "element is not visible". Read recipients from `dialog [email]` attributes instead.
- **Autocomplete can commit the wrong address.** Always compare the chip's `email` attribute to the exact intended address after Enter. A dropped first letter is invisible on screen.
- **The caret lands above the signature.** Gmail prefills `-- Best Regard, <user>` and typing inserts before it, producing signature-then-body. Fix: focus body → `Ctrl+A` → `Delete` → type the whole body. Rewriting is cheaper than fighting the caret.
- **`keyboard.type()` of a full body overruns the 60s default.** Pass `--timeout-ms 180000`.
- **Send verification is two checks**: compose dialog count drops to 0 and a `/Pesan terkirim|Message sent/` toast appears; then open `/#sent` and confirm the subject via `getByText(subject).first().locator("xpath=ancestor::tr")`. The toast alone is not proof of delivery.
- **"Beberapa penerima menggunakan layanan yang tidak mendukung enkripsi"** is a normal external-recipient notice, not a failure.
- Gmail's signature block is untouched by the rewrite above only if the caret clear works; if the signature survives at the bottom it is the user's own sign-off and is fine to send.
