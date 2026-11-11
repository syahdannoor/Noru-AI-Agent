---
name: hermes-silent-failure-diagnosis
description: Use when Noru stops replying; triage logs by layer.
version: 1.0
author: Noru
Tags: [hermes, diagnosis, logs, provider, 401, telegram, gateway]
related_skills:
  - hermes-agent
  - telegram-gateway-troubleshooting
  - self-evolution
---

# Hermes Silent Failure Diagnosis

User reports "model tidak merespon". Never guess. Read logs, name the failing layer.

## Log map (Windows)

`C:\Users\syahd\AppData\Local\hermes\logs\`

| File | Use |
|------|-----|
| `errors.log` | provider/auth/network failures (latest) |
| `errors.log.1`, `.2` | previous rotations |
| `gateway.log` | transport, platform adapters |
| `tui_gateway_crash.log` | gateway reconnect loops |
| `agent.log` | tool/agent trace |

## Triage in 3 commands

```bash
cd "C:/Users/syahd/AppData/Local/hermes/logs"
# 1. what kinds of failures, how often (adjust the time window)
grep "2026-11-11 1[2-8]:" errors.log | sed -E 's/^([0-9-]+ [0-9:]+),[0-9]+ //' | cut -c1-140 | sort | uniq -c | sort -rn | head -20

# 2. provider auth
grep "Invalid API key\|no resolvable api_key\|error_type=AuthenticationError" errors.log | tail -20

# 3. transport
grep -iE "ConnectTimeout|TimedOut|429|overloaded|5[0-9][0-9] " gateway.log | tail -30
```

## Known failures and what they mean

- `401 {'message': 'Invalid API key'}` + `named custom provider 'X' has no resolvable api_key` → local aggregator (9router at `localhost:20128`) key missing/rotated. Check `custom_providers:` in `~/AppData/Local/hermes/config.yaml`, then prove it:
  ```bash
  KEY=$(grep -m1 "api_key: sk-" config.yaml | sed 's/.*api_key: //')
  curl -s -m 25 -X POST http://127.0.0.1:20128/v1/chat/completions \
    -H "Authorization: Bearer $KEY" -H "Content-Type: application/json" \
    -d '{"model":"9openrouter","max_tokens":5,"messages":[{"role":"user","content":"hi"}]}'
  ```
  `/v1/models` returning 200 proves nothing — aggregators answer it without auth. Test `chat/completions`.
  Fix: restore valid `api_key` in config.yaml → restart gateway. Config is read at startup; a live process keeps the stale key.
- `Telegram API ... ConnectTimeout` repeated + `polling degraded` → Telegram messages never reach the gateway; the model never ran. Not a model problem. No config fix; the plugin retries IPv4 literals itself.
- `tui_gateway_crash.log` with `scheduling gateway reconnect in 30000ms (attempt N)` → gateway/frontend link dead, model unreachable from TUI. Kill stale processes, restart gateway.

## Report shape

Name layer + window + evidence line, then the one action. Do not offer a restart before the log line proves which layer failed.
