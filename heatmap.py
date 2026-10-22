import pandas as pd
import matplotlib.pyplot as plt

movimento = pd.read_csv("dados_heatmap.csv", sep=None, engine="python")
ordem_dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

quadro = movimento.pivot(index="dia_semana", columns="horario", values="movimento_clientes")
quadro = quadro.reindex(ordem_dias)

fig, ax = plt.subplots(figsize=(10, 6))
imagem = ax.imshow(quadro, aspect="auto")
fig.colorbar(imagem, ax=ax, label="Quantidade de clientes")
ax.set_xticks(range(len(quadro.columns)), labels=quadro.columns)
ax.set_yticks(range(len(quadro.index)), labels=quadro.index)
ax.set_xlabel("Faixa de horario")
ax.set_ylabel("Dia")
ax.set_title("Intensidade do movimento durante a semana")
plt.tight_layout()
plt.show()
