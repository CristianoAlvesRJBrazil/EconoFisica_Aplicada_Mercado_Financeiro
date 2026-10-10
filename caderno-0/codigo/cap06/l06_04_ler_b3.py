arquivo_b3 = Path("dados") / "COTAHIST_A2025.ZIP"
b3 = ler_cotahist(arquivo_b3, {"PETR4", "VALE3", "ITUB4"})

print(b3.shape)
print(b3[["data", "ticker", "fechamento", "negocios"]].head(3))
# Primeiro pregão de cada mês com o ITUB4 marcado ex-bonificação (EB)
eb = b3[b3["especi"].str.contains("EB")]
print(eb.groupby(eb["data"].dt.month)["data"].min())
