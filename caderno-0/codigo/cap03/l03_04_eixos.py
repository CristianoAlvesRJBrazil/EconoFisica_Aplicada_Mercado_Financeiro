# Fechamentos na B3 de PETR4, VALE3 e ITUB4 nos 6 primeiros pregões de
# 2025: uma linha por pregão, uma coluna por ação
precos = np.array([
    [36.77, 54.25, 30.57],
    [36.38, 53.24, 29.82],
    [36.21, 52.56, 31.16],
    [36.98, 52.05, 31.50],
    [36.68, 51.55, 30.99],
    [36.84, 51.23, 31.07],
])
print(precos.shape)
print(precos.mean(axis=0).round(2))   # média de cada ação (desce as linhas)
print(precos.max(axis=1))             # maior preço de cada pregão
