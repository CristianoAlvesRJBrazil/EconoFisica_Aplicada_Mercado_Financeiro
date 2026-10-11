import matplotlib.pyplot as plt

from dados_caderno2 import padronizar

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.4, 3.0))

# Gráfico quantil-quantil: S&P 500 padronizado contra a normal
z = np.sort(padronizar(retornos["S&P 500"]))
q = stats.norm.ppf((np.arange(1, len(z) + 1) - 0.5) / len(z))
ax1.plot(q, z, ".", markersize=2)
ax1.plot([-5, 5], [-5, 5], color="C1", linewidth=0.8)
ax1.set(title="Quantis: S&P 500 contra normal", xlabel="normal",
        ylabel="S&P 500 (desvios-padrão)")

# Função de sobrevivência de |z| em escala log-log
for nome in ["S&P 500", "Ibovespa"]:
    x = np.sort(np.abs(padronizar(retornos[nome])))[::-1]
    ax2.loglog(x, np.arange(1, len(x) + 1) / len(x), label=nome)
grade = np.logspace(-1, 1.4, 200)
ax2.loglog(grade, 2 * stats.norm.sf(grade), "--", color="black",
           label="normal")
ax2.set(xlim=(0.3, 30), ylim=(1e-5, 1.5))
ax2.set(title="Sobrevivência de |z| (log-log)",
        xlabel="desvios-padrão")
ax2.legend()
fig.tight_layout()
fig.savefig("figuras/fig_01_01_qq_sobrevivencia.pdf")

# Quantos dias passaram de 5 desvios-padrão, e quantos a normal prevê
for nome in ["S&P 500", "Ibovespa"]:
    z = padronizar(retornos[nome])
    previstos = len(z) * 2 * stats.norm.sf(5)
    print(f"{nome:<9} |z| > 5: {(z.abs() > 5).sum():3d} dias; "
          f"a normal prevê {previstos:.3f}")
