from datetime import date
from pathlib import Path

import yfinance as yf

# Os mesmos papéis em 2025, agora SEM o ajuste por proventos
papeis = ["PETR4.SA", "VALE3.SA", "ITUB4.SA"]
brutos = yf.download(papeis, start="2025-01-01", end="2026-01-01",
                     auto_adjust=False, progress=False)

arquivo = Path("dados") / f"yahoo_2025_sem_ajuste_{date.today()}.csv"
brutos[["Close", "Adj Close"]].to_csv(arquivo)
print(arquivo, brutos["Close"].shape)
