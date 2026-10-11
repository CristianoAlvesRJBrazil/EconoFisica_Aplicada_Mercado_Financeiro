from scipy import stats

# Desvio-padrão diário, assimetria e curtose em excesso de cada série
tabela = pd.DataFrame({
    nome: {"desvio_%": 100 * r.std(), "assimetria": stats.skew(r),
           "curtose": stats.kurtosis(r)}
    for nome, r in retornos.items()}).T
print(tabela.round(2))
