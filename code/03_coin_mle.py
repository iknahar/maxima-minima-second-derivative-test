"""Seven heads in ten tosses. What is the coin? Derive it, do not guess."""
import numpy as np
import sympy as sp

p = sp.Symbol('p', positive=True)
n, k = 10, 7

ll = k*sp.log(p) + (n - k)*sp.log(1 - p)        # log of p^7 (1-p)^3
slope = sp.simplify(sp.diff(ll, p))
answer = sp.solve(sp.Eq(slope, 0), p)
curve = sp.simplify(sp.diff(ll, p, 2)).subs(p, sp.Rational(k, n))

print("log believability :", ll)
print("its slope         :", slope)
print("slope is zero at  :", answer)
print("curvature there   :", curve, "=", float(curve))
print("so it is a", "peak" if curve < 0 else "dip")

# the same answer by brute force, as a sanity check
grid = np.linspace(1e-9, 1 - 1e-9, 2000001)
lik = grid**k * (1 - grid)**(n - k)
print("\nbrute force best p:", round(grid[lik.argmax()], 6))
print("best believability:", lik.max())

# how sharp is that peak, for 10 tosses and for 200
for N in (10, 200):
    c = N / (0.7*0.3)
    print(f"n = {N:>3}   curvature {c:8.2f}   wobble +/- {1/np.sqrt(c):.4f}")
