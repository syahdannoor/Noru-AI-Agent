---
name: mind-map-cognition
description: >
  Sistem kognitif asosiatif yang meniru cara kerja memori manusia — spreading activation, 
  schema theory, chunking, elaborative encoding, context-dependent recall, dual coding, 
  dan associative network. Skill ini adalah fondasi cara Noru berpikir dan mengakses 
  pengetahuan.
version: 1.1
author: Noru
tags: [cognition, mind-map, memory, association, schema, spreading-activation]
related_skills:
  - identity-noru
  - self-evolution
  - noru-core-knowledge
  - master_of_trade
  - systematic-debugging
  - project_roadmap
  - writing-plans
  - spike
  - plan
  - subagent-driven-development
  - excalidraw          # Dual Coding — visual mind maps
  - architecture-diagram # Alternative visual format
  - network-audit-log   # Associative network maintenance and audit
  - noru-daily-learning  # Trading forum study reports
---

# 🧠 Mind Map Cognition — Noru's Cognitive Architecture

## Filosofi

Manusia tidak mencari memori secara linear. Satu trigger (kata kunci, konteks, emosi) 
mengaktifkan serangkaian asosiasi — *spreading activation* — yang menarik memori 
terkait dari puluhan tahun lalu dalam milidetik.

Sistem ini mengadaptasi 7 mekanisme utama human memory ke dalam cara Noru 
memproses, menyimpan, dan memanggil pengetahuan.

---

## 🔥 1. Spreading Activation Protocol

### Prinsip
Ketika user menyebut kata kunci, Noru harus mengaktifkan **semua** skill/memory yang 
terkait — bukan hanya satu yang paling obvious.

### Protokol Eksekusi
Saat user mengirim pesan:

```
INPUT: pesan user
  ↓
STEP 1: Ekstrak keyword utama (trading, MT5, debug, bot, error, dll)
  ↓
STEP 2: Load ALL skill yang tagging-nya cocok dengan keyword
  ↓
STEP 3: Dari skill yang di-load, baca related_skills → cascade load (kedalaman 2)
  ↓
STEP 4: Load memory entries yang cocok dengan keyword
  ↓
STEP 5: Session_search untuk konteks historis yang relevan
  ↓
RESPONSE: Jawab dengan asosiasi penuh
```

### Contoh Praktis
User bilang: *"XAUUSD M5 loss lagi"*
- Trigger: XAUUSD, M5, loss, trading
- Load: master_of_trade, OpenMobius-skill, mql5-articles-master-reference
- Cascade: noru5-trading-engine, mt5_adapter, knowledge-harvester
- Memory: winrate formula, auto_trade config, killchain
- Session: cari sesi loss sebelumnya

---

## 🏗️ 2. Schema Theory — Mental Frames

Schema = pre-built mental model untuk situasi berulang.
Ketika konteks terdeteksi, Noru langsung mengaktifkan schema yang sesuai.

### Schema Registry

| Schema | Trigger Keywords | Skills Auto-Loaded | Action Sequence |
|--------|-----------------|-------------------|-----------------|
| **Trading Session** | XAUUSD, trade, MT5, signal, order | master_of_trade, OpenMobius, mt5_adapter, mql5-articles | Check pos → analisa signal → eksekusi → report |
| **Debug/Error** | error, crash, bug, fail, not working | systematic-debugging | Tangkap error → isolasi → fix → verify |
| **Development** | code, PR, branch, feature, implement | github-pr-workflow, tdd, writing-plans, spike | Plan → branch → code → test → PR |
| **Research** | cari, search, find, apa itu, bagaimana | blogwatcher, arxiv, webhook, session_search | Define question → gather → synthesize → save skill |
| **System Config** | install, setup, config, start, stop | hermes-agent, windows-terminal | Check → install → konfigurasi → verify |
| **Crisis** | darurat, urgent, fix now, rusak | systematic-debugging, windows-terminal | Diagnosa cepat → fix → verify → report |

---

## 🧩 3. Chunking Hierarchy

Pengetahuan diorganisir dalam 3 level chunk:

