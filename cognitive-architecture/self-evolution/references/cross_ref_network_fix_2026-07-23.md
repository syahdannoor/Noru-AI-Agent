# cross_ref_network.py Path Resolution Fix — 2026-07-23

## Problem
The `cross_ref_network.py` script (used for Network Integrity Check step 5) had a default `--skills-dir` value of `../..` which only reached the `cognitive-architecture/` directory (5 skills), not the actual Hermes skills root at `hermes/skills/` (146 skills).

## Root Cause
Script location: `hermes/skills/cognitive-architecture/self-evolution/scripts/cross_ref_network.py`

Default path resolution:
```
base_dir = /hermes/skills/cognitive-architecture/self-evolution/scripts
../.. = /hermes/skills/cognitive-architecture  ← WRONG (only 5 skills)
../../.. = /hermes/skills  ← CORRECT (146 skills)
```

## Fix Applied
Changed `parser.add_argument('--skills-dir', default='../..')` to `default='../../..'` in `cross_ref_network.py`.

Also fixed network path resolution to use `base_dir.parent.parent / "mind-map-cognition" / "references" / "associative-network.md"` (goes up two levels from `self-evolution/` to reach `cognitive-architecture/` sibling `mind-map-cognition/`).

## Verification
```bash
cd /c/Users/syahd/AppData/Local/hermes/skills/cognitive-architecture/self-evolution
python scripts/cross_ref_network.py
# Skills on disk: 146 | Skills in network: 146 | ✅ Perfect match
```

## Prevention
- When moving scripts between directory depths, always verify path resolution with absolute paths
- Default arguments should point to the actual data root, not a relative assumption
- Run verification scripts after any path-related changes