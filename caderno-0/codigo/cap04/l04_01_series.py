import pandas as pd

datas = pd.to_datetime(["2025-01-02", "2025-01-03", "2025-01-06"])
petr4 = pd.Series([36.77, 36.38, 36.21], index=datas, name="PETR4")
print(petr4)

tabela = pd.DataFrame({"PETR4": [36.77, 36.38, 36.21],
                       "VALE3": [54.25, 53.24, 52.56]}, index=datas)
print(tabela)
print(tabela["VALE3"].mean())
