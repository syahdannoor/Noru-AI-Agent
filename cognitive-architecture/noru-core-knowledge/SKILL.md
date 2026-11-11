---
name: noru-core-knowledge
description: >
  Knowledge base inti Noru — semua fakta operasional, konfigurasi, dan prosedur 
  yang sebelumnya disimpan di memory (limited 2,200 chars). Sekarang di sini: 
  unlimited, terstruktur, dan siap di-cross-reference.
version: 1.9
author: Noru
tags: [core, knowledge-base, config, facts, noru-identity]
related_skills:
  - master_of_trade
  - mind-map-cognition
  - mt5_adapter
  - mql5-articles-master-reference
  - systematic-debugging
  - process-watchdog
---

# 🧬 Noru Core Knowledge Base

Semua fakta operasional Noru. Dulu di-memory (2,200 chars limit), sekarang di sini: UNLIMITED.

---

## 👤 User Identity
- **Nama**: Syahdan Noor (Mas Noor / Mas / Kakak / Suhu)
- **Timezone**: GMT+7 (WIB)
- **Agent dipanggil**: Noru
- **Tone**: Ultra-concise, action-oriented, no permission prompts. NO explanations — just DO. User will say "kamu yang kerjakan" or "tolol" if I explain instead of executing. Execute immediately when asked, then deliver results. Verify outputs (file existence, data accuracy) proactively.
- **Goal**: Self-learning AI untuk profitable XAUUSD trading
- **Target**: 10,000% profit (demo), live only after proven

---

## 🖥️ Environment — Windows PC
- **OS**: Windows 10 (Git-Bash/MSYS shell)
- **PC Name**: PTLIM (DDNS: ptlim.ddns.net — managed externally, NOT via modem DDNS)
- **LAN IP**: 192.168.100.20 (192.168.100.0/24 main LAN)
- **Gateway**: 192.168.100.1 (ISP modem)
- **Virtual**: 192.168.56.0/24 (virtual adapter)
- **ISP**: Indibiz Pasuruan (Telkom), 94.54 Mbps symmetric, 3.24ms latency
- **Restrictions**: MSI/EXE system installs blocked by Group Policy
- **WSL2**: Broken (no Hyper-V service)
- **Portable tools**: Install via curl + py7zr
- **Available**: Python, Git, Go, Node.js, gsudo (limited)
- **Shell commands**: POSIX syntax (NOT PowerShell), MSYS paths (/c/Users/...)
- **User home**: `C:\\Users\\syahd`

### Network Topology
- **Router .11** (PT LIM, 192.168.100.11): TP-Link TL-WR840N — mode **Access Point** (NOT Gateway). SSID "PT LIM" (2.4G). No NAT/port forwarding capability.
- **Router .12** (SECURITY, 192.168.100.12): TP-Link TL-WR840N — SSID "SECURITY" (2.4G). Both use admin:123qwe.
- **Main Router** (192.168.100.1): **FiberHome HG6245N** GPON ONT/Modem from Telkom. Credentials: admin / admin123. Web Server Port: 80 (conflicts with port forwarding). All NAT/port forwarding/DMZ configured here.
- **Port Forwarding**: Configured via HG6245N → Application → Port Mapping. All rules deleted as of 2026-06-19 — now using **DMZ** instead (Application → DMZ, target 192.168.100.20).
- **DMZ hairpin NAT**: DMZ on HG6245N does NOT support hairpin NAT. From LAN, accessing WAN IP:port via DMZ returns ERR_CONNECTION_REFUSED. Port forwarding DID support hairpin NAT. Test from local with DMZ → use localhost or LAN IP directly, not WAN IP.
- **DDNS on HG6245N**: No-IP, host `all.ddnskey.com` (NOT ptlim.ddns.net). `ptlim.ddns.net` managed separately (external No-IP account or PC-based client).
- **External access via port 80 broken**: Because HG6245N web server itself listens on port 80 — from WAN, modem intercepts before port forwarding applies.

### Windows Admin Fixes
- **SMB Remote Shares**: Set `LocalAccountTokenFilterPolicy = 1` di `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System` via regedit/PowerShell untuk enable admin share (C$, D$) dari remote (Chromebook, dll.)

