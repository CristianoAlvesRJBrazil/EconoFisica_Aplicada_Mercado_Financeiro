ibov = precos["^BVSP"]                        # uma coluna é uma Series
print(ibov.loc["2020-03-09":"2020-03-13"])    # uma semana de março de 2020

print(precos.loc["2025-12", ["PETR4.SA", "VALE3.SA"]].round(2).tail(3))
print(ibov.idxmax().date(), ibov.max())       # data e valor do máximo
