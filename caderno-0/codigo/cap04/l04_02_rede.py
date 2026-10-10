from datetime import date
from pathlib import Path

import yfinance as yf

ativos = ["^BVSP", "^GSPC", "PETR4.SA", "VALE3.SA", "ITUB4.SA"]
precos = yf.download(ativos, start="2016-01-01", end="2026-01-01",
                     auto_adjust=True, progress=False)["Close"]

arquivo = Path("dados") / f"yahoo_fechamentos_{date.today()}.csv"
precos.to_csv(arquivo)
print(arquivo, precos.shape)
