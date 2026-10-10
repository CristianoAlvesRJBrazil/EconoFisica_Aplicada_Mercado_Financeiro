import numpy as np

# Passeio aleatório aritmético de Bachelier: o preço soma choques normais
rng = np.random.default_rng(seed=42)
dias, trajetorias, sigma = 400, 10_000, 1.0     # sigma em R$ por dia
choques = rng.normal(0, sigma, size=(dias, trajetorias))
precos = 100 + np.cumsum(choques, axis=0)

for t in [25, 100, 400]:
    observado = precos[t - 1].std()
    print(f"t = {t:3d} dias: desvio {observado:5.2f}   sigma*raiz(t) = "
          f"{sigma * np.sqrt(t):5.2f}")
