import urllib.request
from pathlib import Path

url = "https://bvmf.bmfbovespa.com.br/InstDados/SerHist/COTAHIST_A2025.ZIP"
arquivo_b3 = Path("dados") / "COTAHIST_A2025.ZIP"

# O servidor da B3 recusa pedidos sem identificação de navegador (erro 403)
pedido = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(pedido) as resposta:
    arquivo_b3.write_bytes(resposta.read())
print(arquivo_b3, round(arquivo_b3.stat().st_size / 1e6, 1), "MB")
