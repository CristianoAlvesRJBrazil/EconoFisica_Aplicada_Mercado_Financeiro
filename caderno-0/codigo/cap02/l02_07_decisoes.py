altas = quedas = 0
for r in retornos:
    if r > 0:
        altas += 1
    elif r < 0:
        quedas += 1
print(f"{altas} altas e {quedas} quedas")

# while: em que pregão o preço voltou ao primeiro fechamento?
i = 1
while fechamentos[i] < fechamentos[0]:
    i += 1
print(f"Voltou a R$ {fechamentos[0]} ou mais no pregão de índice {i}")
