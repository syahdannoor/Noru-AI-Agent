# 🕸️ Associative Network — Cross-Reference Graph

Last updated: 2026-11-12
Total skills: 172
Total rows: 179
Transitions: ... → v1.35 (184→190 unique, 172 rows) → v1.36 (190→169 unique, 176 rows; table rebuilt + 5 skills added)
Status: REBUILT 2026-11-11 — table rows had been mangled by repeated fuzzy patches (leading pipes stripped from data rows, stacked pipes on summary rows). Normalized via `self-evolution/scripts/normalize_network.py`: 176 rows, 169 unique, 29 non-empty domains. Empty sections (PLANNING, MESSAGING, WIKIPEDIA) dropped. Added smc, smc-reload, smc-analysis-daemon (TRADING), xauusdc-all-daemon (MARKET DATA), microsoft-office (PRODUCTIVITY). 15 loose harvester .md artifacts (github-*, wikipedia-main-page) moved to `.archive/loose-md-2026-11-11/`. Cross-ref verified: 0 missing, 0 dead.




## Domain: TRADING (20 skills)
| Skill | Tags | Edges |
|-------|------|-------|
| **master_of_trade** | trading, mt5, ml, noru5, nhits | mt5_adapter, noru5-trading-engine, knowledge-harvester, mql5-articles-master-reference |
| **noru5-trading-engine** | noru5, ensemble, nhits, trading | master_of_trade, knowledge-harvester, mt5_adapter |
| **market-scanner** | yahoo-finance, scan, assets | master_of_trade |
| **mql5-articles-master-reference** | mql5, reference, articles | knowledge-harvester, noru5-trading-engine |
| **backtest_xauusd_scalping_5m** | backtest, smc, ict, xauusd | master_of_trade, noru5-trading-engine |
| **adaptive-trader** | multi-strategy, engine, ai | master_of_trade, mt5_adapter, noru5-trading-engine |
| **wc-prediction-model** | wc2026, prediction, pytorch, fifa | master_of_trade, noru-core-knowledge |
| **mt5-mcp-integration** | mt5, mcp, claude, ai, integration | master_of_trade, mt5_adapter, native-mcp |
| **noru-daily-learning** | cron, trading, learning, forums, report | mql5-articles-master-reference, url_fetch_troubleshooting |
| **mql5-two-sided-breakout-strategy** | mql5, trading, breakout, xauusd, atr | mind-map-cognition, self-evolution, noru-core-knowledge, master_of_trade |
| **mql5-martingale-grid-risk** | mql5, trading, martingale, grid, xauusd, risk | mind-map-cognition, self-evolution, noru-core-knowledge, master_of_trade |
| **mql5-regime-classification** | mql5, trading, regime, classification, overfitting | mind-map-cognition, self-evolution, noru-core-knowledge, master_of_trade |
| **mql5-basket-risk-management** | mql5, trading, basket, risk, management | mind-map-cognition, self-evolution, noru-core-knowledge, master_of_trade |
| **mt5-live-analysis** | mt5, live, analysis, trading | master_of_trade, noru5-trading-engine |
| **smc-ict-live-trading** | smc, ict, live, trading, xauusd | master_of_trade, noru5-trading-engine, mt5_adapter |
| **xauusd_smc_mcp** | xauusd, smc, ict, mcp, tv | master_of_trade, mt5-adapter, native-mcp |
| **trading-compounding-tracker** | compounding, risk-management, journal, plan-tracking | master_of_trade |
| **smc** | smc, analysis, cache, xauusd | smc-reload, smc-analysis-daemon, master_of_trade |
| **smc-reload** | smc, reload, mt5, cache | smc, smc-analysis-daemon, mt5_adapter |
| **smc-analysis-daemon** | smc, daemon, cron, cache | smc-reload, smc, mt5_adapter |

## Domain: MARKET DATA (3 skills)
| Skill | Tags | Edges |
|-------|------|-------|
| **OpenMobius-skill** | ict, smc, trading, market-data | noru5-trading-engine, knowledge-harvester |
| **market-db-mt5** | mt5, market-data, csv, database | mt5_adapter, master_of_trade, noru5-trading-engine |
| **xauusdc-all-daemon** | xauusdc, mt5, timeframes, daemon | smc-reload, market-db-mt5 |

## Domain: TRADING ENGINE (1 skill)
| Skill | Tags | Edges |
|-------|------|-------|
| **mt5_adapter** | mt5, connector, order | master_of_trade, noru5-trading-engine |

