import pandas as pd
import matplotlib.pyplot as plt

# Carrega os valores que serao comparados no grafico
vendas = pd.read_csv("dados_pizza.csv", sep=None, engine="python")

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(
    vendas["faturamento"],
    labels=vendas["canal_venda"],
    autopct="%.1f%%",
    startangle=90
)
ax.set_title("Participacao de cada canal no faturamento")
plt.tight_layout()
plt.show()
