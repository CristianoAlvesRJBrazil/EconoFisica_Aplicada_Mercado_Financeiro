import matplotlib.pyplot as plt

# Crescimento de 100 investidos no início: exp(soma acumulada dos
# log-retornos)
acumulado = 100 * np.exp(base.fillna(0).cumsum())

fig, ax = plt.subplots(figsize=(6.4, 3.6))
colunas = ["^BVSP", "IBOV_USD", "^GSPC", "PETR4.SA", "VALE3.SA", "ITUB4.SA"]
for coluna in colunas:
    ax.plot(acumulado.index, acumulado[coluna], label=coluna)
ax.set_yscale("log")
ax.set_yticks([100, 200, 400, 800, 1600], labels=["100", "200", "400",
                                                 "800", "1600"])
ax.minorticks_off()
ax.set_title("Base 100 em janeiro de 2016 (escala logarítmica)")
ax.legend(ncol=3)
fig.savefig("figuras/fig_06_01_base100.pdf")
