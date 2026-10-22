import pandas as pd
import matplotlib.pyplot as plt

base = pd.read_csv("dados_boxplot.csv", sep=None, engine="python")
nomes = base["departamento"].dropna().unique()
faixas_salariais = [
    base.loc[base["departamento"] == nome, "salario"].dropna()
    for nome in nomes
]

fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot(faixas_salariais, labels=nomes)
ax.set(title="Comparativo salarial entre departamentos",
       xlabel="Departamento", ylabel="Salario")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
