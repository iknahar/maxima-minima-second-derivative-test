# Maxima, minima and the second derivative test

Worked examples for the article **Maxima, Minima and the Second Derivative Test**.

Six short scripts. Each one prints its own answers, so you can check every
number yourself instead of taking my word for it. Nothing here is decoration
and nothing needs a GPU.

## Run them

```bash
pip install -r requirements.txt
python code/01_critical_points.py
```

| file | what it does |
| --- | --- |
| `code/01_critical_points.py` | finds the flat spots of a function and says whether each one is a peak, a dip or neither |
| `code/02_closed_interval.py` | the full candidate check on a fenced range, including the edges people forget |
| `code/03_coin_mle.py` | derives the estimate for a bent coin from seven heads in ten tosses, and measures how sharp that answer is |
| `code/04_least_squares.py` | derives the best straight line through five points, then checks it against numpy |
| `code/05_hill_climbing.py` | seven walkers, seven starting points, and how few of them find the real top |
| `code/06_all_numbers.py` | recomputes every figure quoted in the article, from Kepler's barrel to the saddle point odds |

## What you need

Python 3.9 or newer, plus numpy and sympy. That is the whole list.

## The ideas each file is there to prove

* A flat spot is not the same thing as a best answer. `01` and `02`.
* The second derivative test is fast, and it goes quiet exactly when
  `f''` lands on zero. `01` and `06`.
* Maximum likelihood and least squares are the same procedure in different
  clothes. `03` and `04`.
* Local peaks are indistinguishable from the global one when all you can see
  is the ground under your feet. `05`.
* Multiplying probabilities underflows to exactly zero at 619 numbers, which
  is why everyone works with logs. `06`.

## Licence

MIT. Take it, break it, teach with it.
