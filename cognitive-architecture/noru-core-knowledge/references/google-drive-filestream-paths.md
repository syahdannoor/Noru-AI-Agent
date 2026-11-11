# Google Drive for Desktop — File System Access (PT LIM)

## Mount Points
- **G:\** — Google Drive for Desktop mount (personal My Drive + shared drives)
- **H:\** — Secondary Google account mount (if any)

## Shared Drive Path Navigation
Google Drive for Desktop shortcuts live under:
```
G:\.shortcut-targets-by-id\<folder_id>\
```

### PT LIM Shared Drive
- **Folder ID**: `0B8BwjnRnOOcdanRzNnl5ZzdsQUU`
- **Full path**: `G:\.shortcut-targets-by-id\0B8BwjnRnOOcdanRzNnl5ZzdsQUU\`

### SALES Directory Structure
```
\SALES\
  \2026\
    \06 JUNI\
      ⏳ $ 02 13062026 _ KM. JALA SUTERA - V ( TA BENG ) VIA KM. MAJU BERSAMA JAYA - II.gsheet
      ⏳ $ 03 15062026 _ KM. JALA SUTERA - V ( TA BENG ) VIA KM. MAJU BERSAMA JAYA - II.gsheet
      ... (similar files per date)
```

## File Types
- **.gsheet** — Google Sheets shortcut (176 bytes binary). NOT directly readable via filesystem.
  - Content requires: Google Sheets API (OAuth), or browser-based access.
- **Non-Google files** (.pdf, .xlsx, .csv, .jpg, .txt) — fully readable via filesystem.
- **.gdoc**, **.gslides**, **.gdraw** — Similar shortcuts; require API/browser.

## Terminal Access (MSYS/Git-Bash)
```
cd /g/.shortcut-targets-by-id/0B8BwjnRnOOcdanRzNnl5ZzdsQUU/SALES/2026/06\ JUNI/
ls -la
```

## Limitations
- .gsheet files cannot be read with Python's `open()` — they're just shortcut markers.
- Google Drive OAuth setup is required for actual Sheets content.
- Chrome browser tool also fails on this system ("out of resources" error).
- Google Workspace API setup is deferred by user — prefers doing it when at the server/laptop directly.
