# Uma tupla agrupa valores fixos; um dicionário associa chaves a valores
pregao = ("2025-01-02", 36.77)
data, fechamento = pregao                 # desempacotamento
print(data, fechamento)

carteira = {"PETR4": 100, "VALE3": 50, "ITUB4": 80}        # quantidades
precos = {"PETR4": 36.77, "VALE3": 54.25, "ITUB4": 30.57}  # 02/01/2025

total = 0.0
for ticker, qtd in carteira.items():
    total += qtd * precos[ticker]
print(f"Valor da carteira: R$ {total:,.2f}")
print(carteira.get("BBDC4", 0))           # chave ausente: valor padrão
