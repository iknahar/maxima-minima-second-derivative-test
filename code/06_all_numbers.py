"""Every number quoted in the article, recomputed from scratch."""
import numpy as np
import sympy as sp

print("== Kepler's barrel, a cylinder with a fixed corner-to-corner span ==")
h, d = sp.symbols('h d', positive=True)
V = sp.pi*(d**2 - h**2)/4*h
print("  V(h)          :", sp.simplify(V))
print("  V'(h)         :", sp.simplify(sp.diff(V, h)))
print("  flat spot at h:", sp.solve(sp.Eq(sp.diff(V, h), 0), h))
vol = lambda t: np.pi*t*(1 - t*t)/4
hs = np.linspace(0, 1, 2000001)
v = vol(hs)
band = hs[v >= 0.99*v.max()]
print(f"  best height   : {hs[v.argmax()]:.5f} of the span")
print(f"  99% band      : {band.min():.4f} to {band.max():.4f}, width {band.max()-band.min():.4f}")

print("\n== where the fast test goes quiet ==")
x = sp.Symbol('x', real=True)
for e in (x**4, -x**4, x**3):
    g = sp.lambdify(x, e)
    print(f"  {str(e):>6}: slope {sp.diff(e,x).subs(x,0)}, curvature "
          f"{sp.diff(e,x,2).subs(x,0)}, values {g(-0.1):+.4f} {g(0.0):+.1f} {g(0.1):+.4f}")

print("\n== multiplying probabilities falls off a cliff ==")
for n in (100, 300, 618, 619):
    print(f"  {n:>4} draws: product {np.prod(np.full(n, 0.3))!r:<26}"
          f" log sum {np.sum(np.log(np.full(n, 0.3))):.1f}")

print("\n== a fit that never finishes ==")
X = np.array([-3., -2., -1., 1., 2., 3.])
Y = np.array([0, 0, 0, 1, 1, 1])
for slope in (1, 5, 20, 50):
    z = slope*X
    print(f"  steepness {slope:>3}: log believability {np.sum(Y*z - np.logaddexp(0, z)):.4e}")

print("\n== two robots and one book ==")
per_round = 0.99830*1.270589
print(f"  price multiplier per round: {per_round:.6f}")
print(f"  rounds from $106.23 to $23,698,655.93: "
      f"{np.log(23698655.93/106.23)/np.log(per_round):.1f}")

print("\n== flat spots in many directions ==")
for n in (1, 2, 5, 10, 25, 100):
    print(f"  {n:>4} directions: chance they all agree = 2^-{n} = {2.0**-n:.3e}")