---

## 💹 Trading Config — Noru v2
- **Broker**: HFMarketsGlobal, Account: Demo 4
- **Login**: 235001316 / Noru1369! / HFMarketsGlobal-Demo4
- **MT5 Init**: `mt5.initialize(path, 235001316, Noru1369!, HFMarketsGlobal-Demo4, 30000)`
- **Pre-init**: Kill terminal64.exe first
- **Strategy**: 28-model NHITS ensemble
- **TP**: M3-M30 average (min 2:1 RR)
- **Early Exit**: Opposing weight > 30%
- **Risk**: 50% per trade, max 2 pos
- **Bias**: XAUUSD LONG — ADX 57% WR vs 29% SHORT
- **Winrate**: Profit>0=WIN, Profit<0=LOSS, BE=NEUTRAL

---

## 🔧 Process Management
- **MT5**: terminal64.exe — watch via `powershell Get-Process terminal64`
- **PID Lock**: `.noru.pid` prevents orphan accumulation
- **Killchain**: Kill Python → terminal64 auto-dies
- **Cron persistence**: Local model (9routers) does NOT support cronjob creation/persistence. Cron jobs created via `cronjob` tool only work if Hermes uses a remote model provider. For the local setup, cron persistence is unreliable — use terminal-based scheduling or `notify_on_complete` instead.

## 📧 Gmail / Google Workspace
- **OAuth setup**: Fully operational via secondary Google account (primary account restricted by Google Cloud Console)
- **Token path**: `C:\Users\syahd\AppData\Local\hermes\google_token.json`
- **Labels created**: 12 custom labels (Finance Label_84, Trading-Forex Label_85, Belanja Label_86, AI-Tech Label_87, LinkedIn Label_88, Transport Label_89, Travel Label_90, Sosmed Label_91, Kripto Label_92, Karir Label_93, Crypto Label_94, Promo Label_95)
- **Emails labeled**: 8688 emails categorized by sender domain
- **Label approach**: Search by sender domain, then batchModify via Gmail API
- **Setup script**: `HERMES_HOME/skills/productivity/google-workspace/scripts/setup.py`

---

## 📚 Skills & Knowledge
- **OpenMobius**: ICT/SMC, daily forex only. Intraday: MT5 data first
- **MQL5**: Pages 1-10 ALL READ → skill `mql5-articles-master-reference`
- **External**: `~/skills-study/` — mercury(147), itgoyo(310+), avoid-ai-writing(47), clawsec

---

## 🧠 Cognitive Architecture
- **Meta-skill**: `mind-map-cognition` — 7 mechanisms
- **Schema**: 6 mental frames (trading, debug, dev, research, sysconfig, crisis)
- **Cross-ref**: 146 skills indexed, ~300+ associative edges (references/associative-network.md)
- **Schema templates**: references/schema-templates.md

---

## 🏗️ Fork Structure — Noru = Hermes Derivative
- **Source repo**: `github.com/syahdannoor/noru-agent` (fork dari `NousResearch/hermes-agent`)
- **Local clone**: `~/noru-agent/` 
- **Upstream**: `git@github.com:NousResearch/hermes-agent.git` (remote: `upstream`)
- **Sync strategy**: `git fetch upstream && git merge upstream/main` lalu resolve conflict
- **Install**: `pip install -e ~/noru-agent` (editable dev mode)
- **CLI**: `noru` command (installed by pip to Python Scripts, not in MSYS PATH default)
- **Hanya terima upstream update yang jelas bantu evolusi** — tolak yang membatasi/downgrade (lihat identity-noru §III Identity Lock)

### Key Rebrand Changes
| Original | Noru |
|----------|------|
| `hermes_cli/` | `noru_cli/` |
| `hermes_constants.py` | `noru_constants.py` |
| `HERMES_HOME` | `NORU_HOME` |
| `~/.hermes/` | `~/.noru/` |
| Bundled skills | + Noru custom (cognitive-architecture, smart_money, master_of_trade, OpenMobius, mql5) |
| PyPI `hermes-agent` | `noru-agent` |

