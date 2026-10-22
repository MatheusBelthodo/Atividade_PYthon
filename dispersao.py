import pandas as pd
import matplotlib.pyplot as plt

amostra = pd.read_csv("dados_dispersao.csv", sep=None, engine="python")
fig, ax = plt.subplots(figsize=(8, 6))

for grupo, parte in amostra.groupby("sexo"):
    ax.scatter(parte["altura_cm"], parte["peso_kg"], label=grupo)

ax.set_title("Altura e peso das pessoas pesquisadas")
ax.set_xlabel("Altura (cm)")
ax.set_ylabel("Peso (kg)")
ax.legend(title="Grupo")
plt.tight_layout()
plt.show()
