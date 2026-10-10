for padrao, fonte, descricao in [
    ("yahoo_fechamentos_*.csv", "Yahoo Finance", "fechamentos ajustados"),
    ("bcb_dolar_*.csv", "Banco Central, SGS 1", "dólar, venda"),
    ("COTAHIST_A2025.ZIP", "B3", "séries históricas 2025"),
    ("yahoo_2025_sem_ajuste_*.csv", "Yahoo Finance", "2025, sem ajuste"),
]:
    registrar(sorted(Path("dados").glob(padrao))[-1], fonte, descricao)

print(pd.read_csv(REGISTRO)[["arquivo", "fonte", "baixado_em"]]
      .to_string(index=False))
