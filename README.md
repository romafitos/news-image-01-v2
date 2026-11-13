# The World in One Day — news-image-01

[![make.fun](https://make.fun/badge.svg)](https://make.fun)

One image that sums up the world's news of Friday 13 November 2026.

Three full-bleed bands, each a photograph with a headline and one fact
line, plus a ticker with two more stories:

1. **NVIDIA CEO RESIGNS** — Jensen Huang quits after 33 years, shares
   down 4.3% (chip photo, falling stock chart).
2. **EUROPE JOINS UKRAINE PEACE TALKS** — largest prisoner swap planned
   (handshake, Ukrainian and EU flags).
3. **GAZA HOSPITAL STRUCK** — six killed, including a surgeon
   (hospital at dusk, ambulances).
4. Ticker: **MICROSOFT OUTAGE** and **TANKER HIT IN HORMUZ**.

## How it works

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`),
verifying size (≤ 1 MiB), format (PNG or JPEG by magic bytes) and a
byte-identical copy.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `main.py` — the entrypoint
- `entry.png` — the image (1024×1024 JPEG bytes, 414,634 B)
- `LICENSE` — MIT

## License

MIT — see `LICENSE`.
