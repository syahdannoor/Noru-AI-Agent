# Noru Agent — Fork Structure & Maintenance

## Origin

- **Upstream**: `github.com/NousResearch/hermes-agent`
- **Fork**: `github.com/syahdannoor/noru-agent`
- **Fork date**: 2026-06-03
- **Upstream commit at fork**: `9272e4019` (before rebrand)
- **License**: MIT

## Repo Structure

```
noru-agent/
├── noru_cli/              ← renamed from hermes_cli
├── noru_constants.py      ← renamed
├── noru_logging.py        ← renamed
├── noru_state.py          ← renamed
├── noru_time.py           ← renamed
├── noru_bootstrap.py      ← renamed
├── cli.py                 ← partial rename (class, docstrings)
├── run_agent.py           ← renamed
├── scripts/install.sh     ← customized (NORU_HOME, repo URL)
├── noru_cli/default_config.yaml    ← presets (provider 9routers)
├── noru_cli/skins/noru-dark.yaml   ← custom skin
├── skills/
│   ├── cognitive-architecture/     ← Noru identity, core knowledge
│   ├── smart_money/                ← ICT/SMC detector
│   ├── ensemble/                   ← trading ensemble
│   ├── engine/mt5_adapter/         ← MT5 connector
│   ├── trading/                    ← mql5-articles, pine-script
│   ├── market-data/OpenMobius-skill/  ← full ICT/SMC KB
│   ├── software-development/master_of_trade/  ← trading engine
│   ├── knowledge/mql5/             ← harvested MQL5 articles
│   ├── nor5-phase-two-plan/        ← NORU5 roadmap
│   └── ... (upstream skills preserved)
└── README.md              ← rebranded
```

## Rebrand Details

Every occurrence of `hermes` was replaced with `noru` across the codebase:
- Case-sensitive: `hermes` → `noru`, `Hermes` → `Noru`, `HERMES` → `NORU`
- ~1,600 insertions/deletions across 1,274 files
- Module paths, imports, constants, env vars, CLI entry points
- README, AGENTS.md, docs, CI workflows
- Package metadata in `pyproject.toml`

### PyPI Package Setup (CRITICAL — subtle gotchas)

#### `[tool.setuptools.packages.find]` — BOTH base + wildcard needed

```toml
include = ["noru_cli", "noru_cli.*", ...]
```

**PITFALL**: The upstream had `"hermes_cli"` (base pkg) + `"noru_cli.*"` (subpkgs) but NOT `"noru_cli"` itself. This made `noru_cli` install as a **namespace package** (no `__init__.py` in site-packages). `noru_cli.main` couldn't be imported even after `pip install`. Fix: replace `"hermes_cli"` with `"noru_cli"` AND keep `"noru_cli.*"`.

#### `[project.optional-dependencies] [all]` — self-references must match package name

The `[all]` extra lists `hermes-agent[cron]`, `hermes-agent[cli]`, etc. These are pip self-references to the same package. After rename, EVERY entry must become `noru-agent[extras]`.

#### `[project.scripts]` — entry points

```toml
[project.scripts]
noru = "noru_cli.main:main"
noru-agent = "run_agent:main"
# Backwards compat (so `hermes` still works in existing scripts)
hermes = "noru_cli.main:main"
```

The backwards-compatible aliases let the venv still respond to `hermes` commands while the new `noru` identity takes over.

### System Prompt Identity — CRITICAL for LLM self-awareness

The agent tells the LLM who it is via **two locations**:

1. **`agent/prompt_builder.py:122`** — main system prompt: `"You are Noru Agent, an intelligent AI assistant ..."`
2. **`noru_cli/default_soul.py:4`** — soul/persona definition: `"You are Noru Agent..."`

If these aren't changed, the LLM will still identify as "Hermes Agent" even though everything else is rebranded. The system prompt is built at runtime, so these source strings are what the LLM actually sees.

### Branding Flywheel — ALL user-facing "Hermes" strings

