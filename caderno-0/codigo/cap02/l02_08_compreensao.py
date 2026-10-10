# Compreensão de lista: o mesmo cálculo da Listagem 2.6 em uma expressão
retornos = [fechamentos[i] / fechamentos[i - 1] - 1
            for i in range(1, len(fechamentos))]
quedas = [r for r in retornos if r < 0]
print(len(retornos), len(quedas))
print([round(r, 4) for r in retornos])
