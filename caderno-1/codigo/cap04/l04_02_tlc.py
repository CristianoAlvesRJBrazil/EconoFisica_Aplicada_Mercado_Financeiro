# Teorema central do limite: somar muitos choques independentes
rng = np.random.default_rng(seed=42)
for n in [1, 2, 10, 50]:
    soma = rng.uniform(-1, 1, size=(100_000, n)).sum(axis=1)
    print(f"soma de {n:2d} choques uniformes: curtose em excesso "
          f"{stats.kurtosis(soma):+.3f}")
