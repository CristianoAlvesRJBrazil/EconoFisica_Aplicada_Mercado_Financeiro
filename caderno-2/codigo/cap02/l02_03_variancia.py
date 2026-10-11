# A variância amostral de uma estável (alfa = 1,5) não se estabiliza
rng = np.random.default_rng(seed=42)
estavel = stats.levy_stable.rvs(1.5, 0, size=100_000, random_state=rng)
normal = rng.standard_normal(100_000)
for n in [100, 1_000, 10_000, 100_000]:
    print(f"n = {n:7d}: variância da estável {estavel[:n].var():6.1f}"
          f"   da normal {normal[:n].var():5.2f}")
