# Assimetria entre ganhos e perdas: quedas extremas são mais numerosas
for nome, r in [("S&P 500", r_sp), ("Ibovespa", r_ibov)]:
    s = r.std()
    print(f"{nome:<9} quedas > 3 dp: {(r < -3 * s).sum():3d}   "
          f"altas > 3 dp: {(r > 3 * s).sum():3d}   "
          f"assimetria: {stats.skew(r):+.2f}")
