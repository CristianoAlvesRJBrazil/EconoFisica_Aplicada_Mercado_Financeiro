print(precos.isna().sum())

# Dias com S&P 500 e sem Ibovespa: feriado no Brasil, pregão nos EUA
so_eua = precos["^BVSP"].isna() & precos["^GSPC"].notna()
print(so_eua.sum(), "dias, por exemplo:", precos.index[so_eua][:2].date)

# Dias com preço das ações e sem Ibovespa: o que aconteceu?
suspeitos = precos["^BVSP"].isna() & precos["PETR4.SA"].notna()
anteriores = precos["PETR4.SA"].shift(1)[suspeitos]
print(suspeitos.sum(), "dias; preço igual ao da véspera:",
      (precos.loc[suspeitos, "PETR4.SA"] == anteriores).sum())

# Preço repetido em dia sem índice: tratamos como dia sem pregão na B3
acoes = ["ITUB4.SA", "PETR4.SA", "VALE3.SA"]
precos.loc[suspeitos, acoes] = None
print(precos[acoes].isna().sum().tolist())
