import pandas as pd
import random
import numpy as np
from datetime import datetime, timedelta

# Configurações
n_linhas = 13000

clientes = [f"Cliente_{i}" for i in range(1, 3001)]
restaurantes = ["Pizza Mania", "Sushi Express", "Burger House", "Tempero Caseiro",
                "Cantina Italiana", "Açaí Tropical", "Pastel & Cia", "Churrasco Grill"]
categorias = ["Pizza", "Japonesa", "Hamburguer", "Brasileira", "Italiana",
              "Açai", "Salgados", "Churrasco"]
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Salvador"]
formas_pagamento = ["Cartão Crédito", "Cartao Debito", "Dinheiro", "Pix", "pix"]
status_pedido = ["Entregue", "Cancelado", "Em preparo", "Saiu para entrega"]

def gerar_data():
    base = datetime(2024, 1, 1)
    dias = random.randint(0, 364)
    data = base + timedelta(days=dias)
    
    formatos = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%m-%d-%Y"
    ]
    return data.strftime(random.choice(formatos))

dados = []

for i in range(n_linhas):
    valor = round(random.uniform(20, 150), 2)
    taxa = round(random.uniform(3, 15), 2)
    desconto = random.choice([0, 5, 10, np.nan])
    
    quantidade = random.choice([1, 2, 3, 4, "2", "3"])
    
    dados.append([
        i + 1,
        random.choice(clientes),
        random.choice(restaurantes),
        random.choice(categorias),
        gerar_data(),
        valor,
        taxa,
        desconto,
        quantidade,
        random.choice(formas_pagamento),
        random.choice(status_pedido),
        random.choice(cidades)
    ])

colunas = [
    "id_pedido",
    "cliente",
    "restaurante",
    "categoria",
    "data_pedido",
    "valor_pedido",
    "taxa_entrega",
    "desconto",
    "quantidade_itens",
    "forma_pagamento",
    "status",
    "cidade"
]

df = pd.DataFrame(dados, columns=colunas)

# Inserindo algumas duplicações
df = pd.concat([df, df.sample(50)], ignore_index=True)

# Salvando CSV
df.to_csv("pedidos_delivery_13000.csv", index=False, encoding="utf-8")

print("Dataset gerado com sucesso!")
print("Total de linhas:", len(df))
