from pathlib import Path

# A cópia mais recente: com a data no formato ISO, a ordem alfabética
# dos nomes é também a ordem cronológica
arquivo = sorted(Path("dados").glob("yahoo_fechamentos_*.csv"))[-1]
precos = pd.read_csv(arquivo, index_col="Date", parse_dates=True)

print(arquivo.name)
print(precos.round(2).head(3))
print(precos.shape, precos.index.min().date(), precos.index.max().date())
