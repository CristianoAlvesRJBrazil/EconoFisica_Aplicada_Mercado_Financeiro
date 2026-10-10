ticker = "PETR4"
retorno = 36.38 / 36.77 - 1        # do 1º para o 2º pregão de 2025

print(f"{ticker}: R$ {preco:.2f} por ação")
print(f"Valor da posição: R$ {valor:,.2f}")
print(f"Retorno no dia: {retorno:.2%}")
print(ticker.lower(), ticker[:4], len(ticker))
