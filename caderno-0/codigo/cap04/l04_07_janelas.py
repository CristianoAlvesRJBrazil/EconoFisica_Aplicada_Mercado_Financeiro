import numpy as np

ibov = precos["^BVSP"].dropna()              # só os dias com pregão na B3
r = np.log(ibov).diff()
vol_21 = r.rolling(21).std() * np.sqrt(252)  # volatilidade anualizada
media_200 = ibov.rolling(200).mean()         # média móvel de 200 pregões

print(vol_21.describe().round(3))
print("Maior volatilidade:", vol_21.idxmax().date(), round(vol_21.max(), 3))
print("Acima da média de 200 pregões:", f"{(ibov > media_200).mean():.1%}")
