import pandas as pd
from scipy import stats

from dados_caderno1 import carregar_retornos

r_sp, _ = carregar_retornos()
historico = r_sp.loc[:"1987-10-16"]     # o que se sabia na véspera
queda = r_sp.loc["1987-10-19"]

z = (queda - historico.mean()) / historico.std()
print(f"Log-retorno em 19/10/1987: {queda:.1%}")
print(f"Desvio-padrão diário de 1950 até a véspera: {historico.std():.2%}")
print(f"A queda equivale a {z:.1f} desvios-padrão")
print(f"Probabilidade pela normal: {stats.norm.cdf(z):.1e}")
