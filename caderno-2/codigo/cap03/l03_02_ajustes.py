# Quatro candidatas, ajustadas por máxima verossimilhança
candidatas = {"normal": stats.norm, "Laplace": stats.laplace,
              "t": stats.t, "NIG": stats.norminvgauss}
ajustes, tabelas = {}, {}
for indice in ["S&P 500", "Ibovespa"]:
    r = retornos[indice].to_numpy()
    linhas = {}
    for nome, dist in candidatas.items():
        params = dist.fit(r)
        ajustes[indice, nome] = params
        log_v = dist.logpdf(r, *params).sum()       # log-verossimilhança
        ks = stats.kstest(r, dist.cdf, args=params).statistic
        linhas[nome] = {"AIC": 2 * len(params) - 2 * log_v, "KS": ks}
    tabela = pd.DataFrame(linhas).T
    tabela["AIC"] -= tabela["AIC"].min()           # distância à melhor
    tabelas[indice] = tabela.round({"AIC": 0, "KS": 3})
print(pd.concat(tabelas, axis=1))
for indice in ["S&P 500", "Ibovespa"]:
    graus = ajustes[indice, "t"][0]
    print(f"{indice}: t com {graus:.2f} graus de liberdade")
