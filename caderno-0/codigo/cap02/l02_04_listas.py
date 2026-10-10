# Fechamentos da PETR4 nos cinco primeiros pregões de 2025 (fonte: B3)
fechamentos = [36.77, 36.38, 36.21, 36.98, 36.68]

print(fechamentos[0], fechamentos[-1])    # primeiro e último
print(fechamentos[1:3])                   # fatia: posições 1 e 2
print(len(fechamentos), min(fechamentos), max(fechamentos))

fechamentos.append(36.84)                 # pregão de 09/01/2025
print(fechamentos)