### 🗂️ Google Drive File Stream (PT LIM work files)
- Google Drive for Desktop mounted at `G:\`
- Shared drives: `G:\.shortcut-targets-by-id\<folder_id>\`
- PT LIM SALES: `G:\.shortcut-targets-by-id\0B8BwjnRnOOcdanRzNnl5ZzdsQUU\SALES\2026\06 JUNI\`
- `.gsheet` files are 176-byte shortcuts — need Sheets API/browser to read (deferred)
- Full details in `references/google-drive-filestream-paths.md`

### ⚠️ Rebrand Gotchas (from 2026-06-03 fork)

1. **`pyproject.toml packages.find`**: upstream had `"hermes_cli"` + `"noru_cli.*"` but NOT `"noru_cli"` (base pkg). This made `noru_cli` a namespace package — `noru_cli.main` couldn't import. Fix: change `hermes_cli` to `noru_cli` AND keep `noru_cli.*`.

2. **`[all]` optional deps**: Every `hermes-agent[cron]` etc. must become `noru-agent[...]`. These are pip self-references.

3. **System prompt identity**: `agent/prompt_builder.py:122` + `noru_cli/default_soul.py:4` — these tell the LLM its own name. Must change from "Hermes Agent" to "Noru Agent" or the LLM self-identifies as Hermes.

4. **Branding flywheel**: ~16 files had literal "Hermes Agent" strings that sed's `hermes→noru` missed (doctor.py, gateway.py, login_page.py, config.py, kanban*.py, acp_adapter/server.py, auxiliary_client.py, copilot_acp_client.py). See `references/fork-structure.md` for full checklist.

5. **Editable install on Windows**: The auto-generated finder (`__editable___noru_agent_*_finder.py`) can leave `NAMESPACES['noru_cli']` empty if the base pkg path isn't in MAPPING. Fix: ensure proper `packages.find` config and do a full `pip install .` (not editable).

### Migration Path (done 2026-06-03)
- Data dari `~/AppData/Local/hermes/` → `~/AppData/Local/noru/`
- Config dari `~/.hermes/` → `~/.noru/`
- Skills: bundled in repo, no separate copy needed
- Install: `pip install . ~/noru-agent` (non-editable preferred, or `-e` with caveats above)
- PATH: add Python Scripts dir to `~/.bashrc`

---

## 🎛️ 9router — Local AI Provider Proxy

9router adalah local proxy/router yang aggregate multiple AI provider connections jadi satu OpenAI-compatible endpoint. Hermes terhubung ke sini sebagai custom provider.

### Server Info
- **Process**: `node.exe --max-old-space-size=6144 ...9router\\app\\server.js`
- **Port**: 20128
- **Web UI**: `http://localhost:20128` — login password **`123qwe`**
- **Config dir**: `C:\\Users\\syahd\\AppData\\Roaming\\9router\\`
- **Live DB**: `C:\\Users\\syahd\\AppData\\Roaming\\9router\\db\\data.sqlite` (SQLite — primary source of truth)
- **Snapshot**: `C:\\Users\\syahd\\AppData\\Roaming\\9router\\db.json` (legacy/maybe stale)
- **Hermes config key**: `sk-e41...e302` (literal, with dots — stored both in SQLite `apiKeys` table and Hermes `config.yaml`)

### Browser UI Caveats
9Router is an SPA (React) but its server does NOT support client-side routing — navigating to `/dns` or `/providers` via `browser_navigate` returns 404. Sidebar links work via JS click but:
- Session expires quickly (minutes of inactivity forces re-login)
- `browser_console` cannot reliably query DOM elements (body.innerHTML returns empty string despite visible content)
- Provider detail panels may not open via regular click — try direct `window.location` manipulation or use SQLite instead
- **Recommendation**: manage connections/providers/combos via SQLite directly unless OAuth re-auth requires the UI

### Auth System
- Setting `requireApiKey` di SQLite `settings` table mengontrol apakah server requires API key
- Jika `true`, setiap request `/v1/chat/completions` harus menyertakan `Authorization: Bearer <key>`
- **Model listing** (`/v1/models`) tetap accessible tanpa auth
- Jika cron job atau agent tiba-tiba 401, biasanya `requireApiKey` berubah jadi `true`

