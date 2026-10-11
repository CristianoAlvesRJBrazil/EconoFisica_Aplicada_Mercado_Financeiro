# Incerteza do alfa das quedas do S&P 500: pela fórmula, por bootstrap
# simples e por bootstrap de blocos de 250 pregões, que preserva a
# dependência entre dias vizinhos
def alfa_quedas(amostra):
    return expoentes(amostra)["quedas"]


z = padronizar(retornos["S&P 500"]).to_numpy()
alfa = alfa_quedas(z)
k = int(0.05 * (z < 0).sum())
print(f"{'fórmula:':<21}{alfa - 1.96 * alfa / np.sqrt(k):.2f} a "
      f"{alfa + 1.96 * alfa / np.sqrt(k):.2f}")

rng = np.random.default_rng(seed=42)
n, b = len(z), 250
simples = [alfa_quedas(rng.choice(z, n)) for _ in range(500)]
blocos = []
for _ in range(500):
    inicios = rng.integers(0, n - b, n // b)
    amostra = np.concatenate([z[i:i + b] for i in inicios])
    blocos.append(alfa_quedas(amostra))
for nome, valores in [("bootstrap simples", simples),
                      ("bootstrap em blocos", blocos)]:
    baixo, alto = np.percentile(valores, [2.5, 97.5])
    print(f"{nome + ':':<21}{baixo:.2f} a {alto:.2f}")