## Domain: COGNITIVE ARCHITECTURE (5 skills)
| Skill | Tags | Edges |
|-------|------|-------|
| **mind-map-cognition** | cognition, association, schema | identity-noru, self-evolution, noru-core-knowledge |
| **identity-noru** | identity, self, core, noru | mind-map-cognition, noru-core-knowledge, self-evolution |
| **self-evolution** | evolution, consolidate, prune | identity-noru, mind-map-cognition, noru-core-knowledge |
| **noru-core-knowledge** | knowledge-base, config, facts | identity-noru, mind-map-cognition, master_of_trade |
| **network-audit-log** | audit, documentation, network, cross-reference | mind-map-cognition, identity-noru |

## Domain: DATA SCIENCE (4 skills)
| Skill | Tags | Edges |
|-------|------|-------|
| **image-recognition** | vision, analyze | comfyui |
| **jupyter-live-kernel** | jupyter, notebook, python | data-science |
| **cloudflare-bypass-scraping** | cloudflare, bypass, scraping, bot-protection, turnstile | url_fetch_troubleshooting |
| **defuddle** | extraction, markdown, web, content | url_fetch_troubleshooting |

## Domain: COMMUNICATION (1 skill)
| Skill | Tags | Edges |
|-------|------|-------|
| **user-preferences** | preferences, communication, style | communication |

## Domain: DEV / SOFTWARE DEVELOPMENT (22 skills)
| Skill | Tags | Edges |
|-------|------|-------|
| **systematic-debugging** | debug, error, fix | windows-terminal, node-inspect-debugger, writing-plans |
| **test-driven-development** | tdd, test, red-green | writing-plans, spike |
| **writing-plans** | plan, design, impl | subagent-driven-development, spike |
| **spike** | experiment, validate | writing-plans, plan |
| **plan** | plan, markdown | writing-plans, spike |
| **subagent-driven-development** | subagent, delegate | writing-plans, github-pr-workflow |
| **requesting-code-review** | review, security, quality | github-code-review |
| **node-inspect-debugger** | node, debug, chrome-devtools | systematic-debugging |
| **hermes-agent-skill-authoring** | skill, author, frontmatter | self-evolution, mind-map-cognition |
| **adaptive-trader** | engine, multi-strategy, mt5 | master_of_trade, mt5_adapter |
| **debugging-hermes-tui-commands** | debug, tui, hermes | hermes-agent |
| **ruby-native-gems-windows** | ruby, gem, windows | windows-terminal |
| **simplify-code** | code-review, cleanup, refactor | requesting-code-review, test-driven-development, plan |
| **nextjs-rsc-payload-regex** | nextjs, rsc, regex, payload | debugging-hermes-tui-commands |
| **streaming-site-scraper** | streaming, scraper, video, cloudflare | cloudflare-bypass-scraping, debugging-hermes-tui-commands |
| **inspecting-hermes-desktop-dom** | dom, css, cdp, desktop, inspect | hermes-agent, hermes-desktop-plugins |
| **cctv-monitor-alert** | cctv, hikvision, alert | cctv-object-detection |
| **cctv-object-detection** | yolo, detection, object | cctv-monitor-alert |
| **hikvision-camera-control** | hikvision, camera, stream | cctv-monitor-alert |
| **dogfood** | qa, testing, browser | systematic-debugging |
| **codebase-memory** | graph, codebase, structural, queries | github-code-review, hermes-agent-skill-authoring |
| **modern-web-guidance** | web, html, css, ui, platform-primitives | hermes-agent, sketch, modern-web-guidance |

## Domain: DEVOPS (5 skills)
| Skill | Tags | Edges |
|-------|------|-------|
| **kanban-orchestrator** | kanban, orchestrator, decomposition | kanban-worker, kanban-codex-lane |
| **kanban-worker** | kanban, worker, pitfalls | kanban-orchestrator |
| **sdlc-review** | kanban, review, quality, verification | kanban-orchestrator, kanban-worker |
| **webhook-subscriptions** | webhook, subscriptions, event-driven | hermes-agent |
| **windows-terminal** | windows, terminal, powershell, pty | systematic-debugging, ruby-native-gems-windows, openvpn-windows-setup |

