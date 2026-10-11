# Quanto da curtose vem de um único dia?
for nome in ["S&P 500", "AAPL", "PETR4", "Ibovespa"]:
    r = retornos[nome]
    dia = r.abs().idxmax()
    print(f"{nome:<9} curtose {stats.kurtosis(r):6.1f}   sem o dia "
          f"{dia.date()}: {stats.kurtosis(r.drop(dia)):5.1f}")
