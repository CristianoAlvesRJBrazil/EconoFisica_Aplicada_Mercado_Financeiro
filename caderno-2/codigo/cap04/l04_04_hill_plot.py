# Gráfico de Hill: o alfa estimado conforme a fração k/n usada
series = {"S&P 500 (quedas)": quedas, **amostras}
fig, ax = plt.subplots(figsize=(6.4, 3.0))
for nome, x in series.items():
    ks = np.unique(np.geomspace(10, 0.2 * len(x), 60).astype(int))
    ax.semilogx(ks / len(x), [hill(x, k) for k in ks], label=nome)
ax.axhline(3, color="black", linewidth=0.8, linestyle="--")
ax.set_ylim(1, 8)
ax.set(title="Gráfico de Hill", ylabel="alfa estimado",
       xlabel="fração dos maiores valores usada (k/n)")
ax.legend()
fig.savefig("figuras/fig_04_01_hill.pdf")

for fracao in [0.01, 0.025, 0.05, 0.10, 0.20]:
    k = int(fracao * len(quedas))
    print(f"quedas do S&P 500, k/n = {fracao:5.1%}: alfa = "
          f"{hill(quedas, k):.2f}")
