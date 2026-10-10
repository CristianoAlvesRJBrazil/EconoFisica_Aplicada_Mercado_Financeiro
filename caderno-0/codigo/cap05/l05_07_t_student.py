gl, loc, escala = stats.t.fit(r)
print(f"graus de liberdade: {gl:.2f}")
print(f"Queda de mais de 5% pela t ajustada: "
      f"{stats.t.cdf(-0.05, gl, loc, escala):.3%}")
