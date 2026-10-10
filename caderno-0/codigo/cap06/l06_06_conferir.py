arquivo = sorted(Path("dados").glob("yahoo_2025_sem_ajuste_*.csv"))[-1]
yahoo = pd.read_csv(arquivo, header=[0, 1], index_col=0, parse_dates=True)
def sem_sufixo(coluna):
    return coluna.removesuffix(".SA")           # "PETR4.SA" -> "PETR4"


fech_yahoo = yahoo["Close"].rename(columns=sem_sufixo)
ajust_yahoo = yahoo["Adj Close"].rename(columns=sem_sufixo)

fech_b3 = b3.pivot(index="data", columns="ticker", values="fechamento")
diferenca = (fech_b3 - fech_yahoo).abs()
print("Pregões em que B3 e Yahoo diferem em mais de R$ 0,005:")
print((diferenca > 0.005).sum())
print("Razão Yahoo/B3 do ITUB4 ao longo de 2025:")
print((fech_yahoo["ITUB4"] / fech_b3["ITUB4"]).round(4).drop_duplicates())
print("Ajustado / sem ajuste no primeiro pregão de 2025:")
print((ajust_yahoo / fech_yahoo).iloc[0].round(4))
