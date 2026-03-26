# NAS PIN Brute Force with Raspberry Pi GPIO

Physical PIN brute-force tool for a **Thecus N8800 PRO** NAS using a Raspberry Pi connected directly to the front-panel button contacts via GPIO.

## Background

Bought a second-hand Thecus N8800 PRO NAS from OLX — the seller didn't know the admin PIN. The NAS has a small LCD panel on the front with physical buttons for navigation and digit input. This project automates pressing those buttons to try all 10,000 possible 4-digit PINs (0000–9999).

## How it works

The Raspberry Pi's GPIO pins are wired to two button contacts on the NAS front panel:

| GPIO Pin (BCM) | Function | NAS Button |
|---|---|---|
| **4** | Navigate / confirm | Shows password panel, moves to next digit |
| **17** | Increment | Cycles digit value 0→1→2→...→9 |

Both lines are **active-LOW** — pulling a pin LOW for ~170ms simulates a button press.

### Sequence for each PIN attempt

1. Pulse GPIO 4 → opens password entry screen
2. For each of the 4 digits:
   - Pulse GPIO 17 N times (to select digit value N)
   - Pulse GPIO 4 (move to next digit position)
3. Wait 7 seconds for the NAS lockout timer after a wrong PIN
4. Repeat with next combination

## Wiring

```
Raspberry Pi              NAS Front Panel
─────────────             ───────────────
GPIO 4  ──────────────►  Navigate button contact
GPIO 17 ──────────────►  Increment button contact
GND     ──────────────►  Common ground
```

Make sure the Raspberry Pi and NAS share a common ground. Solder or clip wires directly to the button pads on the NAS front panel PCB.

## Usage

```bash
# Run on the Raspberry Pi
python3 code.py
```

To resume from a specific PIN (e.g. after a power interruption), edit the `START_FROM` variable in `code.py`:

```python
START_FROM = "0180"  # skip 0000-0179, start from 0180
```

Stop anytime with `Ctrl+C` — the script prints the last attempted PIN so you know where to resume.

## Timing

| Parameter | Value |
|---|---|
| Pulse duration | 170ms |
| Interval between pulses | 1s |
| Lockout delay after wrong PIN | 7s |
| Approx. time per attempt | ~15-20s (depends on digit values) |
| Worst case for all 10,000 PINs | ~2-3 days |

## Requirements

- Raspberry Pi (any model with GPIO)
- Python 3
- `RPi.GPIO` library (pre-installed on Raspberry Pi OS)
- Wires soldered/clipped to the NAS front panel buttons

## NAS Model

[Thecus N8800 PRO](https://www.thecus.com/product?cat=linux_nas&cat_type=largeBusinessTower&PROD_ID=14&language_num=1) — 8-bay Linux NAS tower
