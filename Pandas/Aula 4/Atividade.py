# Missão 1: Configuração Inicial


# 1. Importe pandas, numpy e datetime
#pip install numpy
import pandas as pd
import numpy as np
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

#2. Carregue o arquivo Excel usando pd.read_excel() com engine='openpyxl'
#3. Crie uma variável df_original para manter os dados originais
dados_original = pd.read_excel("dados_clinica.xlsx", engine="openpyxl")

#4. Crie uma cópia chamada df para trabalhar
dados = dados_original.copy()


#5. Imprima: 
# O nome das colunas
print("Colunas do DataFrame:")
print(dados.columns)

# O número total de registros
print("\nNúmero total de registros:")
print(f"{dados.shape[0]:,}".replace(",", "."))

# As 3 primeiras linhas do DataFrame
print("\nPrimeiras 3 linhas do DataFrame:")
print(dados.head(3))

# O tipo de dado de cada coluna
print("\nTipos de dados das colunas:")
print(dados.dtypes)
