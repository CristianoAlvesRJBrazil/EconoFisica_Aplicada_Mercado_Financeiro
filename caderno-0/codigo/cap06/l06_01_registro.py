from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd

REGISTRO = Path("dados") / "registro_dados.csv"


def registrar(arquivo, fonte, descricao):
    """Anota no registro de dados a origem e a data de um arquivo."""
    arquivo = Path(arquivo)
    linha = pd.DataFrame([{
        "arquivo": arquivo.name, "fonte": fonte, "descricao": descricao,
        "baixado_em": date.fromtimestamp(arquivo.stat().st_mtime)}])
    if REGISTRO.exists():                       # substitui a linha antiga
        antigo = pd.read_csv(REGISTRO)
        antigo = antigo[antigo["arquivo"] != arquivo.name]
        linha = pd.concat([antigo, linha])
    linha.to_csv(REGISTRO, index=False)
