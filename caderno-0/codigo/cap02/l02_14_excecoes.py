def para_numero(texto: str) -> float | None:
    """Converte '36,77' ou '36.77' em número; devolve None se não der."""
    try:
        return float(texto.replace(",", "."))
    except ValueError:
        return None


for texto in ["36,77", "36.38", "n/d", ""]:
    print(repr(texto), "->", para_numero(texto))
