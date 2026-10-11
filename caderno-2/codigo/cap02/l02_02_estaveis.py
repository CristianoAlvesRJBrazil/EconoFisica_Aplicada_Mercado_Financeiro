# Estáveis simétricas (beta = 0) de escala 1; alfa = 2 é uma normal
x = np.linspace(-10, 10, 401)
fig, ax = plt.subplots(figsize=(6.4, 2.8))
for alfa in [2.0, 1.5, 1.0]:
    densidade = stats.levy_stable.pdf(x, alfa, 0)
    ax.semilogy(x, densidade, label=f"alfa = {alfa}")
    p5, p10 = stats.levy_stable.sf([5, 10], alfa, 0)
    print(f"alfa = {alfa}:  P(X > 5) = {p5:.1e}   P(X > 10) = {p10:.1e}")
ax.set(title="Densidades estáveis (escala log)", xlabel="x")
ax.legend()
fig.savefig("figuras/fig_02_01_estaveis.pdf")
