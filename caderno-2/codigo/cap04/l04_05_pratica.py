def expoentes(z, fracao=0.05):
    """Alfa de Hill das quedas e das altas de retornos padronizados z,
    com os maiores 5% de cada cauda; ic = metade do intervalo de 95%."""
    resultado = {}
    for cauda, x in [("quedas", -z[z < 0]), ("altas", z[z > 0])]:
        k = int(fracao * len(x))
        alfa = hill(x, k)
        resultado[cauda] = alfa
        resultado["ic_" + cauda] = 1.96 * alfa / np.sqrt(k)
    return resultado


# Prática principal: o expoente de cauda das 14 séries
tabela = pd.DataFrame({nome: expoentes(padronizar(r).to_numpy())
                       for nome, r in retornos.items()}).T
print(tabela[["quedas", "ic_quedas", "altas", "ic_altas"]].round(2))
print(f"média das 14 séries: quedas {tabela['quedas'].mean():.2f}, "
      f"altas {tabela['altas'].mean():.2f}")
