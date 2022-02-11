import numpy as np

tol = 1e-13

def findroots(p, a, b):
    roots = np.roots(p[::-1]) # np.roots takes coefficients in reverse order
    roots = [z for z in roots if abs(np.imag(z)) < tol
             and a - tol < np.real(z) < b + tol]
    return np.array(sorted(roots))

# p(x) = (x - 0)*(x - 0.25)*(x - 0.5)*(x - 0.75)*(x - 1.0)
p = np.array([0.0, 0.09375, -0.78125, 2.1875, -2.5, 1.0])

roots_true = np.array([0.0, 0.25, 0.5, 0.75, 1.0])

# this choice of (a, b) should be easy if you do the bisection right
a, b = -0.1, 1.2
roots = findroots(p, a, b)
# check relative error... be careful how you do this!
assert (abs(roots - roots_true) < tol*roots_true + tol).all()

# this choice will trigger corner cases
a, b = 0.0, 1.0
roots = findroots(p, a, b)
assert (abs(roots - roots_true) < tol*roots_true + tol).all()
