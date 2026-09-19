"""Find the flat spots of a function and say what each one is."""
import sympy as sp

x = sp.Symbol('x', real=True)
f = x**3 - 3*x
fp = sp.diff(f, x)          # the slope
fpp = sp.diff(f, x, 2)      # the slope of the slope

print("f   =", f)
print("f'  =", fp)
print("f'' =", fpp)

for c in sp.solve(sp.Eq(fp, 0), x):
    curve = fpp.subs(x, c)
    verdict = "a peak" if curve < 0 else "a dip" if curve > 0 else "no verdict"
    # sympy numbers do not take format specs, so turn them into text first
    print(f"x = {str(c):>4}   height {str(f.subs(x, c)):>4}"
          f"   curvature {str(curve):>4}   {verdict}")

# the corner case: sympy refuses, and it is right to
print()
try:
    sp.solve(sp.Eq(sp.diff(sp.Abs(x), x), 0), x)
except NotImplementedError as e:
    print("abs(x):", str(e).strip().splitlines()[-1])
