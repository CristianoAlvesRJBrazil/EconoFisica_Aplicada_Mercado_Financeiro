from dados_caderno1 import carregar_retornos

r_sp, r_ibov = carregar_retornos()
for nome, r in [("S&P 500", r_sp), ("Ibovespa", r_ibov)]:
    print(f"{nome:<9} {len(r):6d} retornos, de {r.index.min().date()} "
          f"a {r.index.max().date()}")
