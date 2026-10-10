defasagens = np.arange(1, 101)
limite = 1.96 / np.sqrt(len(r_ibov))     # faixa de 95% sem correlação

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.4, 4.2), sharex=True)
for ax, serie, titulo in [(ax1, r_ibov, "Retornos"),
                          (ax2, r_ibov.abs(), "Retornos absolutos")]:
    ax.bar(defasagens, acf(serie, nlags=100)[1:], width=0.8)
    ax.axhspan(-limite, limite, color="C1", alpha=0.25)
    ax.set_title(f"{titulo} do Ibovespa: autocorrelação")
ax2.set_xlabel("defasagem (pregões)")
fig.savefig("figuras/fig_03_01_correlograma.pdf")
print(f"faixa de 95%: +/- {limite:.3f}")
