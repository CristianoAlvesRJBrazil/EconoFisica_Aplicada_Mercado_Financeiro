# Log-retornos de cada série no seu próprio calendário de pregões
retornos = pd.DataFrame({c: np.log(precos[c].dropna()).diff()
                         for c in precos.columns})

resumo = pd.DataFrame({
    "media_%": retornos.mean() * 100,
    "desvio_%": retornos.std() * 100,
    "assimetria": retornos.apply(lambda s: stats.skew(s.dropna())),
    "curtose_exc": retornos.apply(lambda s: stats.kurtosis(s.dropna())),
})
print(resumo.round(2))
