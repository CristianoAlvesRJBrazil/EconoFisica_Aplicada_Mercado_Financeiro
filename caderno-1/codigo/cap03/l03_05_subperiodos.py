# Autocorrelação de 1 pregão do S&P 500, por período
for inicio, fim in [("1950", "1969"), ("1970", "1989"), ("1990", "2009"),
                    ("2010", "2025")]:
    trecho = r_sp.loc[inicio:fim]
    print(f"{inicio}-{fim}: {trecho.autocorr(1):+.3f}  "
          f"(faixa de 95%: +/- {1.96 / np.sqrt(len(trecho)):.3f})")
