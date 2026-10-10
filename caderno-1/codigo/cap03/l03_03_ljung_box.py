from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.tsa.stattools import acf

# A função acf do statsmodels faz a mesma conta da Listagem 3.2
print(np.allclose(acf(r_ibov, nlags=5)[1:],
                  [autocorrelacao(r_ibov, k) for k in range(1, 6)]))

# Ljung-Box: as 10 primeiras autocorrelações são todas nulas?
for nome, serie in [("retornos", r_ibov), ("absolutos", r_ibov.abs())]:
    teste = acorr_ljungbox(serie, lags=[10])
    print(f"{nome:<10} Q = {teste['lb_stat'].iloc[0]:8.1f}   "
          f"p = {teste['lb_pvalue'].iloc[0]:.2g}")
