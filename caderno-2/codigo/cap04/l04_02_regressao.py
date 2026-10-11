# Regressão na função de sobrevivência em escala log-log: as quedas do
# S&P 500, com quatro escolhas de quantos pontos usar
z = padronizar(retornos["S&P 500"]).to_numpy()
quedas = np.sort(-z[z < 0])[::-1]           # da maior para a menor
sobrevivencia = np.arange(1, len(quedas) + 1) / len(quedas)
for fracao in [0.01, 0.025, 0.05, 0.10]:
    k = int(fracao * len(quedas))
    inclinacao = np.polyfit(np.log(quedas[:k]),
                            np.log(sobrevivencia[:k]), 1)[0]
    print(f"maiores {fracao:5.1%} ({k:3d} pontos): "
          f"alfa = {-inclinacao:.2f}")
