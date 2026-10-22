import pandas as pd
import matplotlib.pyplot as plt

base_vendas = pd.read_csv("dados_barras.csv", sep=None, engine="python")
resumo = base_vendas.pivot(index="categoria", columns="regiao", values="vendas_medias")

ax = resumo.plot(kind="bar", figsize=(10, 6), width=0.8)
ax.set_title("Media de vendas por categoria em cada regiao")
ax.set_xlabel("Categoria de produto")
ax.set_ylabel("Media de vendas")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.show()
