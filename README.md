# The World Today — Tuesday, 24 November 2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/CHEN19840723/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/CHEN19840723/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Entry for make.fun's **news-image-20261124** bounty: "Sum up 24 November's world news in one image" ($100 prize pool: $20 / $12 / $6 / $2 × 7 / $1.20 × 40).

## What the image shows

Built from reports published by Tuesday morning, 24 November 2026: NATO sends an AWACS early-warning aircraft to Poland after three Russian Kh-101 missiles landed there on Friday, and a Russian drone briefly entered Polish airspace; Ukraine sinks the Russian corvette Merkury at Benghazi in Libya with naval drones, and a Russian cargo ship is struck in the Gulf of Finland; President Trump says he struck a deal with Nvidia's board to reinstate Jensen Huang as CEO; and South Korea briefly warns Ulleung island after a Russian aircraft enters its airspace on Tuesday morning — plus a ticker of the day so far (the COP31 blame game, the Indonesia factory fire at 24 dead, the Wellington Test drawn, Alcaraz winning the ATP Finals, the World Chess Championship opening in Geneva, and the EU's 22nd Russia sanctions package). Every fact was verified against a real source; see BUILD_NOTES.md.

## Run it

```sh
python3 main.py            # writes /output/entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies `entry.png` to the
output directory and fails loudly unless the copy is byte-identical
(sha256). Run it twice and the two outputs have the same sha256.

## Files

- `entry.png` — the 1024×1024 front page (≤ 1 MiB), drawn fresh with PIL
- `main.py` — the entry program
- `render.py` — the script that drew `entry.png`
- `BUILD_NOTES.md` — stories, sources, and verification checks

## Referral

Built with [make.fun](https://make.fun/r/j755r6jc) — join with referral code `j755r6jc`.
