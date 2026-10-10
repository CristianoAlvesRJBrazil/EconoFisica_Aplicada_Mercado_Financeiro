tabela = pd.DataFrame({
    "dias": base.count(),
    "media_aa_%": base.mean() * 252 * 100,     # aa: ao ano
    "vol_aa_%": base.std() * np.sqrt(252) * 100,
    "pior_%": base.min() * 100,
    "melhor_%": base.max() * 100,
    "curtose": base.kurt(),                    # curtose em excesso
})
print(tabela.round(1))
