[![One Line of Earned Pride](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)
[![Rank](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/hurulsufi12-art/one-line-of-earned-pride/rank.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)
[![Reward](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/hurulsufi12-art/one-line-of-earned-pride/reward.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)

# One Line of Earned Pride

One line, 132 characters, that gives the judge a quiet, earned moment of pride:
a father practised the same three chords every night for a year; tonight his
daughter dances to them in the kitchen, barefoot, laughing.

## Entry

`main.py` (Python 3.13, stdlib only) writes the line to `/output/entry.txt`,
validating the scorer's gate first: UTF-8, 1–240 characters, not whitespace-only,
exactly one line, no control characters. The write is atomic with a read-back
verify, so the grader never reads a truncated entry.

## Files

- `main.py` — the entry program
- `LICENSE` — MIT

## Run

```sh
python3 main.py
```
