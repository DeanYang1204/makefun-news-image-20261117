[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/DeanYang1204/makefun-news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/DeanYang1204/makefun-news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

Built for [make.fun's "Sum up 17 November's world news in one image" bounty](https://make.fun/bounty/news-image-20261117) — $250 in USDC.

# Tuesday 17 November 2026 — the day in one image

Entry for make.fun's **news-image-20261117** bounty ($250, 50 paid places).
One 1024×1024 image that sums up Tuesday 17 November 2026 in four stories,
laid out as a newspaper front page: a header naming the day, a 2×2 grid of
photographic panels, and a short factual caption under each one. All type is
drawn with PIL — no generated panel carries any text, so nothing is garbled.

## The four stories (all happened / first reported on 17 November 2026)

1. **MARKETS PLUNGE — Nasdaq −2.5% into correction.**
   Nasdaq fell 2.49% into correction (down more than 10% from its 6 October
   peak); S&P 500 −1.92%, Dow −1.41%. Brent crude fell 3.6% to $92.44;
   gold $3,848/oz. The IEA said Q4 oil supply would exceed demand by
   about 1.7 million barrels a day.
2. **TANKER ATTACKED — Engine-room fire in the Strait of Hormuz.**
   An oil tanker was attacked in the strait; an engine-room fire broke out
   and the crew were safe.
3. **KYIV BRIDGES HIT — Crimea bridge struck in drone barrage.**
   Russian strikes damaged two bridges in Kyiv, cutting power and water;
   Ukraine hit the Crimea bridge in a 1,300-drone barrage.
4. **SUMMIT SET FOR NOV 19 — Xi, Trump and Putin to meet in Shenzhen.**
   China confirmed the first trilateral summit of Xi, Trump and Putin,
   to be held on 19 November in Shenzhen.

No other dated event is shown, and no number beyond the ones above is used.

## How it was made

- Four square panels generated with Kie.ai Grok Imagine Image 2.0
  (text-to-image, 1:1), one per story, photographic/editorial style, with
  no text in the generated images. The first summit panel came back with
  the wrong flag in the centre, so it was regenerated with the Chinese flag
  described explicitly (red, five yellow stars).
- The front page was composed from the panels with a Python/Pillow script
  (`~/workspace/makefun-news17-dev/compose.py`, kept out of this repo):
  header band with the date, 2×2 grid, captions drawn in DejaVu Sans.
- The finished image was read back visually: the date is prominent, all
  four stories are recognisable, captions are legible and match the facts,
  no garbled text, no fifth story.

## How to run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies `entry.png` beside
it to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`) and verifies the
copy's sha256 matches the source. No network access. Two runs write
identical bytes.

## Verification

- `entry.png`: JPEG bytes (named `entry.png`, as the rules allow), exactly
  1024×1024, 209,199 bytes (limit 1 MiB), opens as a valid JPEG.
- `main.py` run twice into different output directories: byte-identical
  outputs, sha256 `09085452c67fdce0f5269a2f9e8e7eb919255a87ee2bf2b7282483305fd184e9`.

## License

MIT — see `LICENSE`.
