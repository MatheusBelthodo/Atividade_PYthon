import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

consumo = pd.read_csv("dados_regressao.csv", sep=None, engine="python")
renda = consumo["renda_mensal"]
gastos = consumo["gasto_mensal"]

# Ajusta uma reta para observar a tendencia dos dados
inclinacao, constante = np.polyfit(renda, gastos, 1)
ordem = np.argsort(renda)
renda_ordenada = renda.iloc[ordem]
gasto_estimado = inclinacao * renda_ordenada + constante

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(renda, gastos, label="Dados observados")
ax.plot(renda_ordenada, gasto_estimado, label="Tendencia linear")
ax.set_title("Renda mensal em comparacao com gastos")
ax.set_xlabel("Renda mensal")
ax.set_ylabel("Gasto mensal")
ax.legend()
plt.tight_layout()
plt.show()
