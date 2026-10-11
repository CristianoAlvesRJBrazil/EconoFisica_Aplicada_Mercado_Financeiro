# Dias além de k desvios-padrão no S&P 500: observados e previstos
r = retornos["S&P 500"]
m, s = r.mean(), r.std()
linhas = {}
for k in [3, 4, 5, 6, 8, 10]:
    linha = {"observados": (abs(r - m) > k * s).sum()}
    for nome, dist in candidatas.items():
        params = ajustes["S&P 500", nome]
        p = dist.cdf(m - k * s, *params) + dist.sf(m + k * s, *params)
        linha[nome] = len(r) * p
    linhas[f"> {k} dp"] = linha
print(pd.DataFrame(linhas).T.round(1))
