"""Funções de dados usadas em todos os capítulos do Caderno 2."""
from pathlib import Path

import numpy as np
import pandas as pd

INDICES = {"^GSPC": "S&P 500", "^BVSP": "Ibovespa", "^GDAXI": "DAX",
           "^N225": "Nikkei"}
ACOES_BR = ["PETR4", "VALE3", "ITUB4", "BBAS3", "SBSP3"]
ACOES_EUA = ["AAPL", "MSFT", "JPM", "XOM", "KO"]

# Dias excluídos depois de conferir os extremos (Seção 1.2): eventos
# societários que mudam o preço sem ser um movimento de mercado.
EXCLUSOES = {"ITUB4": ["2021-10-04"]}    # cisão da participação na XP


def arquivo_mais_recente(padrao):
    """Devolve a cópia mais recente de um arquivo (nomes com data ISO)."""
    copias = sorted(Path("dados").glob(padrao))
    if not copias:
        raise FileNotFoundError(f"Sem arquivo {padrao}: rode a Listagem 1.1")
    return copias[-1]


def ler(grupo):
    """Preços do arquivo mais recente de um grupo (indices, acoes_br...)."""
    return pd.read_csv(arquivo_mais_recente(f"yahoo_{grupo}_*.csv"),
                       index_col="Date", parse_dates=True)


def log_retornos(precos):
    """Log-retornos de uma série de preços, só nos dias com cotação."""
    return np.log(precos.dropna()).diff().dropna()


def carregar_retornos(excluir=True):
    """Log-retornos diários dos 4 índices e das 10 ações, num dicionário."""
    retornos = {}
    indices = ler("indices")
    for codigo, nome in INDICES.items():
        retornos[nome] = log_retornos(indices[codigo])
    for grupo, acoes, referencia, sufixo in [
            ("acoes_br", ACOES_BR, "^BVSP", ".SA"),
            ("acoes_eua", ACOES_EUA, "^GSPC", "")]:
        precos = ler(grupo)
        precos = precos[precos[referencia].notna()]   # só dias de pregão
        for acao in acoes:
            r = log_retornos(precos[acao + sufixo])
            if excluir:
                r = r.drop(pd.to_datetime(EXCLUSOES.get(acao, [])))
            retornos[acao] = r
    return retornos


def padronizar(r):
    """Retornos em desvios-padrão: (r - média) / desvio."""
    return (r - r.mean()) / r.std()


def hill(x, k):
    """Estimador de Hill do expoente de cauda com os k maiores valores
    de x (todos positivos). Explicado no Capítulo 4."""
    x = np.sort(np.asarray(x))[::-1]
    return 1 / np.mean(np.log(x[:k] / x[k]))
