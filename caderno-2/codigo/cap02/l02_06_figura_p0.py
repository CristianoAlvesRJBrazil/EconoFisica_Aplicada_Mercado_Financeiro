fig, ax = plt.subplots(figsize=(6.4, 3.0))
for nome, valores in p0.items():
    ax.loglog(horizontes, valores, "o-", markersize=3, label=nome)
# Referência: inclinação -1/2, a de uma soma de choques normais
ref = p0["S&P 500"][0] * horizontes ** -0.5
ax.loglog(horizontes, ref, "--", color="black", label="inclinação -1/2")
ax.minorticks_off()
ax.set_yticks([5, 10, 20, 50], labels=["5", "10", "20", "50"])
ax.set_xticks(horizontes, labels=[str(h) for h in horizontes])
ax.set(title="Densidade em zero contra o horizonte",
       xlabel="horizonte (pregões)", ylabel="P(0)")
ax.legend()
fig.savefig("figuras/fig_02_02_p0.pdf")