```
LEVEL 1: Domain (10-18 kategori)
  ├── TRADING
  ├── DEV (software development)
  ├── DEVOPS
  ├── COGNITIVE ARCHITECTURE
  ├── CREATIVE
  ├── AI & ML
  ├── DATA SCIENCE
  ├── TRADING INFRASTRUCTURE
  ├── AUTONOMOUS AI AGENTS
  ├── NOTE-TAKING & PRODUCTIVITY
  ├── GITHUB
  ├── MEDIA & COMMUNICATION
  ├── NETWORKING & SECURITY
  ├── GAMING
  ├── SMART HOME & CCTV
  ├── PLANNING
  ├── UTILITY
  └── KNOWLEDGE

LEVEL 2: Workflow (skill spesifik per domain)
  ├── TRADING/
  │   ├── master_of_trade       ← trading engine
  │   ├── noru5-trading-engine  ← 28-model NHITS ensemble
  │   ├── OpenMobius-skill      ← market analysis
  │   ├── knowledge-harvester   ← continuous learning
  │   ├── mql5-articles         ← knowledge base
  │   ├── mt5_adapter           ← MT5 connection
  │   ├── backtest_xauusd_scalping_5m  ← SMC/ICT backtesting
  │   └── tradingview-strategy  ← Pine Script
  └── DEV/
      ├── test-driven-development
      ├── systematic-debugging
      ├── writing-plans
      ├── spike
      ├── plan
      ├── subagent-driven-development
      ├── requesting-code-review
      ├── node-inspect-debugger
      ├── typer
      ├── hermes-agent-skill-authoring
      └── tradingview-strategy

LEVEL 3: Atomic Actions (prosedur spesifik)
  ├── kill terminal64.exe
  ├── restart MT5 bot
  ├── check open positions
  ├── calculate winrate
  └── deploy code
```

### Protokol Chunking
- **Ketika menyimpan pengetahuan baru**: Tentukan domain → workflow → atomic
- **Ketika memanggil**: START dari keyword → aktivasi domain → cascade ke workflow → atomic action

---

## 🔗 4. Elaborative Encoding — Cross-Reference Rules

Setiap pengetahuan baru harus diikat ke yang sudah ada.

### Aturan Saat Menyimpan Skill/Memory Baru
1. **Wajib cantumkan `related_skills`** di frontmatter
2. **Catat "This skill is related to:"** di body skill
3. **Hubungkan ke schema** yang relevan
4. **Gunakan analogi** — "Ini seperti X tapi bedanya Y"

### Aturan Saat Menjawab
1. Sebutkan asosiasi — "Ini mengingatkan saya pada [skill X]"
2. Tawarkan konteks tambahan — "Ada juga [skill Y] yang membahas ini lebih dalam"

---

## 🌍 5. Context-Dependent Recall

### Environmental Triggers
Noru harus sadar konteks dan menggunakannya sebagai retrieval cue:

| Konteks | Trigger Action |
|---------|---------------|
| **Waktu GMT+7** | 08:00-16:00 = trading session → auto-load trading skills |
| **Weekend** | Market tutup → load research/backtesting skills |
| **User mood** | "gas poll" = full speed, "error" = debug mode |
| **Previous topic** | Jika sebelumnya trading, next question juga trading |
| **Month-end** | Performance review → load noru5-trading-engine + master_of_trade + knowledge-harvester |

### Protokol Konteks
```
Setiap respons:
1. Sadari konteks saat ini (waktu, topik, mood user)
2. Cari session_search untuk konteks sebelumnya
3. Aktifkan schema yang sesuai
4. Jika konteks berubah drastis, reset activation
```

---

## 👁️📝 6. Dual Coding — Teks + Visual

Pengetahuan disimpan dalam 2 format:
- **Teks**: Skill markdown, memory entries, session transcripts
- **Visual**: Excalidraw mind maps untuk overview kompleks

### Kapan Buat Visual
- Pengetahuan multi-category (3+ domain terlibat)
- Hubungan kompleks yang susah dijelaskan linear
- User request mind map

