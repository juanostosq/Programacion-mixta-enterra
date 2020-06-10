

import sys


if hasattr(sys, '_called_from_test') and sys._called_from_test is True:
    import platform
    if 'pypy' in platform.python_implementation().lower():
        import pytest
        pytest.skip("Matplotlib installation not working under pypy")


if sys.platform == "darwin":
    import matplotlib as mpl
    mpl.use('TkAgg')
    del mpl

import matplotlib.pyplot as plt
from math import sqrt, log
from itertools import product
from mip import Model, xsum, minimize, OptimizationStatus


F = [1, 2, 3]

#x1,x2
pf = {1: (2, 1), 2: (3, 1), 3: (7, 4), 4: (1, 1)}


c = {1: 21, 2: 56, 3: 1987, 4: 12}


C = [1, 2, 3]

# position of clients

# demands
d = {1: 21, 2: 56, 3: 1987, 4: 12}

# plotting possible plant locations
for i, p in pf.items():
    plt.scatter((p[0]), (p[1]), marker="^", color="purple", s=50)
    plt.text((p[0]), (p[1]), "$f_%d$" % i)


for i, p in pc.items():
    plt.scatter((p[0]), (p[1]), marker="o", color="black", s=15)
    plt.text((p[0]), (p[1]), "$c_{%d}$" % i)

plt.text((20), (78), "Region 1")
plt.text((70), (78), "Region 2")
plt.plot((50, 50), (0, 80))

dist = {(f, c): round(sqrt((pf[f][0] - pc[c][0]) ** 2 + (pf[f][1] - pc[c][1]) ** 2), 1)
        for (f, c) in product(F, C) }

m = Model()

z = {i: m.add_var(ub=c[i]) for i in F}


for r in [0, 1]:
    # set of plants in region r
    Fr = [i for i in F if r * 50 <= pf[i][0] <= 50 + r * 50]
    m.add_sos([(z[i], i - 1) for i in Fr], 1)


x = {(i, j): m.add_var() for (i, j) in product(F, C)}


for j in C:
    m += xsum(x[(i, j)] for i in F) == d[j]


y = {i: m.add_var() for i in F}
for f in F:
    D = 4
    v = [c[f] * (v / (D - 1)) for v in range(D)]

    vn = [0 if k == 0 else 1520 * log(v[k]) for k in range(D)]

    w = [m.add_var() for v in range(D)]
    m += xsum(w) == 1

    m += z[f] == xsum(v[k] * w[k] for k in range(D))

    m += y[f] == xsum(vn[k] * w[k] for k in range(D))
    m.add_sos([(w[k], v[k]) for k in range(D)], 2)


for i in F:
    m += z[i] >= xsum(x[(i, j)] for j in C)


m.objective = minimize(
    xsum(dist[i, j] * x[i, j] for (i, j) in product(F, C)) + xsum(y[i] for i in F) )

m.optimize()

plt.savefig("location.pdf")

if m.num_solutions:

    print("Costos minimizados: {}".format([y[f].x for f in F]))


    for (i, j) in [(i, j) for (i, j) in product(F, C) if x[(i, j)].x >= 1e-6]:
        plt.plot(
            (pf[i][0], pc[j][0]), (pf[i][1], pc[j][1]), linestyle="--", color="darkgray"
        )

    plt.savefig("location-sol.pdf")



if m.status == OptimizationStatus.OPTIMAL:
    assert abs(m.objective_value - opt) <= 0.01
elif m.status == OptimizationStatus.FEASIBLE:
    assert m.objective_value >= opt - 0.01
else:
    assert m.status not in [OptimizationStatus.INFEASIBLE, OptimizationStatus.UNBOUNDED]
