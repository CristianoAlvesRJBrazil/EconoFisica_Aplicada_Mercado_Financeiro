rng = np.random.default_rng(seed=42)
print(rng.normal(0, 0.01, size=3).round(5))

rng = np.random.default_rng(seed=42)         # mesma semente...
print(rng.normal(0, 0.01, size=3).round(5))  # ...mesmos números
