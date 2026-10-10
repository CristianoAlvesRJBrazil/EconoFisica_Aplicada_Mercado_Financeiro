from datetime import date
from pathlib import Path

import yfinance as yf

# Séries longas: S&P 500 desde 1950 e Ibovespa desde 2000
series = {"sp500": ("^GSPC", "1950-01-01"),
          "ibovespa": ("^BVSP", "2000-01-01")}
for nome, (codigo, inicio) in series.items():
    precos = yf.download(codigo, start=inicio, end="2026-01-01",
                         auto_adjust=True, progress=False)["Close"]
    arquivo = Path("dados") / f"yahoo_{nome}_{date.today()}.csv"
    precos.to_csv(arquivo)
    print(arquivo, precos.shape)
