import matplotlib.pyplot as plt

# Passeio aleatório geométrico: log-retornos normais e independentes
rng = np.random.default_rng(seed=42)
dias, trajetorias = 250, 5
log_r = rng.normal(0.0003, 0.015, size=(dias, trajetorias))
simulados = 100 * np.exp(np.cumsum(log_r, axis=0))

print(simulados.shape)
print(simulados[-1].round(2))           # preço final de cada trajetória

fig, ax = plt.subplots()
ax.plot(simulados)
ax.set_title("Cinco passeios aleatórios a partir de R$ 100")
ax.set_xlabel("pregão")
ax.set_ylabel("preço (R$)")
fig.savefig("figuras/fig_03_01_passeio.pdf")
