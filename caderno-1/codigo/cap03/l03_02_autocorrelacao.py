def autocorrelacao(x, k):
    """Correlação entre a série e ela mesma k passos antes."""
    x = np.asarray(x) - np.mean(x)
    return np.sum(x[k:] * x[:-k]) / np.sum(x * x)


for nome, serie in [("retornos", r_ibov), ("absolutos", r_ibov.abs())]:
    valores = np.array([autocorrelacao(serie, k) for k in range(1, 6)])
    print(f"Ibovespa, {nome:<9} (defasagens 1 a 5): {valores.round(3)}")
