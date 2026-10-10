mensal = precos.resample("ME").last()         # último preço de cada mês
print(mensal.round(2).tail(3))

anual = precos["^BVSP"].resample("YE").last()
print((anual.pct_change() * 100).round(1).dropna())
