import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from statsmodels.tsa.stattools import acf

# ARCH(1): a variância de hoje depende do choque de ontem
rng = np.random.default_rng(seed=42)
n, omega, alfa = 6000, 0.00008, 0.5
z = rng.normal(size=n)
r = np.zeros(n)
for t in range(1, n):
    variancia = omega + alfa * r[t - 1] ** 2
    r[t] = np.sqrt(variancia) * z[t]
iid = rng.normal(0, r.std(), size=n)        # mesma volatilidade média

for nome, x in [("ARCH(1)", r), ("normal iid", iid)]:
    print(f"{nome:<10} curtose {stats.kurtosis(x):5.2f}   "
          f"acf|r| (1, 2, 3): {np.round(acf(np.abs(x), nlags=3)[1:], 3)}")
