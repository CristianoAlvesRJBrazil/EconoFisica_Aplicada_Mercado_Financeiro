from dados_caderno2 import carregar_retornos

retornos = carregar_retornos()
for nome, r in retornos.items():
    print(f"{nome:<9} {len(r):6d} retornos, de {r.index[0].date()} "
          f"a {r.index[-1].date()}")
