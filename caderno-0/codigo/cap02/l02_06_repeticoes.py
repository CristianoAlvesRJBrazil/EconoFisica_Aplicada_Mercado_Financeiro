# Retorno simples de cada pregão: r = P(t) / P(t-1) - 1
retornos = []
for i in range(1, len(fechamentos)):
    r = fechamentos[i] / fechamentos[i - 1] - 1
    retornos.append(r)

for r in retornos:
    print(f"{r:+.2%}")
