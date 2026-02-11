import pandas as pd
import locale
import matplotlib.pyplot as plt

# Ler arquivo
dados = pd.read_excel("dados_vendas_brutos_corrigidos.xlsx", engine="openpyxl")



dados['data'] = pd.to_datetime(dados['data'],errors="coerce")

# 1.1  Crie uma nova coluna contendo o nome do mês por extenso (em português)
dados['nome_mes'] = dados['data'].dt.month_name(locale="pt_BR")

# 1.2 Crie uma coluna com o nome do dia da semana (em português)
dados['nome_dia'] = dados['data'].dt.day_name(locale="pt_BR")

# 1.3 Crie uma coluna no formato "Mês/Ano" para agrupamentos mensais
dados['mes_ano'] = dados['data'].dt.to_period("M")

# 2.1 Crie uma nova coluna calculando o valor total de cada venda (quantidade × preço unitário)
dados['valor_total'] = dados['quantidade']*dados['preco_unitario']

# 2.2 Ajuste o formato para duas casas decimais
dados['valor_total'] = dados['valor_total'].round(2)

# Missao 3
produto_venda = dados.groupby("loja").agg(
    total_venda = ("valor_total", "sum")
).reset_index().sort_values("total_venda", ascending=True)

plt.figure(figsize=(12,5))

plt.plot(produto_venda["loja"],produto_venda["total_venda"])

plt.show()

print(dados.sample(20).to_string())