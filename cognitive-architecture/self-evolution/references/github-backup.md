# 📤 GitHub Backup Procedure

Backup rutin cognitive architecture ke GitHub.
Dijalankan manual atau sebagai bagian dari self-evolution cron.

---

## Konfigurasi

Dua repo, dua isi — jangan tertukar:

| Detail | Value |
|--------|-------|
| **Repo A (config + skills)** | `https://github.com/syahdannoor/Hermes-Backup.git` (PRIVATE) |
| Local dir Repo A | `C:\Users\syahd\.hermes` — remote name `backup`, branch `master` |
| Isi Repo A | SOUL.md, config.yaml, cron/, sessions/, skills/ (mirror aktif) |
| **Repo B (cognitive architecture)** | `https://github.com/syahdannoor/Noru-AI-Agent.git` |
| Local dir Repo B | `C:\Users\syahd\noru-agent-backup` — remote `origin`, branch `master` |
| **Repo C (agent source)** | Hermes-Backup branch `main`, remote `backup` dari `AppData/Local/hermes/hermes-agent` |

### Sync skills ke Repo A (text-only filter — wajib)

Aktif skills = `C:\Users\syahd\AppData\Local\hermes\skills` = **3.6 GB**, isinya `.curator_backups/*.tar.gz` (2.2 GB), `.venv` (torch dll), market-data CSV. Copy buta = repo bengkak.

Mirror hanya file teks <2 MB, skip `.curator_backups`, `.venv`, `node_modules`, `__pycache__`, `.git` → 3.080 file / 75 MB. Setelah copy: `git status --porcelain | wc -l` harus ratusan, bukan ribuan.


---

## Langkah Backup Manual

### 0. Cek staleness dulu (wajib)

```bash
cd "/c/Users/syahd/noru-agent-backup"
git log -1 --date=short --format='last commit: %h %ad %s'
git status --short | wc -l
```

Jangan pernah jawab "sudah backup" tanpa `git log -1`. Repo bisa saja tertinggal berbulan-bulan di commit lama sementara semua perubahan hanya ada di disk — `git status` bersih TIDAK berarti up-to-date, karena perubahan yang tidak pernah di-copy memang tidak muncul sebagai dirty.

### 1. Copy skills

```bash
# A. cognitive architecture tree
cp -r "/c/Users/syahd/AppData/Local/hermes/skills/cognitive-architecture/"* \
      "/c/Users/syahd/noru-agent-backup/cognitive-architecture/"

# B. Skill lain: COPY HANYA YANG BARU/BERUBAH (scope rule)
#    JANGAN loop `cp -r skills/*/` ke repo — tree aktif berisi market-data/
#    (69 simbol × 8 TF CSV, ±1.5 GB) dan dump docs lain yang bukan skill.
#    Loop buta = commit 2.700 file / 1,9 juta baris sekali jalan (kejadian 2026-11-12).
for s in web/modern-web-guidance web/user-chrome-automation; do
  mkdir -p "/c/Users/syahd/noru-agent-backup/$(dirname "$s")"
  cp -r "/c/Users/syahd/AppData/Local/hermes/skills/$s" "/c/Users/syahd/noru-agent-backup/$(dirname "$s")/"
done
# Verifikasi sebelum commit: `git status --porcelain | wc -l` harus kecil (<100).
# Kalau ribuan → ada direktori data (market-data/, knowledge/tradingview/docs) ke-sweep.
```

Skill yang dibuat di luar tree cognitive-architecture (mis. `autonomous-ai-agents/`, `trading/`, `github/`) adalah penyebab paling sering commit "backup selesai" padahal skill baru tidak ikut — selalu bandingkan `ls` repo vs `ls` skills dir sebelum commit.

### 2. README + commit + push

```bash
# Update README jika perlu (version bump, changelog)
cd "/c/Users/syahd/noru-agent-backup"
git add -A
git commit -m "🧬 Noru vX.Y — description of changes"
git push origin master
```

---

## Kapan Backup

- **Setelah perubahan besar** pada cognitive architecture (skill baru, restruktur)
- **Setelah identity update** (patch identity-noru)
- **Setiap self-evolution cron** jika ada perubahan yang signifikan
- **Sebelum update Hermes Agent** (backup dulu, baru evaluasi update)

---

## Verifikasi Backup

Token diambil dari `gh auth token` — jangan tempel token literal ke file.

```bash
TOKEN=$(gh auth token)
# Bukti commit terbaru yang benar-benar ada di remote (contents/ hanya list file, tidak membuktikan commit):
curl -s -H "Authorization: token $TOKEN" \
  "https://api.github.com/repos/syahdannoor/Hermes-Backup/branches/master" \
  | python -c "import sys,json; c=json.load(sys.stdin)['commit']; print(c['sha'][:8], c['commit']['committer']['date'], c['commit']['message'].splitlines()[0])"
```

Cocokkan sha hasil ini dengan `git rev-parse HEAD` lokal. Kalau beda → push belum jalan.

---

## Recovery dari Backup

Jika cognitive architecture rusak atau hilang:

```bash
# Clone repo
cd /c/Users/syahd/
git clone https://github.com/syahdannoor/Noru-AI-Agent.git noru-agent-restore

# Copy skills back ke Hermes
cp -r noru-agent-restore/cognitive-architecture/* \
      "/c/Users/syahd/AppData/Local/hermes/skills/cognitive-architecture/"

# Memory index akan tetap ada (tool terpisah)
# Tapi pastikan untuk load identity-noru dulu sebagai self-check
```
