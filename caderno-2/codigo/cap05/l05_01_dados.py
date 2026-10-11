import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

from dados_caderno2 import (ACOES_BR, ACOES_EUA, carregar_retornos, hill,
                            padronizar)

retornos = carregar_retornos()


def agregar(r, h):
    """Soma os log-retornos em blocos de h pregões, sem sobreposição."""
    x = np.asarray(r)
    m = len(x) // h
    return x[:m * h].reshape(m, h).sum(axis=1)
