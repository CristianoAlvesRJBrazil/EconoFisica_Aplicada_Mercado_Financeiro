# Estabilidade: a soma de n estáveis, dividida por n**(1/alfa), tem a
# mesma distribuição de uma só
alfa = 1.5
for n in [1, 10, 100]:
    x = stats.levy_stable.rvs(alfa, 0, size=(n, 20_000), random_state=rng)
    soma = x.sum(axis=0) / n ** (1 / alfa)
    q50, q90, q99 = np.percentile(soma, [50, 90, 99])
    print(f"n = {n:3d}: quantis de 50%, 90% e 99%: "
          f"{q50:5.2f} {q90:5.2f} {q99:5.2f}")
