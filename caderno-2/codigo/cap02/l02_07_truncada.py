# Voo de Lévy truncado: passos estáveis (alfa = 1,5) cortados em +-10
rng = np.random.default_rng(seed=7)
passos = stats.levy_stable.rvs(1.5, 0, size=(1024, 20_000),
                               random_state=rng)
somas = {"Lévy": np.cumsum(passos, axis=0),
         "Lévy truncada": np.cumsum(np.clip(passos, -10, 10), axis=0)}

n = 2 ** np.arange(11)                   # 1, 2, 4, ..., 1024 passos
fig, ax = plt.subplots(figsize=(6.4, 3.0))
for nome, s in somas.items():
    d = np.array([densidade_no_zero(s[k - 1]) for k in n])
    inicio = np.polyfit(np.log(n[:4]), np.log(d[:4]), 1)[0]
    fim = np.polyfit(np.log(n[-4:]), np.log(d[-4:]), 1)[0]
    print(f"{nome:<14} inclinação até 8 passos: {inicio:5.2f}   "
          f"de 128 a 1024: {fim:5.2f}")
    ax.loglog(n, d, "o-", markersize=3, label=nome)
ax.loglog(n, d[0] * n ** (-1 / 1.5), ":", color="black",
          label="inclinação -1/1,5")
ax.loglog(n, d[0] * n ** -0.5, "--", color="black",
          label="inclinação -1/2")
ax.minorticks_off()
ax.set_xticks([1, 10, 100, 1000], labels=["1", "10", "100", "1000"])
ax.set(title="Densidade em zero da soma de n passos", xlabel="n",
       ylabel="P(0)")
ax.legend()
fig.savefig("figuras/fig_02_03_truncada.pdf")
