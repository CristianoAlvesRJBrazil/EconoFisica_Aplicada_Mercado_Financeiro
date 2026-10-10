# Log-retornos se somam no tempo: a soma dos diários dá o do período todo
total_somado = logaritmico.sum()
total_direto = np.log(petr4.iloc[-1] / petr4.iloc[0])
print(round(total_somado, 6), round(total_direto, 6))

# Do diário ao mensal: soma dentro de cada mês
mensal = logaritmico.resample("ME").sum()
print(mensal.loc["2025-10":].round(4))

# Volatilidade anualizada pela regra da raiz do tempo (supõe independência)
print(f"{logaritmico.std() * np.sqrt(252):.1%} ao ano a partir dos diários")
print(f"{mensal.std() * np.sqrt(12):.1%} ao ano a partir dos mensais")
