fig, eixos = plt.subplots(1, 2, figsize=(6.4, 3.0))
for ax, indice, limite in zip(eixos, ["S&P 500", "Ibovespa"],
                              [0.10, 0.15]):
    r = retornos[indice]
    x = np.linspace(-limite, limite, 400)
    ax.hist(r, bins=np.linspace(-limite, limite, 120), density=True,
            color="0.8", label="dados")
    for nome, dist in candidatas.items():
        ax.semilogy(x, dist.pdf(x, *ajustes[indice, nome]), label=nome)
    ax.set_ylim(1e-2, None)
    ax.set(title=indice, xlabel="log-retorno diário")
eixos[0].legend()
fig.tight_layout()
fig.savefig("figuras/fig_03_01_ajustes.pdf")
