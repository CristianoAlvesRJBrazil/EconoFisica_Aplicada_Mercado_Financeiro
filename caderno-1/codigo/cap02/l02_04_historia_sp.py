fig, ax = plt.subplots(figsize=(6.4, 3.0))
ax.plot(r_sp.index, r_sp, linewidth=0.4, color="C0")
for data, rotulo in [("1987-10-19", "1987"), ("2008-10-15", "2008"),
                     ("2020-03-16", "2020")]:
    ax.annotate(rotulo, (pd.Timestamp(data), r_sp.loc[data]),
                xytext=(6, -2), textcoords="offset points", fontsize=8,
                color="C3")
ax.set_title("S&P 500: log-retornos diários, 1950 a 2025")
fig.savefig("figuras/fig_02_02_sp500_historia.pdf")
print(r_sp.nsmallest(3).round(3))
