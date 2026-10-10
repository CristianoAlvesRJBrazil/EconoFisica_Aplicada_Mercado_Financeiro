"""Funções de dados usadas em todos os capítulos do Caderno 1."""
from pathlib import Path

import numpy as np
import pandas as pd


def arquivo_mais_recente(padrao):
    """Devolve a cópia mais recente de um arquivo (nomes com data ISO)."""
    copias = sorted(Path("dados").glob(padrao))
    if not copias:
        raise FileNotFoundError(f"Sem arquivo {padrao}: rode a Listagem 1.1")
    return copias[-1]


def log_retornos(precos):
    """Log-retornos de uma série de preços, só nos dias com cotação."""
    return np.log(precos.dropna()).diff().dropna()


def carregar_retornos():
    """Log-retornos diários do S&P 500 e do Ibovespa."""
    sp500 = pd.read_csv(arquivo_mais_recente("yahoo_sp500_*.csv"),
                        index_col="Date", parse_dates=True)["^GSPC"]
    ibov = pd.read_csv(arquivo_mais_recente("yahoo_ibovespa_*.csv"),
                       index_col="Date", parse_dates=True)["^BVSP"]
    return log_retornos(sp500), log_retornos(ibov)