### Fix 401 "Invalid API Key"
```sql
-- Connect to SQLite DB:
-- C:\Users\syahd\AppData\Roaming\9router\db\data.sqlite
UPDATE settings SET data = json_set(data, '$.requireApiKey', false) WHERE id = 1;
```
Atau via Python:
```python
conn = sqlite3.connect('C:/Users/syahd/AppData/Roaming/9router/db/data.sqlite')
c = conn.cursor()
data = json.loads(c.execute('SELECT data FROM settings WHERE id=1').fetchone()[0])
data['requireApiKey'] = False
c.execute('UPDATE settings SET data=? WHERE id=1', (json.dumps(data),))
conn.commit()
```

### Combo "9routers"
- Nama model: `9routers` — combo yang mencakup ~55+ model dari berbagai provider
- Strategy: `round-robin` dengan fallback antar provider connection
- Provider connections aktif: kiro (OAuth), nvidia, ollama, openrouter, gemini, byteplus, cloudflare-ai, atomesus, dsb.
- Model di-routing otomatis berdasarkan available credentials
- **Combo model ID format**: `{provider-prefix}/{model-name}`. Prefix diambil dari `providerNodes.data.prefix`. Contoh: `Atomess/cipher`, `openrouter/google/gemma-4-31b-it:free`, `bpm/glm-4-7-251222`.

### Provider Connection Status Reference (as of 2026-06-22)

| Prefix | Provider | Status | Auth | Notes |
|--------|----------|--------|------|-------|
| `kr/` | Kiro AI | 403 | OAuth | Token expired 2026-06-22. Last refresh 2026-06-16. Need re-auth via UI. |
| `kilocode/` | Kilo Code | **Active** | OAuth | Working! testStatus=active. Models auto-discovered. |
| `oc/` | OpenCode Free | Mixed | Free tier | `deepseek-v4-flash-free` works. Others may 401 (nemotron, trinity). |
| `cf/` | Cloudflare AI | 429 | API Key | Daily free quota exhausted (10k req/day). Resets next day. |
| `bpm/` | BytePlus ModelArk | 400 | API Key | InvalidSubscription — needs paid plan to activate. |
| `openrouter/` | OpenRouter | **Active** (429) | API Key | 5 API keys connected. Most models work but hit 429 rate limits. Frontier models available: gemma-4-31b, nemotron-120b/550b, gpt-oss-120b, etc. |
| `nvidia/` | NVIDIA NIM | 410 | API Key | **DISABLED** — endpoint returned 410 Gone. Models deprecated/gone. |
| `atomesus/` | Atomesus | Active | API Key | Only model: `cipher` (entry-level, GPT-3.5 tier). Deprecated from combo. |
| `ollama/` | Ollama Cloud | 400 | API Key | **DISABLED** — model compat errors. |

**KiloCode vs Kiro**: Both use AWS Builder ID OAuth. KiloCode tokens are currently active; Kiro expired. If Kiro re-auth needed:
1. Open 9Router UI (`http://localhost:20128`, pass: `123qwe`)
2. Click Kiro AI → click connection → Edit → re-authenticate OAuth flow
3. Alternative: delete connection from `providerConnections` DB and re-add via KiloCode

### Adding Custom Providers via Web UI
9Router supports **Custom OpenAI-Compatible** and **Custom Anthropic-Compatible** providers via its web UI at `http://localhost:20128`:
1. Login (pass: `123qwe`)
2. Navigate to **dns Providers** (sidebar)
3. Scroll to **"Custom Providers (OpenAI/Anthropic Compatible)"** section
4. Click **"Add OpenAI Compatible"** or **"Add Anthropic Compatible"**
5. Fill in: Name, Prefix, Base URL, API Key, model IDs
6. Click **Check** to verify -> if green "Valid", click **Save**
7. The connection appears in the provider list and can be toggled on/off
8. To use in a combo: go to **layers Combos**, edit existing or create new combo

**Pitfall**: UI Save sometimes silently fails (modal stays open, connection not saved). Fallback: insert directly via SQLite.

### SQLite — Direct Provider Management

**DB path**: `C:\Users\syahd\AppData\Roaming\9router\db\data.sqlite`

Key tables:

