def resumo(x):
    """Curtose em excesso e % de valores além de 4 desvios-padrão."""
    z = (x - x.mean()) / x.std()
    return {"curtose": stats.kurtosis(x),
            "acima_4dp_%": 100 * np.mean(np.abs(z) > 4)}


# S&P 500 em horizontes de 1 a 60 pregões: os dados, na ordem real, e a
# média de 20 versões embaralhadas (os mesmos dias, sem dependência)
rng = np.random.default_rng(seed=42)
r = retornos["S&P 500"].to_numpy()
linhas = {}
for h in [1, 5, 20, 60]:
    real = resumo(agregar(r, h))
    emb = pd.DataFrame([resumo(agregar(rng.permutation(r), h))
                        for _ in range(20)]).mean()
    linhas[h] = {"curtose": real["curtose"],
                 "acima_4dp_%": real["acima_4dp_%"],
                 "curtose_emb": emb["curtose"],
                 "acima_4dp_%_emb": emb["acima_4dp_%"]}
tabela = pd.DataFrame(linhas).T
tabela.index.name = "pregões"
print(tabela.round(3))
print(f"normal: {200 * stats.norm.sf(4):.4f}% além de 4 desvios-padrão")
