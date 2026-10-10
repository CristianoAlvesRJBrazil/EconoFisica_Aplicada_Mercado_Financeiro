import time

grande = np.random.default_rng(1).uniform(10, 50, size=1_000_000)

t0 = time.perf_counter()
r_laco = [grande[i] / grande[i - 1] - 1 for i in range(1, len(grande))]
t1 = time.perf_counter()
r_vet = grande[1:] / grande[:-1] - 1
t2 = time.perf_counter()

print(f"laço: {t1 - t0:.3f} s   vetorizado: {t2 - t1:.4f} s")
print(f"vetorizado: cerca de {(t1 - t0) / (t2 - t1):.0f} vezes mais rápido")
print(np.allclose(r_laco, r_vet))
