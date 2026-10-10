fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.4, 4.4), sharex=True)
ax1.plot(ibov.index, ibov)
ax1.set_yscale("log")
ax1.set_yticks([40_000, 80_000, 160_000],
              labels=["40 mil", "80 mil", "160 mil"])   # cada marca dobra
ax1.minorticks_off()
ax1.set_title("Ibovespa (escala logarítmica)")
ax2.plot(r.index, r, color="C3", linewidth=0.5)
ax2.set_title("Log-retornos diários")
fig.savefig("figuras/fig_05_02_precos_retornos.pdf")
