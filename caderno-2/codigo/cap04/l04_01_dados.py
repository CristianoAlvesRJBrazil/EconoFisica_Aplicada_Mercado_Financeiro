import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

from dados_caderno2 import (ACOES_BR, ACOES_EUA, carregar_retornos, hill,
                            padronizar)

retornos = carregar_retornos()