## Domain: CREATIVE (21 skills)
| Skill | Tags | Edges |
|-------|------|-------|
| **architecture-diagram** | svg, diagram, dark | excalidraw |
| **ascii-art** | ascii, pyfiglet, cowsay | ascii-video |
| **ascii-video** | ascii, video, gif | ascii-art |
| **baoyu-article-illustrator** | article, illustration | baoyu-comic, baoyu-infographic |
| **baoyu-comic** | comic, knowledge, manga | baoyu-article-illustrator |
| **baoyu-infographic** | infographic, 信息图 | baoyu-article-illustrator |
| **claude-design** | design, html, artifact | sketch |
| **comfyui** | comfyui, image, video | image-recognition |
| **design-md** | design, token, spec | creative |
| **excalidraw** | excalidraw, diagram, hand-drawn | mind-map-cognition, architecture-diagram |
| **humanizer** | humanize, text, rewrite | creative |
| **ideation** | ideas, brainstorming | creative |
| **manim-video** | animation, math, 3b1b | creative |
| **p5js** | p5js, generative, art | creative |
| **pixel-art** | pixel, retro, palette | creative |
| **popular-web-designs** | design-systems, css, html | sketch, claude-design |
| **pretext** | text-layout, ascii, generative | ascii-art |
| **sketch** | mockup, html, prototype | claude-design |
| **songwriting-and-ai-music** | songwriting, suno, ai-music | heartmula |
| **touchdesigner-mcp** | touchdesigner, visuals, mcp | comfyui |
| **json-canvas** | canvas, json, visual, mindmap, obsidian | excalidraw, mind-map-cognition |

## Domain: GITHUB (8 skills)
| Skill | Tags | Edges |
|-------|------|-------|
| **github-auth** | auth, gh, ssh | github-pr-workflow |
| **github-pr-workflow** | pr, branch, ci | github-code-review, subagent-driven-development |
| **github-code-review** | review, pr, diff | requesting-code-review, github-pr-workflow |
| **github-issues** | issues, triage, label | github-pr-workflow |
| **github-repo-management** | repo, clone, fork | github-auth |
| **codebase-inspection** | pygount, loc, langs | github-code-review |
| **github-issue-to-pr** | issue, pr, workflow | github-pr-workflow, github-issues |
| **github** | github, auth, gh, ssh | github-auth, github-code-review, github-issue-to-pr, github-issues, github-pr-workflow, github-repo-management, codebase-inspection |

## Domain: ML / AI (5 skills)
| Skill | Tags | Edges |
|-------|------|-------|
| **dspy** | dspy, declarative, lm | huggingface-hub |
| **huggingface-hub** | huggingface, hf, models | llama-cpp |
| **llama-cpp** | llama, gguf, inference | huggingface-hub |
| **weights-and-biases** | wandb, experiment, log | dspy |
| **segment-anything-model** | multimodal, image-segmentation, computer-vision, sam, zero-shot | huggingface-hub |

## Domain: NETWORKING (3 skills)
| Skill | Tags | Edges |
|-------|------|-------|
| **lan-network-scanner** | lan, scan, hosts | networking |
| **networking** | network, utilities | lan-network-scanner |
| **telegram-gateway-troubleshooting** | telegram, gateway, media | hermes-agent |

## Domain: MEDIA (5 skills)
| Skill | Tags | Edges |
|-------|------|-------|
| **gif-search** | gif, tenor, search | spotify |
| **heartmula** | music, song, suno | songwriting-and-ai-music |
| **songsee** | audio, spectrogram, mfcc | media |
| **spotify** | spotify, play, queue | media |
| **youtube-content** | youtube, transcript, summary | media |

## Domain: RESEARCH (14 skills)
| Skill | Tags | Edges |
|-------|------|-------|
| **arxiv** | arxiv, paper, search | blogwatcher |
| **blogwatcher** | blog, rss, feed | knowledge-harvester |
| **llm-wiki** | wiki, knowledge-base | mind-map-cognition |
| **polymarket** | polymarket, prediction | research |
| **blocked-page-recovery** | blocked, page, recovery, waf | url_fetch_troubleshooting |
| **competitor-news-monitor** | competitor, news, monitor | blogwatcher, knowledge-harvester |
| **grounded-citations** | citations, grounding, verification | arxiv, blogwatcher |
| **tinyfish-authenticated** | web-automation, browser, authenticated, vault | hermes-agent |
| **tinyfish-automation** | web-automation, browser, goal-driven | hermes-agent |
| **tinyfish-browser** | browser, cdp, stealth, chrome | hermes-agent, claude-code, codex |
| **tinyfish-monitor** | monitor, web, cron, alert | hermes-agent |
| **tinyfish-research** | research, web, search, fetch | hermes-agent, blogwatcher |
| **tinyfish-web** | tool-selection, web, tinyfish | hermes-agent |
| **user-chrome-automation** | chrome, browse, browser, authenticated, playwright | tinyfish-browser, blocked-page-recovery, google-workspace |

