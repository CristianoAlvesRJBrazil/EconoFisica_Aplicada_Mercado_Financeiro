def curtose_por_horizonte(r, horizontes):
    """Curtose em excesso dos retornos somados em blocos de h pregões."""
    x = np.asarray(r)
    resultado = {}
    for h in horizontes:
        n = len(x) // h
        resultado[h] = stats.kurtosis(x[:n * h].reshape(n, h).sum(axis=1))
    return pd.Series(resultado)


horizontes = [1, 5, 21, 63, 252]      # dia, semana, mês, trimestre, ano
tabela = pd.DataFrame({
    "S&P 500": curtose_por_horizonte(r_sp, horizontes),
    "Ibovespa": curtose_por_horizonte(r_ibov, horizontes)})
tabela.index.name = "pregões"
print(tabela.round(2))
