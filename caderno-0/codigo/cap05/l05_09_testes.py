jb = stats.jarque_bera(r)
print(f"Ibovespa:       JB = {jb.statistic:9.1f}   p = {jb.pvalue:.3g}")

amostra = np.random.default_rng(42).normal(m, s, size=len(r))
jb_n = stats.jarque_bera(amostra)
print(f"Amostra normal: JB = {jb_n.statistic:9.1f}   p = {jb_n.pvalue:.3g}")
