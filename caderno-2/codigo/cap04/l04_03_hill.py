def hill_passo_a_passo(x, k):
    """Estimador de Hill com os k maiores valores de x (positivos)."""
    x = np.sort(x)[::-1]               # do maior para o menor
    limiar = x[k]                      # o (k+1)-ésimo maior valor
    return 1 / np.mean(np.log(x[:k] / limiar))


# Teste com caudas conhecidas: t de Student com 3 graus de liberdade
# (alfa = 3) e normal (sem lei de potência)
rng = np.random.default_rng(seed=42)
amostras = {"t, 3 graus": np.abs(rng.standard_t(3, 20_000)),
            "normal": np.abs(rng.standard_normal(20_000))}
k = 500
for nome, x in amostras.items():
    alfa = hill_passo_a_passo(x, k)
    assert np.isclose(alfa, hill(x, k))        # igual à do módulo
    print(f"{nome:<11} k = {k}: alfa = {alfa:.2f} +- "
          f"{1.96 * alfa / np.sqrt(k):.2f}")