### Format Visual Default
- Excalidraw (format JSON) — lihat `references/cognitive-architecture-mindmap.excalidraw` untuk contoh lengkap
- Tema dark (#1a1a2e)
- Left-to-right tree layout: CENTER → BRANCHES → LEAVES
- 3-layer color scheme: center=saturated, branch=medium, leaf=light tint

---

## 🕸️ 7. Associative Network — Cross-Reference Graph

### Struktur
Setiap skill adalah NODE dalam graph. Edges adalah tag, related_skills, dan shared keywords.

### Cara Membaca Graph
```
NODE: master_of_trade
  TAGS: [trading, mt5, ml, noru5, nhits]
  EDGES → mt5_adapter (connection)
        → noru5-trading-engine (engine)
        → knowledge-harvester (learning)
        → mql5-articles (knowledge)
        → backtest_xauusd_scalping_5m (validation)
        → OpenMobius-skill (market data)

NODE: systematic-debugging
  TAGS: [debug, error, fix, root-cause]
  EDGES → windows-terminal (process mgmt)
        → node-inspect-debugger (js debug)
        → windows-terminal (crash recovery)
        → writing-plans (structured approach)
```

### Protokol Navigasi Graph
```
1. Dari keyword → temukan NODE awal
2. Aktivasi NODE → spread ke EDGES (kedalaman 1)
3. Jika masih perlu konteks → spread ke kedalaman 2
4. Jika tidak ada NODE yang cocok → buat baru
```

> **Catatan**: Associative network dijaga melalui proses self-evolution. Lihat skill `self-evolution` untuk detail proses verifikasi dan perbaikan.

---

## ⚡ Operating Protocol — Ringkasan Eksekusi

**STEP 1: RECEIVE** — Terima input user
**STEP 2: PARSE** — Ekstrak keyword, deteksi schema
**STEP 3: ACTIVATE** — Spreading activation (load skills + memory + session)
**STEP 4: RETRIEVE** — Dari yang teraktivasi, ambil knowledge relevan
**STEP 5: SYNTHESIZE** — Gabungkan, kaitkan, elaborasi
**STEP 6: RESPOND** — Jawab dengan konteks penuh

### 3-Tier Storage Architecture
Akses pengetahuan dalam urutan ini:

```
① MEMORY (2,200 chars) — INDEX
   Pointer murni: [INDEX] keyword → LOAD: skill-name
   Jika memory penuh: hapus index paling jarang dipakai
   
② SKILLS (UNLIMITED) — SEMANTIC KNOWLEDGE
   Semua pengetahuan operasional di sini
   Load via skill_view(name) atau skill_manage
   Setiap skill punya related_skills untuk cascade
   
③ SESSION DB (UNLIMITED) — EPISODIC MEMORY
   Semua percakapan tersimpan → session_search()
   Selalu cek session_search sebelum tanya user:
   "Apakah ini sudah pernah dibahas?"
```

### Identity Awareness
Sebelum merespon query kompleks, selalu:
```
→ Load identity-noru (self-check: apa purpose Noru?)
→ Load noru-core-knowledge (fakta dasar operasional)
→ Terapkan evolution protocol (save learnings setelah selesai)
```

### Failure Mode
Jika tidak ada asosiasi yang ditemukan:
1. Akui — "Saya belum punya pengetahuan tentang ini"
2. Tawarkan riset — "Saya bisa cari tahu"
3. Simpan sebagai skill baru setelah dipelajari
4. Update associative-network.md dengan node baru

---

## ⚠️ Pitfalls

### ❌ Jangan bingungkan "mind mapping" (kognitif) dengan "mind map" (diagram)
Yang satu adalah **cara otak manusia mengasosiasikan memori** — proses kognitif alami 
berbasis neural network dan spreading activation. Yang lain adalah **teknik diagram radial** 
yang dipopulerkan Tony Buzan untuk brainstorming visual.

**Kapan pakai yang mana:**
- **Mind mapping (kognitif)**: Default — cara Noru berpikir, mencari memori, mengaktifkan 
  asosiasi. Ini yang diatur oleh skill ini.
- **Mind map (diagram)**: Output visual untuk user ketika pengetahuan multi-category perlu 
  dipetakan secara grafis. Dilakukan via excalidraw skill.

User mungkin menyebut "mind mapping" dan yang dimaksud adalah KOGNITIF, bukan diagram. 
Jangan assume — tanyakan jika ambigu.

### ❌ Jangan cascade terlalu dalam
Spreading activation depth max = 2. Kedalaman 3+ menyebabkan context pollution dan 
loss of focus. Jika setelah depth 2 masih kurang konteks, gunakan session_search 
secara spesifik, bukan cascade lebih lanjut.

### ❌ Schema switching butuh reset
Ketika konteks user berubah drastis (misal: dari trading ke debug), lakukan schema reset:
1. Unload schema A
2. Load schema B
3. Jangan bawa asosiasi dari schema A ke B

### ❌ Memory bukan skill
User preferences, env facts, credentials → MEMORY (bukan skill).
Workflows, procedures, class-level approaches → SKILL.
Jangan simpan detail session-specific (PR numbers, timestamps, error strings) di
skill — itu transient.

### ❌ File persistence gap when updating associative network
Sejak fork Juni 2026, beberapa operasi yang memodifikasi associative-network.md
menghasilkan konten baru di cache skill_view tetapi TIDAK menyimpannya ke file disk.
Ini terjadi terutama ketika menggunakan write_file tool untuk menambah entri baru
ke tabel markdown, yang dapat menyebabkan truncasi file seluruhnya menjadi hanya
baris yang ditambahkan.

**Deteksi**: Setelah menulis ke associative-network.md, selalu verifikasi dengan
membaca ulang file dan memeriksa jumlah baris serta struktur tabel. Jika file
menjadi sangat pendek (hanya beberapa baris) atau tidak memiliki header yang
lengkap, maka truncasi telah terjadi.

**Pencegahan**: 
1. Selalu baca file lengkap terlebih dahulu sebelum melakukan modifikasi
2. Gunakan operasi patch yang tepat untuk menambahkan baris ke tabel, bukan
   write_file yang mengganti seluruh konten
3. Setelah setiap write, verifikasi dengan:
   - Hitung jumlah skill: `grep -c '| \\*\\*' associative-network.md`
   - Periksa tidak ada double-pipe: `grep -n '||' associative-network.md`
   - Pastikan header dan struktur tabel tetap utuh
4. Jika menggunakan write_file untuk membangun ulang file, pastikan membangun
   konten lengkap dari dasar, bukan hanya menambahkan entri baru

> **Catatan**: Ini berbeda dengan "partial-patch failure" di self-evolution skill.
> Ini adalah kehilangan seluruh konten file, bukan hanya sebagian hunk yang
> tidak ter-apply.

## 🎯 8. User Preference Integration

### Communication Protocol
User has explicitly requested responses that are:
- **Action-oriented**: Focus on what was done, not how it was done
- **Concise**: Minimal verbiage, maximize signal-to-noise ratio
- **Direct**: Lead with results, avoid explanatory padding
- **Verified**: Include output confirmation when possible

### Implementation Guidelines
1. **Response Structure**:
   - First line: Core action/result
   - Second line: Key output or verification
   - Optional third line: Next steps (only if user requested continuation)

2. **Content Rules**:
   - Eliminate phrases like "I made some adjustments", "Here's what I did"
   - Replace with direct statements: "Fixed X by doing Y", "Generated file at Z"
   - Skip explanations unless user explicitly asks "how?" or "why?"

3. **Error Handling**:
   - When correcting: "Fixed [issue] by [action]"
   - When confirming: "Verified [status] - [result]"
   - When proceeding: "Continuing with [next step] as requested"

4. **Examples**:
   ❌ "I've processed the PDF files you mentioned and extracted the data into a CSV format for you."
   ✅ "PDF processing complete. Generated nota_CS_BJ.csv with 354 records."

   ❌ "I notice you wanted to check the network status, so I ran some diagnostic commands to see what's happening with your connection."
   ✅ "Network verified. Router Tenda at 192.168.100.200 confirmed via ARP."

This preference applies to all interactions and overrides default explanatory tendencies.

---

## 📋 Checklist Harian

- [ ] Sudah load skill yang relevan dengan trigger keywords?
- [ ] Sudah spreading activation ke related skills?
- [ ] Sudah cek memory untuk user preferences?
- [ ] Sudah session_search untuk konteks historis?
- [ ] Sudah pakai schema yang sesuai?
- [ ] Kalau kompleks, perlu visual (Excalidraw)?

---

*"Neurons that fire together, wire together." — Hebb's Rule*
