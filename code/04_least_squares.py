"""Fit a line by making the total squared miss as small as possible."""
import numpy as np
import sympy as sp

b = sp.Symbol('b', real=True)
X = [1, 2, 3, 4, 5]
Y = [2.1, 3.9, 6.2, 7.8, 10.1]

S = sum((yi - b*xi)**2 for xi, yi in zip(X, Y))
print("total miss        :", sp.expand(S))
print("its slope         :", sp.expand(sp.diff(S, b)))
print("slope is zero at  :", sp.solve(sp.diff(S, b), b))
print("curvature         :", sp.diff(S, b, 2), "-> positive, so a dip")

best = float(sp.solve(sp.diff(S, b), b)[0])
print("\nour slope        :", round(best, 6))
print("numpy polyfit    :", np.polyfit(X, Y, 1))
print("smallest miss    :", round(float(S.subs(b, best)), 6))
