import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.tsa.stattools import acf

from dados_caderno1 import carregar_retornos

r_sp, r_ibov = carregar_retornos()
