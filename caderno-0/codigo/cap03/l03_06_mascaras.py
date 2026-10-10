quedas = retornos < 0
print(quedas)
print(quedas.sum(axis=0))                    # número de quedas por ação

vale = retornos[:, 1]
print(vale[vale < -0.01].round(4))           # quedas de mais de 1% da VALE3
print(np.where(retornos[:, 2] > 0, "alta", "queda"))   # ITUB4
print(retornos.argmin(axis=0))               # pior queda de cada uma