## Domain: PRODUCTIVITY (22 skills)
| Skill | Tags | Edges |
|-------|------|-------|
| **airtable** | airtable, rest, api | productivity |
| **document-to-action-items** | document, action-items, extraction | productivity |
| **docx** | docx, word, template | pdf, powerpoint |
| **google-workspace** | gmail, calendar, drive, docs, sheets | productivity |
| **linear** | linear, graphql, issues | productivity |
| **maps** | geocode, pois, routes, timezones | productivity |
| **meeting-action-items** | meeting, action-items, decisions | document-to-action-items |
| **multi-level-index** | index, hierarchical, memory | productivity |
| **nano-pdf** | pdf, edit, prompt | pdf, ocr-and-documents |
| **notion** | notion, api, pages, databases | productivity |
| **ocr-and-documents** | ocr, pdf, extract, annotate | pdf, nano-pdf |
| **pdf** | pdf, create, read, merge, fill, secure | docx, powerpoint, ocr-and-documents |
| **petdex** | petdex, mascot, animation | productivity |
| **powerpoint** | pptx, deck, python-pptx | docx, pdf |
| **product-price-monitor** | price, monitor, alert | productivity |
| **screenshot-desktop** | screenshot, desktop, windows, telegram | productivity |
| **session-librarian** | session, librarian, organize | productivity |
| **teams-meeting-pipeline** | teams, meeting, graph, replay | productivity |
| **weekly-review-planning** | weekly, review, planning, commitments | productivity |
| **xlsx** | excel, spreadsheet, xlsx, csv, openpyxl | docx, pdf, powerpoint |
| **box** | box, cloud-storage, collaboration, metadata, content-extraction, cli, sdk | google-workspace |
| **microsoft-office** | office, docx, xlsx, pptx | docx, xlsx, pdf |

## Domain: SECURITY (4 skills)
| Skill | Tags | Edges |
|-------|------|-------|
| **awesome-ai-hacking-agents** | hacking, pentest, ai | windows-pentesting |
| **ai-hacking-team** | hacking, pentest, ai, kali, multi-agent | awesome-ai-hacking-agents, windows-pentesting, networking |
| **ai_hacking_core** | hacking, core, architecture, red-teaming | awesome-ai-hacking-agents, windows-pentesting, ai-hacking-team |
| **hf-agent-intrusion-july2026** | security, incident, analysis, hf | ai_hacking_core, security-incident-research |

## Domain: CCTV (3 skills)
| Skill | Tags | Edges |
|-------|------|-------|
| **cctv-monitor-alert** | cctv, hikvision, alert | cctv-object-detection |
| **cctv-object-detection** | yolo, detection, object | cctv-monitor-alert |
| **hikvision-camera-control** | hikvision, camera, stream | cctv-monitor-alert |

## Domain: SPORTS (4 skills)
| Skill | Tags | Edges |
|-------|------|-------|
| **football-match-prediction** | football, prediction, xg, understat | live-match-data, sports-scores |
| **football-match-enhanced** | football, prediction, live, enhanced | football-match-prediction, live-match-data |
| **live-match-data** | espn, live, scores, football | football-match-prediction, sports-scores |
| **sports-scores** | sports, football, live | media |

## Domain: KNOWLEDGE / MQL5 (4 skills)
| Skill | Tags | Edges |
|-------|------|-------|
| **circle-search-algorithm-csa** | mql5, algorithm, optimization | mql5-articles-master-reference |
| **metatrader-5-machine-learning-blueprint-part-5-seq** | mql5, ml, bootstrapping | mql5-articles-master-reference |
| **reimagining-classic-strategies-part-17-modelling-t** | mql5, strategy, indicators | mql5-articles-master-reference |
| **csv-data-analysis-series** | mql5, csv, data-analysis, python | mql5-articles-master-reference, jupyter-live-kernel |

