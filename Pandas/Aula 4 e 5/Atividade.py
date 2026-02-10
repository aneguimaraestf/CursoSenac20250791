# Missão 1: Configuração Inicial


# 1. Importe pandas, numpy e datetime
#pip install numpy
import pandas as pd
import numpy as np
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


#2. Carregue o arquivo Excel com os dados da clínica
dados_original = pd.read_excel("dados_clinica_simplificado.xlsx", engine="openpyxl")

#Crie uma variável df_original para manter os dados originais
#Crie uma cópia chamada dados para trabalhar
dados = dados_original.copy()


#3. Exiba as primeiras 10 linhas do DataFrame para entender a estrutura dos dados
print(dados.head(10))


#4. Verifique quantas linhas e colunas existem no tota
print(
    f"\nA quantidade de colunas é: {dados.shape[1]:,}".replace(",", ".") +
    f"\nA quantidade de linhas é: {dados.shape[0]:,}".replace(",", ".")
)


#5. Identifique o tipo de dado de cada coluna
print(f"\nOs tipos de dados das colunas, são: \n{dados.dtypes}")


#6. Conte quantos valores nulos existem em cada coluna
print(f"\nQuantidade de valores nulos: \n{dados.isnull().sum()}")


#Missão 2: Padronização dos Nomes
#1. Converta todos os nomes para string (caso ainda não estejam)
dados['Nome'] = dados['Nome'].astype(str)


#2. Remova espaços extras no início e fim de cada nome
dados['Nome'] = dados['Nome'].str.strip()


#3. Padronize os nomes para o formato "Primeira Letra Maiúscula" (ex: "Maria Silva")
dados['Nome'] = dados['Nome'].str.title()


#4. Verifique se a correção foi aplicada corretamente
#print(dados.sample(10))


# Missão 3 - Padronizar idade


dados["Idade"] = dados["Idade"].replace(["", " ", "N/A"], pd.NA)

dados["Idade"] = pd.to_numeric(dados["Idade"], errors="coerce")

# Se a coluna for extremamente importante, faz sentido filtrar os dados ruins

# dados_limpo = dados[dados["Idade"].notna()]

mediana_idade = dados[dados["Idade"].notna()]["Idade"].median()

dados.loc[dados["Idade"].isna(), "Idade"] = mediana_idade

dados["Idade"] = dados["Idade"].astype("int64")

dados["Idade"] = dados["Idade"].clip(lower=0, upper=120)

# print(dados[(dados["Idade"] < 0) | (dados["Idade"] > 120)])


# Missão 4 - Padronizar Gênero
dict_genero = {
    "feminino": "f",
    "masculino": "m",
    "": "Não Informado",
    " ":"Não Informado",
    "N/A":"Não Informado"
}

dados["Sexo"] = dados["Sexo"].astype("str").str.strip().str.lower().replace(dict_genero).fillna("Não Informado").str.upper()


# Missão 5 - Padronizar Data

# Forma padrão, porém não suficiente para todas as datas
# dados["Data_Consulta"] = pd.to_datetime(dados["Data_Consulta"], errors="coerce", dayfirst=True)

# def converter_data(data):

#     try:
#         return pd.to_datetime(data, format="%d/%m/%Y")
#     except:
#         try:
#             return pd.to_datetime(data, format="%Y-%m-%d")
#         except:
#             return pd.NaT



# dados["Data_Consulta"] = dados["Data_Consulta"].str.strip().apply(converter_data)

# dados["Dia da Semana"] = dados["Data_Consulta"].dt.day_name()

# print(dados.sample(20).to_string())


# Missão 6 - Padronizar Especialidades

dados["Especialidade"] = dados["Especialidade"].astype("str").str.strip().str.upper().fillna("NÃO INFORMADO").replace([""," "], "NÃO INFORMADO").str.replace("_"," ")



# Missão 7 - Padronizar Retorno

dict_retorno = {
    "s": "Sim",
    "n": "Não",
    "si": "Sim",
    "na": "Não",
    "nã": "Não",
    "": "Não",
    " ": "Não"
}

dados["Retorno"] = dados["Retorno"].astype("str").str.strip().str.lower().replace(dict_retorno).fillna("Não").str.title()

dados.loc[(dados["Retorno"] != "Não") & (dados["Retorno"] != "Sim"), "Retorno"] = "Não"

print(dados["Retorno"].value_counts())


# Missão 8 - Remoção de duplicatas

# Consultar para verificar se a remoção de duplicados está selecionando linhas corretas
# print(dados[(dados.duplicated(subset=["Nome", "Data_Consulta", "Especialidade"] ,keep=False)) & (dados["Nome"] == "Juliana Santos")])

dados = dados.drop_duplicates(subset=["Nome", "Data_Consulta", "Especialidade"]).reset_index(drop=True)

print(dados.info())
