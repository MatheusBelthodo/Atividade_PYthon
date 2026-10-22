import pandas as pd
import matplotlib.pyplot as plt

registros = pd.read_csv("dados_frequencia.csv", sep=None, engine="python")
contagem = registros["tipo_atendimento"].value_counts()

fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(contagem.index, contagem.values)
ax.set_title("Quantidade de registros por atendimento")
ax.set_xlabel("Tipo de atendimento")
ax.set_ylabel("Numero de ocorrencias")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.show()
