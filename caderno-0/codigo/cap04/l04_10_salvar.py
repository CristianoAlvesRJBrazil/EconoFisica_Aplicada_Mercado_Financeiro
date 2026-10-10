from datetime import date

# Os dados limpos vão para um arquivo novo; o arquivo baixado fica intocado
limpo = Path("dados") / f"precos_limpos_{date.today()}.csv"
precos.to_csv(limpo)
print(limpo.name, precos.shape)
