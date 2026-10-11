from datetime import date
from pathlib import Path

import pandas as pd
import yfinance as yf


def baixar(codigos, inicio):
    """Fechamentos ajustados de vários códigos, de inicio até 2025."""
    return yf.download(codigos, start=inicio, end="2026-01-01",
                       auto_adjust=True, progress=False)["Close"]


# Índices desde o início de cada série no Yahoo; o Ibovespa, desde 2000
indices = pd.concat([baixar(["^GSPC", "^GDAXI", "^N225"], "1950-01-01"),
                     baixar(["^BVSP"], "2000-01-01")], axis=1)
# Ações de 2000 a 2025, com o índice do seu mercado, para conferir os
# dias em que houve pregão
acoes_br = baixar(["PETR4.SA", "VALE3.SA", "ITUB4.SA", "BBAS3.SA",
                   "SBSP3.SA", "^BVSP"], "2000-01-01")
acoes_eua = baixar(["AAPL", "MSFT", "JPM", "XOM", "KO", "^GSPC"],
                   "2000-01-01")

for nome, precos in [("indices", indices), ("acoes_br", acoes_br),
                     ("acoes_eua", acoes_eua)]:
    arquivo = Path("dados") / f"yahoo_{nome}_{date.today()}.csv"
    precos.to_csv(arquivo)
    print(arquivo, precos.shape)
