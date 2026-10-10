import zipfile

# Posições (início, fim) de cada campo no layout oficial da B3, contadas a
# partir de 1. Os preços têm duas casas decimais implícitas.
CAMPOS = {"data": (3, 10), "codbdi": (11, 12), "ticker": (13, 24),
          "tpmerc": (25, 27), "especi": (40, 49), "abertura": (57, 69),
          "maxima": (70, 82), "minima": (83, 95), "fechamento": (109, 121),
          "negocios": (148, 152), "volume": (171, 188)}
PRECOS = ["abertura", "maxima", "minima", "fechamento", "volume"]


def ler_cotahist(caminho, tickers):
    """Lê do arquivo anual da B3 as cotações à vista (lote padrão)."""
    registros = []
    with zipfile.ZipFile(caminho) as z, z.open(z.namelist()[0]) as f:
        for bruta in f:                          # uma linha por vez
            linha = bruta.decode("latin-1")
            if linha[:2] != "01" or linha[12:24].strip() not in tickers:
                continue                    # 00 e 99: cabeçalho, rodapé
            campos = {nome: linha[i - 1:j].strip()
                      for nome, (i, j) in CAMPOS.items()}
            if campos["codbdi"] == "02" and campos["tpmerc"] == "010":
                registros.append(campos)
    tabela = pd.DataFrame(registros)
    tabela["data"] = pd.to_datetime(tabela["data"], format="%Y%m%d")
    tabela[PRECOS] = tabela[PRECOS].astype("int64") / 100
    tabela["negocios"] = tabela["negocios"].astype("int64")
    tabela = tabela.sort_values(["data", "ticker"], ignore_index=True)
    return tabela.drop(columns=["codbdi", "tpmerc"])
