import matplotlib.pyplot as plt

# Mesma volatilidade inicial, 25 anos: aritmético (Bachelier) e
# geométrico (Osborne)
rng = np.random.default_rng(seed=7)
dias, n = 25 * 252, 20
choques = rng.normal(0, 0.02, size=(dias, n))       # 2% ao dia
aritmetico = 100 + np.cumsum(100 * choques, axis=0)
geometrico = 100 * np.exp(np.cumsum(choques, axis=0))

print("Trajetórias que ficaram negativas, de", n)
print("  aritmético:", (aritmetico.min(axis=0) < 0).sum())
print("  geométrico:", (geometrico.min(axis=0) < 0).sum())

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.4, 2.9), sharey=True)
anos = np.arange(dias) / 252
ax1.plot(anos, aritmetico, linewidth=0.6)
ax1.axhline(0, color="black", linewidth=0.8)
ax1.set_title("Aritmético (Bachelier)")
ax2.plot(anos, geometrico, linewidth=0.6)
ax2.axhline(0, color="black", linewidth=0.8)
ax2.set_title("Geométrico (Osborne)")
for ax in (ax1, ax2):
    ax.set_xlabel("anos")
ax1.set_ylabel("preço")
fig.savefig("figuras/fig_02_01_bachelier_osborne.pdf")
