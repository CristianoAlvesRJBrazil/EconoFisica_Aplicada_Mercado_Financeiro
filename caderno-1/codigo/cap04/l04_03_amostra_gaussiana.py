# A referência: uma amostra normal com a média e o desvio do Ibovespa
rng = np.random.default_rng(seed=42)
gauss = pd.Series(rng.normal(r_ibov.mean(), r_ibov.std(), len(r_ibov)),
                  index=r_ibov.index)


def resumo(r):
    s = r.std()
    return {"desvio_%": 100 * s, "assimetria": stats.skew(r),
            "curtose": stats.kurtosis(r), "pior_%": 100 * r.min(),
            "melhor_%": 100 * r.max(), "dias>4dp": (abs(r) > 4 * s).sum()}


tabela = pd.DataFrame({"Ibovespa": resumo(r_ibov), "Normal": resumo(gauss)})
print(tabela.round(2))
