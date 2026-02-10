import pandas as pd

import matplotlib.pyplot as plt

#Bibliotecas necessárias
#pip install pandas
#pip install openpyxl
#pip install matplotlib


df = pd.DataFrame(
    {
        "mes": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
        "lojaA": [1200, 1500, 1800, 1600, 1850, 2100],
        "lojaB": [1600, 1700, 2000, 1750, 1900, 1750]
    }
)

plt.figure(figsize=(8,5))

plt.plot(df["mes"], df["lojaA"], color="red", marker="o", linewidth=2, linestyle='-', label="Loja A")
plt.plot(df["mes"], df["lojaB"], color="blue", marker="x", linewidth=2, linestyle='--', label="Loja B")

plt.title("Análise Mês x Faturamento")
plt.xlabel("Mês")
plt.ylabel("Faturamento")
plt.grid(True)
#plt.show()




# Produzir um dataframe com uma coluna chamada bimestre contendo Bimestre 1, Bimestre 2, Bimestre 3, Bimestre 4 e outra coluna contendo as notas de cada bimestre. Produza um gráfico de linhas ou de barras que exibe as notas do aluno em cada bimestre ao longo do tempo.

df = pd.DataFrame({
    "bimestre": ["Bimestre 1", "Bimestre 2", "Bimestre 3", "Bimestre 4"],
    "nota": [7.5, 8.0, 6.8, 8.7]
})

# Gráfico de linhas
plt.figure(figsize=(8, 5))

plt.plot(df["bimestre"], df["nota"], marker="o", linewidth=2, color="green")
plt.title("Evolução das Notas por Bimestre")
plt.xlabel("Bimestre")
plt.ylabel("Nota")
plt.grid(True)
#plt.show()

#Gráfico de barras 
plt.figure(figsize=(8, 5))

plt.bar(df["bimestre"], df["nota"], color="skyblue")

plt.title("Notas do Aluno por Bimestre")
plt.xlabel("Bimestre")
plt.ylabel("Nota")
plt.ylim(0, 10)
plt.grid(axis="y")

#plt.show()





# Adapte seus dados para ter notas de cada bimestre de Matemática e Química e faça um gráfico que mostra os dois grupos de nota simultaneamente.


df = pd.DataFrame({
    "bimestre": ["Bimestre 1", "Bimestre 2", "Bimestre 3", "Bimestre 4"],
    "matematica": [7.5, 8.0, 6.8, 8.7],
    "quimica": [6.9, 7.4, 7.8, 8.2]
})

plt.figure(figsize=(8,5))

plt.plot(df["bimestre"], df["matematica"], color="purple", 
marker="o", linewidth=2, linestyle='-', label="Matemática")

for i, valor in enumerate(df["matematica"]):
    plt.text(df["bimestre"][i],
             valor + 0.05,
             f'{valor}',
             ha='center', va='bottom')

plt.plot(df["bimestre"], df["quimica"], color="green", marker="x", linewidth=2, linestyle='--', label="Química")

for i, valor in enumerate(df["quimica"]):
    plt.text(df["bimestre"][i],
             valor + 0.05,
             f'{valor}',
             ha='center', va='bottom')


plt.title("Matemática x Química")
plt.xlabel("Bimestre")
plt.ylabel("Notas")
plt.grid(True)
plt.show()
