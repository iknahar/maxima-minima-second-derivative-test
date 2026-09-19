"""Seven walkers, seven starting points, and not many happy endings."""
import numpy as np

f = lambda v: np.sin(3*v) + 0.35*np.sin(7*v) - 0.06*v*v
fp = lambda v: 3*np.cos(3*v) + 2.45*np.cos(7*v) - 0.12*v


def climb(v, step=0.02, rounds=4000):
    for _ in range(rounds):
        v = v + step*fp(v)     # always move whichever way is uphill
    return v


grid = np.linspace(-6, 6, 2000001)
top = f(grid).max()
print(f"the real top is {top:.4f} at x = {grid[f(grid).argmax()]:.4f}\n")

for start in (-5.0, -3.0, -1.0, 0.2, 2.0, 4.0, 5.5):
    end = climb(start)
    tag = "found it" if abs(f(end) - top) < 1e-4 else "stuck"
    print(f"start {start:>5}  ->  x = {end:8.4f}   height {f(end):8.4f}   {tag}")
