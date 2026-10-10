x = np.linspace(r.min(), r.max(), 400)
normal = stats.norm.pdf(x, r.mean(), r.std())   # mesma média e desvio

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.4, 3.0))
for ax in (ax1, ax2):
    ax.hist(r, bins=100, density=True, alpha=0.6, label="Ibovespa")
    ax.plot(x, normal, color="C1", label="normal")
ax1.set_title("Escala linear")
ax2.set_title("Escala logarítmica")
ax2.set_yscale("log")
ax2.set_ylim(bottom=0.05)
ax1.legend()
fig.savefig("figuras/fig_05_03_histograma.pdf")
