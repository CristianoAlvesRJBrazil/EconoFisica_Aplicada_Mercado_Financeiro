# Prática principal: base de log-retornos diários, cada série no seu
# próprio calendário, mais o Ibovespa convertido em dólares
arq_dolar = sorted(Path("dados").glob("bcb_dolar_*.csv"))[-1]
dolar = pd.read_csv(arq_dolar, index_col="Date", parse_dates=True)["dolar"]

ibov = precos["^BVSP"].dropna()
ibov_usd = (ibov / dolar).dropna()      # datas com as duas cotações

series = {c: precos[c].dropna() for c in precos.columns}
series["IBOV_USD"] = ibov_usd
base = pd.DataFrame({nome: np.log(s).diff() for nome, s in series.items()})

saida = Path("dados") / f"base_retornos_m0_{date.today()}.csv"
base.to_csv(saida)
registrar(saida, "calculado", "log-retornos diários, 2016-2025")
print(saida.name, base.shape)
print(base.count())
