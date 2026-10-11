def alfa_agrupado(acoes, h, embaralhar=False):
    """Alfa de Hill de |z| das ações juntas, no horizonte de h pregões,
    com os 5% maiores valores."""
    zs = []
    for acao in acoes:
        x = retornos[acao].to_numpy()
        if embaralhar:
            x = rng.permutation(x)
        soma = agregar(x, h)
        zs.append((soma - soma.mean()) / soma.std())
    z = np.abs(np.concatenate(zs))
    return hill(z, int(0.05 * len(z))), len(z)


acoes = ACOES_BR + ACOES_EUA
for h in [1, 5, 10, 20]:
    alfa, n = alfa_agrupado(acoes, h)
    alfa_emb = np.mean([alfa_agrupado(acoes, h, embaralhar=True)[0]
                        for _ in range(10)])
    print(f"h = {h:2d} ({n:5d} valores): alfa {alfa:.2f}   "
          f"embaralhado {alfa_emb:.2f}")
