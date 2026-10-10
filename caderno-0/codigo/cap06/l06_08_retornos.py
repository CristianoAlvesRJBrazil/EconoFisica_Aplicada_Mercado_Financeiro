arquivo = sorted(Path("dados").glob("precos_limpos_*.csv"))[-1]
precos = pd.read_csv(arquivo, index_col="Date", parse_dates=True)
petr4 = precos["PETR4.SA"].dropna()

simples = petr4.pct_change()                 # P(t) / P(t-1) - 1
logaritmico = np.log(petr4).diff()           # ln P(t) - ln P(t-1)
comparacao = pd.DataFrame({"simples": simples, "log": logaritmico}).dropna()
print(comparacao.loc["2020-03-06":"2020-03-12"].round(4))
print((comparacao["simples"] - comparacao["log"]).abs().max().round(4))
