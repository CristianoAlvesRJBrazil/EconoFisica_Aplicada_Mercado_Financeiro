# Base 100: cada linha dividida pela primeira (broadcasting)
base100 = 100 * precos / precos[0]
print(base100.round(2))

retornos = precos[1:] / precos[:-1] - 1      # as três ações de uma vez
print(retornos.std(axis=0, ddof=1).round(4))
