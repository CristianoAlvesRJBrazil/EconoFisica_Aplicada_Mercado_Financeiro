# As ações de cada mercado juntas: cada uma padronizada pela sua
# volatilidade, para que todas fiquem na mesma escala
fig, ax = plt.subplots(figsize=(6.4, 3.2))
for rotulo, acoes in [("ações BR", ACOES_BR), ("ações EUA", ACOES_EUA)]:
    juntos = np.concatenate([padronizar(retornos[a]).to_numpy()
                             for a in acoes])
    e = expoentes(juntos)
    print(f"{rotulo}: {len(juntos)} retornos; alfa das quedas "
          f"{e['quedas']:.2f}, das altas {e['altas']:.2f}")
    x = np.sort(np.abs(juntos))[::-1]
    ax.loglog(x, np.arange(1, len(x) + 1) / len(x), label=rotulo)
grade = np.logspace(0.3, 1.5, 50)
ax.loglog(grade, 0.012 * (grade / 3) ** -3, "--", color="black",
          label="inclinação -3")
grade_normal = np.logspace(-1, 0.8, 100)
ax.loglog(grade_normal, 2 * stats.norm.sf(grade_normal), ":",
          color="black", label="normal")
ax.set(xlim=(0.3, 40), ylim=(1e-5, 1.5))
ax.set(title="Sobrevivência de |z| das ações (log-log)",
       xlabel="desvios-padrão")
ax.legend()
fig.savefig("figuras/fig_04_02_lei_cubica.pdf")
