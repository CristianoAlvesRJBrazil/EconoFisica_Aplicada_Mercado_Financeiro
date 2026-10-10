def retorno_simples(p0: float, p1: float) -> float:
    """Retorno simples entre dois preços: p1 / p0 - 1."""
    return p1 / p0 - 1


def retorno_acumulado(retornos: list[float]) -> float:
    """Compõe retornos simples: (1 + r1)(1 + r2)...(1 + rn) - 1."""
    fator = 1.0
    for r in retornos:
        fator *= 1 + r
    return fator - 1


print(f"{retorno_simples(36.77, 36.84):.4%}")
print(f"{retorno_acumulado(retornos):.4%}")
assert math.isclose(retorno_acumulado(retornos),
                    retorno_simples(fechamentos[0], fechamentos[-1]))
print("Conferido: compor os retornos diários dá o retorno do período.")
