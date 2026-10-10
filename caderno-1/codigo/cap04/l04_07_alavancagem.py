# Efeito alavancagem: o retorno de hoje e a volatilidade dos dias seguintes
for nome, r in [("S&P 500", r_sp), ("Ibovespa", r_ibov)]:
    adiante = [r.corr(r.abs().shift(-k)) for k in (1, 5, 20)]
    atras = [r.abs().corr(r.shift(-k)) for k in (1, 5, 20)]
    print(f"{nome:<9} corr(r hoje, |r| em 1, 5, 20 dias): "
          f"{np.round(adiante, 3)}")
    print(f"{'':<9} corr(|r| hoje, r em 1, 5, 20 dias): "
          f"{np.round(atras, 3)}")
