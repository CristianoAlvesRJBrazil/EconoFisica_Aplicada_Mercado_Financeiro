from datetime import date
from pathlib import Path

from bcb import sgs

# Série 1 do SGS: taxa de câmbio do dólar americano (venda), em R$ por US$
dolar = sgs.get({"dolar": 1}, start="2016-01-01", end="2025-12-31")

arquivo = Path("dados") / f"bcb_dolar_{date.today()}.csv"
dolar.to_csv(arquivo)
print(arquivo, dolar.shape)
