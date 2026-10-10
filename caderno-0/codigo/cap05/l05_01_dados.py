from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

arquivo = sorted(Path("dados").glob("precos_limpos_*.csv"))[-1]
precos = pd.read_csv(arquivo, index_col="Date", parse_dates=True)
ibov = precos["^BVSP"].dropna()
r = np.log(ibov).diff().dropna()            # log-retornos diários
print(len(r), "retornos, de", r.index.min().date(),
      "a", r.index.max().date())
