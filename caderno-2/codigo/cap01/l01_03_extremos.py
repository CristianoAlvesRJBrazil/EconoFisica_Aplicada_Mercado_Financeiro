import numpy as np
import pandas as pd

from dados_caderno2 import ACOES_BR, ACOES_EUA

# Movimento próprio: o retorno da ação menos o do índice do seu mercado.
# Os maiores, nos dados brutos, são os primeiros suspeitos de erro.
brutos = carregar_retornos(excluir=False)
linhas = []
for acao in ACOES_BR + ACOES_EUA:
    indice = brutos["Ibovespa" if acao in ACOES_BR else "S&P 500"]
    r = brutos[acao]
    proprio = (r - indice.reindex(r.index)).dropna()
    for dia in proprio[proprio.abs() > 0.17].index:
        linhas.append({"dia": dia.date(), "ação": acao,
                       "ação_%": 100 * r[dia],
                       "índice_%": 100 * indice[dia]})
print(pd.DataFrame(linhas).sort_values("dia").set_index("dia").round(1))