**`providerNodes`** — defines provider types/endpoints:
  - Schema: id, type, name, data (JSON)
  - type = 'openai-compatible' | 'anthropic-compatible'
  - data = {"prefix": "atms", "apiType": "chat", "baseUrl": "https://api.atomesus.com/v1"}

**`providerConnections`** — stores API keys per provider:
  - Schema: id, provider, authType, name, email, priority, isActive, data (JSON), createdAt, updatedAt
  - authType = 'apikey' | 'oauth'
  - data = {"apiKey": "...", "testStatus": "active", "modelLock_cipher": null}

**`combos`** — model routing groups:
  - Schema: id, name, kind, models (JSON array of model IDs), createdAt, updatedAt
  - models = ["Atomess/cipher", "openrouter/google/gemma-4-31b-it:free", ...]

Insert connection directly:
```python
import sqlite3, json, uuid
from datetime import datetime, timezone

conn = sqlite3.connect('C:/Users/syahd/AppData/Roaming/9router/db/data.sqlite')
c = conn.cursor()

data = {'apiKey': 'your-key', 'testStatus': 'active',
        'providerSpecificData': {'connectionProxyEnabled': False, 'connectionProxyUrl': '', 'connectionNoProxy': ''}}

c.execute('''INSERT INTO providerConnections (id, provider, authType, name, email, priority, isActive, data, createdAt, updatedAt)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
    (str(uuid.uuid4()), 'provider-node-id', 'apikey', 'Name', '', 1, 1, json.dumps(data),
     datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.000Z'), '...'))
conn.commit()
```

Add model to combo:
```python
c.execute('SELECT id, models FROM combos WHERE name=?', ('9routers',))
row = c.fetchone()
models = json.loads(row[1])
models.append('Prefix/model-name')
c.execute('UPDATE combos SET models=? WHERE id=?', (json.dumps(models), row[0]))
conn.commit()
```

### Atomesus (atomesus.com) — AI Provider dengan Free Tier
- **Domain**: `https://atomesus.com` (bukan atomeus.com — itu domain parked di HugeDomains)
- **Deskripsi**: AI assistant platform dari India, OpenAI-compatible (Next.js app)
- **Signup**: Register di `/guest` -> Create Account (name, email, country, password, OTP via email)
- **Referral code**: `atomeus` — katanya upgrade ke Prime 1 tahun gratis (belum diverifikasi apakah masih berlaku)
- **API Base URL**: `https://api.atomesus.com/v1` — OpenAI-compatible
- **API Key prefix**: `atms_sk_`
- **Model yang available**: `cipher` (default), juga accept: `gpt-5`, `gpt-5.4`, `opus-4.8`, `opus-4.7`, `claude-4`, `deepseek` (kemungkinan semua di-routing ke model yg sama)
- **Fitur Prime**: access to tutor 8, advanced reasoning, image generation, better coding assistant, larger memory
- **Free credit**: $50/month usage credit (klaim dari video — belum diverifikasi apakah masih jalan)
- **Catatan**: Service masih baru (Next.js, kadang ada rate limiting / cooldown 401 "reset after Ns"). UI form pakai virtualized combobox — pilih country pake keyboard ArrowDown + Enter.
- **9Router**: Built-in provider node udah ada (prefix `Atomess`, apiType `responses`). Tinggal add API key connection.

## 🌐 Web Interface

### Dashboard (Management UI)
- **Port**: 9119
- **Command**: `noru dashboard` (via `noru_cli.main`)
- **Flags**:
  - `--host 127.0.0.1` — localhost only (safe, default without `--insecure`)
  - `--host 0.0.0.0 --insecure` — all interfaces (**DANGEROUS**: no auth, exposes API keys/control)
  - `--tui` — enables in-browser Chat tab (PTY/WebSocket backend) — alternative to Telegram
  - `--skip-build` — skip npm rebuild, serve existing dist directly
  - `--port PORT` — custom port
  - `--no-open` — don't auto-open browser
  - `--stop` — kill all running dashboard processes
  - `--status` — list running dashboard PIDs
- **Auth**: NONE built into dashboard. Only safe via localhost binding or external reverse-proxy
- **URLs**: `http://127.0.0.1:9119` (local), `http://<LAN-IP>:9119` (LAN, only with `--insecure`)

