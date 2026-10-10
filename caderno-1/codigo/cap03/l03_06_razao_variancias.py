def razao_variancias(r, q):
    """Var(retorno de q pregões) / (q * Var(retorno de 1 pregão))."""
    x = np.asarray(r)
    n = len(x) // q
    somas = x[:n * q].reshape(n, q).sum(axis=1)   # blocos sem sobreposição
    return np.var(somas, ddof=1) / (q * np.var(x, ddof=1))


rng = np.random.default_rng(seed=42)
for nome, r in [("S&P 500", r_sp), ("Ibovespa", r_ibov)]:
    print(nome)
    for q in [2, 5, 10, 20]:
        # Referência: a mesma série embaralhada não tem memória nenhuma
        nulas = [razao_variancias(rng.permutation(r.values), q)
                 for _ in range(200)]
        baixo, alto = np.percentile(nulas, [2.5, 97.5])
        print(f"  q = {q:2d}: {razao_variancias(r, q):.3f}   "
              f"embaralhada: {baixo:.3f} a {alto:.3f}")
