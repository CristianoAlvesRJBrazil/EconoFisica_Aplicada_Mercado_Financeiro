fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.4, 3.8), sharex=True,
                               sharey=True)
ax1.plot(iid, linewidth=0.3)
ax1.set_title("Normal independente")
ax2.plot(r, linewidth=0.3, color="C3")
ax2.set_title("ARCH(1): a volatilidade depende do passado")
ax2.set_xlabel("dia simulado")
fig.savefig("figuras/fig_05_01_arch.pdf")