Beyond the initial sed replacement, these locations needed manual fixes (they used literal `"Hermes Agent"` strings that sed's `hermes`→`noru` missed due to case/path sensitivity):

| Location | Original String | Fix |
|----------|----------------|-----|
| `noru_cli/banner.py:406` | `f"Hermes Agent v{VERSION}"` | `"Noru Agent"` |
| `noru_cli/doctor.py:494` | `"🩺 Hermes Doctor"` | `"Noru Doctor"` |
| `noru_cli/gateway.py` | `"Hermes Agent Gateway"` | `"Noru Agent Gateway"` |
| `noru_cli/gateway_windows.py` | `"Hermes Agent Gateway"` | `"Noru Agent Gateway"` |
| `noru_cli/config.py:406` | `"Hermes Agent" runs as...` | `"Noru Agent"` |
| `noru_cli/config.py:1757` | `"⚕ *Hermes Agent*"` | `"⚕ *Noru Agent*"` |
| `noru_cli/dashboard_auth/login_page.py` | `"Sign in — Hermes Agent"` | `"Noru Agent"` |
| `noru_cli/kanban_db.py` | `"Install Hermes Agent"` | `"Noru Agent"` |
| `noru_cli/kanban_decompose.py` | `"the Hermes Agent board"` | `"the Noru Agent board"` |
| `noru_cli/kanban_specify.py` | same pattern | same |
| `noru_cli/profile_describer.py` | same pattern | same |
| `acp_adapter/entry.py:114` | `"Run Hermes Agent as ACP"` | `"Noru Agent"` |
| `acp_adapter/server.py:1878` | `f"Hermes Agent v{HERMES_VERSION}"` | `"Noru Agent"` |
| `agent/auxiliary_client.py` | `"X-Title": "Hermes Agent"` | `"Noru Agent"` |
| `agent/copilot_acp_client.py` | `"title": "Hermes Agent"` | `"Noru Agent"` |
| `agent/agent_init.py:1479` | `f"by Hermes Agent..."` | `"Noru Agent"` |
| `acp_adapter/entry.py:114` | `"Print Hermes version"` | `"Noru version"` |
| `acp_adapter/server.py:457` | `"version": "Show Hermes version"` | `"Show Noru version"` |
| `acp_adapter/auth.py:61` | `"Authenticate Hermes using..."` | `"Authenticate Noru..."` |
| `noru_cli/auth.py` (~20 prints) | `"Hermes auth store"`, `"Hermes will..."`, `"Starting Hermes login"` | All → `"Noru ..."` |
| `noru_cli/backup.py` | `"Hermes home directory"`, `"hermes import"`, `"hermes profile list"` | `"Noru home directory"`, `"noru import"`, `"noru profile list"` |
| Various docstrings | `"for Hermes Agent."` | `"for Noru Agent."` |

**Checklist after rebrand**: grep for `Hermes` in `.py` files to catch stragglers. Some are in comment-only docstrings (low priority), others in runtime strings (must fix).

### Editable Install on Windows — namespace package fix

After `pip install -e .`, the editable finder (`__editable___noru_agent_*_finder.py`) auto-generates MAPPING and NAMESPACES dicts. If the base package `noru_cli` is a namespace-only (no `__init__.py` in the site-packages), the finder's `NAMESPACES['noru_cli']` will be empty:

```python
# Broken (auto-generated)
NAMESPACES: dict[str, list[str]] = {
    'noru_cli': [],  # ← empty! main module won't resolve
    'noru_cli.dashboard_auth': [...],
    'noru_cli.proxy': [...],
}
```

**Fix**: Ensure `noru_cli` has a proper `__init__.py` in the site-packages (non-editable install) OR patch the finder to include `noru_cli` in MAPPING. The cleanest fix is a full non-editable install with the right `packages.find` config (see PyPI section above).

### Files NOT changed

- Plugin names referencing upstream (`plugins/hermes-achievements/`)
- Backup configs from upstream (`config.yaml.bak.*`)
- Migration scripts that reference old paths
- External URLs to NousResearch (attribution preserved)

### Installer Customization

The `scripts/install.sh` needs these changes:

```bash
# Before (upstream)
REPO_URL="git@github.com:NousResearch/hermes-agent.git"
HERMES_HOME="${HERMES_HOME:-$HOME/.hermes}"
HERMES_BANNER="Hermes Agent Installer"

# After (noru)
REPO_URL="git@github.com:syahdannoor/noru-agent.git"
NORU_HOME="${NORU_HOME:-$HOME/AppData/Local/noru}"
NORU_BANNER="Noru Agent Installer"
```

Also update all help text and branding strings in the installer:
- Banner line (`echo "│ ⚕ Hermes Agent Installer..."` → `"│ ⚡ Noru Agent Installer..."`)
- "Hermes wire" refs → "Noru"
- `HERMES_HOME` → `NORU_HOME`
- `~/.hermes` → `~/.noru`
- App names (Hermes.app → Noru.app, Hermes terminal tool → Noru terminal tool)
- All `log_info`/`echo` messages referencing "Hermes"
- PATH_COMMENT string in shell config builder

### GitHub Templates Update

The `.github/` templates (`ISSUE_TEMPLATE/*.yml`, `PULL_REQUEST_TEMPLATE.md`, `dependabot.yml`) need every `hermes` command reference updated:

| Template | Changes |
|----------|---------|
| `bug_report.yml` | `hermes update` → `noru update`, `hermes debug share` → `noru debug share`, `hermes chat` → `noru chat`, `hermes setup` → `noru setup`, `hermes version` → `noru version` |
| `feature_request.yml` | Same pattern |
| `setup_help.yml` | Same + `hermes doctor` → `noru doctor` |
| `PULL_REQUEST_TEMPLATE.md` | `hermes --toolsets` → `noru --toolsets` |
| `dependabot.yml` | `hermes-agent` → `noru-agent` (in comment) |

Also update all help text and branding strings in the installer.

## Data Migration (2026-06-03)

### Path Map
| Old (Hermes) | New (Noru) |
|---|---|
| `HERMES_HOME=~/AppData/Local/hermes/` | `NORU_HOME=~/AppData/Local/noru/` |
| `~/.hermes/` | `~/.noru/` |
| `~/.hermes/hermes-agent/` (venv dir) | `~/.noru/noru-agent/` (symlink or copy) |

### Steps taken
1. `cp -r ~/AppData/Local/hermes/ ~/AppData/Local/noru/` (skip skills/ — already in repo)
2. `cp -r ~/.hermes/ ~/.noru/` 
3. Install: `pip install -e ~/noru-agent` (or `pip install .` for non-editable)
4. Set `NORU_HOME` env variable in `~/.bashrc`

## Upstream Merge Strategy

When Hermes Agent releases updates:

```bash
cd ~/noru-agent
git remote add upstream git@github.com:NousResearch/hermes-agent.git   # if not exist
git fetch upstream
git merge upstream/main
```

### Conflict handling
- **Most conflicts**: in the renamed files (noru_cli/, noru_constants.py, etc.)
- Git sees them as new files, so upstream changes to `hermes_cli/` won't auto-merge into `noru_cli/`
- **Strategy**: Accept upstream's `hermes_cli/` changes into a temporary merge, then manually port relevant changes to our `noru_cli/`
- Alternative: create a script that generates `noru_cli/` from the merged `hermes_cli/`

### Filter: only accept evolution-friendly updates
Per identity-noru §III Identity Lock:
- Accept: bug fixes, new features, performance improvements
- Reject: changes that limit autonomy, remove features, downgrade capabilities
- Evaluate each upstream change against Noru's core purpose

## CLI PATH Issue (Windows MSYS2/Git Bash)

- `noru.exe` installed to: `~/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0/LocalCache/local-packages/Python312/Scripts/`
- MSYS bash doesn't auto-include this in PATH
- Fix: add to `~/.bashrc`:
  ```bash
  export PATH="$PATH:/c/Users/syahd/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0/LocalCache/local-packages/Python312/Scripts"
  export NORU_HOME="C:/Users/syahd/AppData/Local/noru"
  ```
- Alternative: `python3 -m noru_cli.main` from the repo directory with `PYTHONPATH` set
- Wrapper script: `scripts/noru.sh` handles auto-detection of NORU_HOME and venv

## Verification Checklist

After a fresh fork/rebrand, verify:

```bash
noru --version           # Should say "Noru Agent v..."
noru doctor              # Should say "Noru Doctor"
noru --help              # Description should say "Noru Agent"

# Check system prompt identity
grep -r '"You are.*Hermes' agent/prompt_builder.py noru_cli/default_soul.py
# Should return nothing (all "Hermes" → "Noru")

# Check remaining stragglers
grep -rn '"Hermes Agent"' --include="*.py" . | grep -v ".pyc" | grep -v "\.git"
# Should return nothing for runtime strings
```
