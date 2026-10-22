import pandas as pd
import matplotlib.pyplot as plt

historico = pd.read_csv("dados_linhas.csv", sep=None, engine="python")
historico["data"] = pd.to_datetime(historico["data"])
historico = historico.sort_values("data")

fig, ax = plt.subplots(figsize=(9, 6))
for nome_loja, vendas_loja in historico.groupby("loja"):
    ax.plot(vendas_loja["data"], vendas_loja["vendas"], marker="o", label=nome_loja)

ax.set_title("Evolucao das vendas por loja")
ax.set_xlabel("Data")
ax.set_ylabel("Total vendido")
ax.legend(title="Loja")
plt.xticks(rotation=40)
plt.tight_layout()
plt.show()