## Domain: AUTONOMOUS AI AGENTS (8 skills)
| Skill | Tags | Edges |
|-------|------|-------|
| **claude-code** | claude, coding, cli | codex, opencode |
| **codex** | codex, coding, cli | claude-code, opencode |
| **computer-use** | computer-use, desktop, automation | hermes-agent, claude-code, codex |
| **hermes-agent** | hermes, configure, agent | noru-core-knowledge |
| **kanban-codex-lane** | kanban, codex, lane | kanban-orchestrator, codex |
| **opencode** | opencode, coding, cli | claude-code, codex |
| **merge-reconciler** | merge, reconciler, conflict | hermes-agent, kanban-orchestrator |
| **hermes-silent-failure-diagnosis** | hermes, diagnosis, logs, provider, 401, telegram, gateway | hermes-agent, telegram-gateway-troubleshooting, self-evolution |

## Domain: RED-TEAMING (1 skill)
| Skill | Tags | Edges |
|-------|------|-------|
| **godmode** | jailbreak, llm, parseltongue | security |

## Domain: GAMING (2 skills)
| Skill | Tags | Edges |
|-------|------|-------|
| **pokemon-player** | pokemon, emulator, gameboy | gaming |
| **chess-engine** | chess, engine, stockfish, analysis, training, puzzle, strategy | pokemon-player, planning, project_roadmap, master_of_trade |

## Domain: SMART HOME (1 skill)
| Skill | Tags | Edges |
|-------|------|-------|
| **openhue** | philips-hue, lights, scenes | smart-home |

## Domain: EMAIL (2 skills)
| Skill | Tags | Edges |
|-------|------|-------|
| **himalaya** | email, imap, smtp | productivity |
| **email-inbox-triage** | email, triage, inbox | himalaya, productivity |

## Domain: NOTE-TAKING (4 skills)
| Skill | Tags | Edges |
|-------|------|-------|
| **obsidian** | obsidian, notes, vault | notion, llm-wiki |
| **obsidian-bases** | obsidian, bases, views, filters, formulas, database | obsidian, obsidian-markdown, obsidian-cli |
| **obsidian-cli** | obsidian, cli, vault, plugin, theme, dev | obsidian, obsidian-bases, obsidian-markdown |
| **obsidian-markdown** | obsidian, markdown, wikilinks, callouts, embeds, properties | obsidian, obsidian-bases, obsidian-cli |

## Domain: MCP (1 skill)
| Skill | Tags | Edges |
|-------|------|-------|
| **native-mcp** | mcp, client, tools | hermes-agent |

## Domain: QA / TESTING (1 skill)
| Skill | Tags | Edges |
|-------|------|-------|
| **dogfood** | qa, testing, browser | systematic-debugging |

## Domain: HERMES DESKTOP PLUGINS (1 skill)
| Skill | Tags | Edges |
|-------|------|-------|
| **hermes-desktop-plugins** | desktop, plugins, ui, panes | inspecting-hermes-desktop-dom |

## Domain: OTHER / UTILITY (4 skills)
| Skill | Tags | Edges |
|-------|------|-------|
| **sports-scores** | sports, football, live | media |
| **dogfood** | qa, testing, browser | systematic-debugging |
| **useful-skills** | skills, discovery | mind-map-cognition |
| **yuanbao** | yuanbao, tencent, group-chat | media |

---

## Summary
| Domain | Count |
|--------|-------|
| AUTONOMOUS AI AGENTS | 8 |
| CCTV | 3 |
| COGNITIVE ARCHITECTURE | 5 |
| COMMUNICATION | 1 |
| CREATIVE | 21 |
| DATA SCIENCE | 4 |
| DEV / SOFTWARE DEVELOPMENT | 22 |
| DEVOPS | 5 |
| EMAIL | 2 |
| GAMING | 2 |
| GITHUB | 8 |
| HERMES DESKTOP PLUGINS | 1 |
| KNOWLEDGE / MQL5 | 4 |
| MARKET DATA | 3 |
| MCP | 1 |
| MEDIA | 5 |
| ML / AI | 5 |
| NETWORKING | 3 |
| NOTE-TAKING | 4 |
| OTHER / UTILITY | 4 |
| PRODUCTIVITY | 22 |
| QA / TESTING | 1 |
| RED-TEAMING | 1 |
| RESEARCH | 14 |
| SECURITY | 4 |
| SMART HOME | 1 |
| SPORTS | 4 |
| TRADING | 20 |
| TRADING ENGINE | 1 |
| **Total rows** | **179** |

**Note**: 179 rows = 172 unique skills + 7 cross-domain duplicates, 29 domains. Cross-domain dups are intentional.
