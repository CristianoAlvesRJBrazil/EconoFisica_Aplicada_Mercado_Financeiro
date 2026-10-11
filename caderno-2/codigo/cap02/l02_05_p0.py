def densidade_no_zero(x):
    """Densidade de probabilidade em zero: a fração dos valores numa
    janela estreita em torno de zero, dividida pela largura da janela."""
    q25, q75 = np.percentile(x, [25, 75])
    meia_largura = (q75 - q25) / 20
    return np.mean(np.abs(x) < meia_largura) / (2 * meia_largura)


# P(0) dos retornos somados em h pregões (janelas sobrepostas)
horizontes = np.array([1, 2, 4, 8, 16, 32])
p0 = {}
for nome in ["S&P 500", "Ibovespa", "DAX", "Nikkei"]:
    r = retornos[nome]
    p0[nome] = [densidade_no_zero(r.rolling(h).sum().dropna())
                for h in horizontes]
    inclinacao = np.polyfit(np.log(horizontes), np.log(p0[nome]), 1)[0]
    print(f"{nome:<9} inclinação {inclinacao:6.3f}   "
          f"alfa = -1/inclinação = {-1 / inclinacao:.2f}")
