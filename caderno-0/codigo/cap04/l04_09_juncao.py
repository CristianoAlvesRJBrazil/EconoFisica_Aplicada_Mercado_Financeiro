arq_dolar = sorted(Path("dados").glob("bcb_dolar_*.csv"))[-1]
dolar = pd.read_csv(arq_dolar, index_col="Date", parse_dates=True)

junto = precos[["^BVSP"]].join(dolar, how="inner").dropna()
junto["ibov_em_dolar"] = junto["^BVSP"] / junto["dolar"]
print(junto.round(2).iloc[[0, -1]])

variacao = junto.iloc[-1] / junto.iloc[0] - 1
print((variacao * 100).round(1))
