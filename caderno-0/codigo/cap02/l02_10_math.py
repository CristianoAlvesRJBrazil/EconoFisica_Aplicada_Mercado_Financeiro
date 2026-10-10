# Retorno logarítmico: ln(p1 / p0). Para variações pequenas, fica muito
# perto do retorno simples; para variações grandes, não.
for p1 in [36.84, 40.00, 50.00]:
    simples = retorno_simples(36.77, p1)
    logaritmico = math.log(p1 / 36.77)
    print(f"R$ {p1:5.2f}   simples {simples:+.4f}   log {logaritmico:+.4f}")