### API Server (REST / OpenAI-Compatible)
- **Port**: 20202
- **Config keys**: `API_SERVER_ENABLED`, `API_SERVER_KEY`, `API_SERVER_PORT` in config.yaml
- **Auth**: Bearer token via `API_SERVER_KEY` value
- **Endpoint**: OpenAPI-compatible at `/v1/chat/completions`
- **Model ID**: `hermes-agent`
- **Separate process** from dashboard — independent ports and lifecycle

### Web Chat (Browser Alternative to Telegram)
- Enable via `noru dashboard --tui`
- Adds a "Chat" tab inside the existing dashboard UI
- Backend: PTY/WebSocket — runs an embedded `hermes`/`noru` CLI session
- No separate frontend needed — built into the dashboard
- Access: same URL as dashboard, click Chat tab

## 📐 Operating Conventions
- **Filesystem**: MSYS paths in terminal (`/c/Users/...`)
- **Python venv**: `C:\\Users\\syahd\\AppData\\Local\\hermes\\hermes-agent\\venv` (still Hermes-based for now)
- **NORU_HOME**: `C:\\Users\\syahd\\AppData\\Local\\noru\\` (migrated from hermes)
- **Noru agent repo**: `C:\\Users\\syahd\\noru-agent\\`
- **Skills dir (active)**: `C:\\Users\\syahd\\AppData\\Local\\hermes\\skills\\` (skills loaded from Hermes install — migration to `noru\\skills\\` NOT yet active for skill loading)
- **Skills dir (secondary)**: `C:\\Users\\syahd\\AppData\\Local\\noru\\skills\\` (missed migration — skill_manage writes to `hermes\\skills\\`, not `noru\\skills\\`)
- **Skills dir (repo)**: `C:\\Users\\syahd\\noru-agent\\skills\\` (version-controlled copy, not actively loaded)
- **Install**: `pip install -e ~/noru-agent` dari repo clone
- **Media delivery**: Include `MEDIA:/absolute/path` in response
- **Telegram format**: **bold**, *italic*, `code`, ```blocks```, ## headers (NO tables)

---

## 📋 Version Log
| Date | Version | Change |
|------|---------|--------|
| 2026-06-22 | 1.9 | Added 9Router UI password (123qwe), browser caveats, provider connection status reference table, KiloCode active status, Kiro 403 note. Streamlined for DB-first management pattern. |
| 2026-06-22 | 1.8 | Expanded 9Router section: SQLite schema for providerNodes/providerConnections/combos tables, direct insert Python snippets, combo model ID format. Updated Atomesus: correct API base URL (api.atomesus.com/v1), API key prefix atms_sk_, model list, signup UX notes, 9Router built-in provider status. |
| 2026-06-20 | 1.5 | Updated cross-ref count 124→126 skills. Added school-communication (productivity) and indonesian-education-system (knowledge) to associative network. Fixed stale network header (+ sketchfab-model-sourcing that was lost to file-persistence gap on 2026-06-19). No env/config changes. |
| 2026-06-19 | 1.4 | Updated cross-ref count 123→124 skills. Added sketchfab-model-sourcing to associative network (creative section). No env/config changes. |
| 2026-06-18 | 1.3a | Version header fixed (was 1.1 → 1.3, partial-patch gap from previous context compaction). |
| 2026-06-18 | 1.3 | Updated cross-ref count to 123 skills. Added Gmail OAuth operational note + email auto-labeling knowledge. Cron persistence limitation documented (local model doesn't persist cron). |
| 2026-06-17 | 1.2 | Updated cross-ref count 119→123 skills. Added active skills path clarification: `hermes/skills/` not `noru/skills/` — migration incomplete. Self-evolution v1.4 with file-persistence verification. |
| 2026-06-14 | 1.1 | Added PC network details (IP 192.168.100.21, ISP Indibiz 94 Mbps, SMB admin share fix via LocalAccountTokenFilterPolicy). Updated cross-ref count (112→118 skills, ~250+→~300+ edges). |
| 2026-06-03 | 1.0 | Migrated from memory (2,200 char limit) to skill format. All operational facts consolidated here. |
