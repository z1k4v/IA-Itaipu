#%%

import pandas as pd

df = pd.read_csv("data/points_tmw.csv", sep= ";")
df.head()

#%%

freq_produto = df.groupby(["descProduto"])[["idTransacao"]].count()
freq_produto["Freq. Abs. Acum."] = freq_produto["idTransacao"].cumsum()
freq_produto["Freq. rel."] = freq_produto["idTransacao"] / freq_produto ["idTransacao"].sum()
freq_produto["Freq. acum."] = freq_produto["Freq. rel."].cumsum()
freq_produto