m, s = r.mean(), r.std()
for k in [3, 4, 5]:
    observados = (np.abs(r - m) > k * s).sum()
    esperados = len(r) * 2 * stats.norm.sf(k)   # sf = 1 - cdf
    print(f"|r - média| > {k} desvios: {observados:3d} dias "
          f"(a normal prevê {esperados:.2f})")

p_normal = stats.norm.cdf(-0.05, m, s)
print(f"Queda de mais de 5% num dia: normal {p_normal:.3%}, "
      f"dados {(r < -0.05).mean():.3%}")
