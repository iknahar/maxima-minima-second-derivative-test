"""On a fenced range the edges are candidates too. Check them."""
import numpy as np


def best_on(fn, flat_spots, lo, hi):
    pts = [c for c in flat_spots if lo <= c <= hi] + [lo, hi]
    scored = [(fn(p), p) for p in pts]
    return max(scored), min(scored)


f = lambda v: v**3 - 3*v
print("candidates and their values")
for p in (-3, -1, 1, 2.5):
    kind = "edge" if p in (-3, 2.5) else "flat spot"
    print(f"  x = {p:>4}   f = {f(p):>8.3f}   {kind}")

hi, lo = best_on(f, [-1, 1], -3, 2.5)
print("\nbest ", hi, "\nworst", lo)

grid = np.linspace(-3, 2.5, 400001)
vals = f(grid)
print("\nbrute force over 400k points:", round(vals.max(), 6), round(vals.min(), 6))
