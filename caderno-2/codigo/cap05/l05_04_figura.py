# Sobrevivência de |z| do S&P 500 em 1, 5 e 20 pregões
fig, eixos = plt.subplots(1, 2, figsize=(6.4, 3.0), sharey=True)
grade = np.logspace(-1, 0.8, 100)
for ax, titulo, x0 in [(eixos[0], "Ordem real", r),
                       (eixos[1], "Embaralhado", rng.permutation(r))]:
    for h in [1, 5, 20]:
        soma = agregar(x0, h)
        z = np.sort(np.abs((soma - soma.mean()) / soma.std()))[::-1]
        ax.loglog(z, np.arange(1, len(z) + 1) / len(z), label=f"h = {h}")
    ax.loglog(grade, 2 * stats.norm.sf(grade), "--", color="black",
              label="normal")
    ax.set(title=f"S&P 500: {titulo.lower()}", xlabel="desvios-padrão")
    ax.set(xlim=(0.3, 30), ylim=(1e-4, 1.5))
eixos[0].legend()
fig.tight_layout()
fig.savefig("figuras/fig_05_01_horizontes.pdf")
