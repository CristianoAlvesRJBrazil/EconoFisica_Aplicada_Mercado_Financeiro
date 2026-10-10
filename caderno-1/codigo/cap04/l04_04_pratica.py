fig, eixos = plt.subplots(3, 2, figsize=(6.4, 7.0))
(a, b), (c, d), (e, f) = eixos

for ax, serie, titulo in [(a, r_ibov, "Ibovespa"), (b, gauss, "Normal")]:
    ax.plot(serie.index, serie, linewidth=0.3)
    ax.set_ylim(-0.17, 0.17)
    ax.set_title(f"{titulo}: retornos diários")

bins = np.linspace(-0.17, 0.17, 80)
c.hist(r_ibov, bins=bins, alpha=0.6, label="Ibovespa")
c.hist(gauss, bins=bins, alpha=0.6, label="Normal")
c.set_yscale("log")
c.set_title("Histogramas (escala log)")
c.legend()

d.plot(np.sort(gauss), np.sort(r_ibov), ".", markersize=2)
d.plot([-0.17, 0.17], [-0.17, 0.17], color="C1", linewidth=0.8)
d.set_title("Quantis: Ibovespa contra normal")

k = np.arange(1, 51)
for ax, f_serie, titulo in [(e, lambda s: s, "Autocorrelação dos retornos"),
                            (f, abs, "Autocorrelação dos absolutos")]:
    ax.plot(k, acf(f_serie(r_ibov), nlags=50)[1:], label="Ibovespa")
    ax.plot(k, acf(f_serie(gauss), nlags=50)[1:], label="Normal")
    ax.axhline(0, color="black", linewidth=0.6)
    ax.set_title(titulo)
    ax.set_xlabel("defasagem")
e.legend()
fig.tight_layout()
fig.savefig("figuras/fig_04_01_pratica.pdf")
