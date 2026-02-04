# Missão 1: Preparação do Ambiente
import pandas as pd
import numpy as np
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

dados = pd.read_excel("vendas.xlsx", engine="openpyxl")

#print(dados)


# ******************************************************************************
# Missão 2: Criar Coluna de Valor de Venda
dados["valor_venda"] = dados["quantidade"]*dados["preco_unitario"]
#print(dados)


# ******************************************************************************
# Missão 3: Classificar o Nível da Venda
def classificar_venda(valor):
    if valor >= 500:
        return "Alto"
    elif valor < 100:
        return "Baixo"
    elif valor >= 100 and valor <=500:
        return "Médio"
    else:
        return "INVÁLIDA"

dados["nivel_venda"] = dados["valor_venda"].apply (classificar_venda)
#print(dados.to_string())


# ******************************************************************************
# Missão 4: Calcular o Imposto
def classificar_imposto(venda):
    if venda > 300:
        return 0.15
    elif venda <= 300:
        return 0.10
    else:
        return 0
    
dados["imposto"] = dados["valor_venda"].apply (classificar_imposto)
dados["imposto_pago"] = (dados["valor_venda"] * dados["imposto"]).round(2)
#print(dados.to_string())


# ******************************************************************************
# Missão 5: Calcular o Valor Líquido
dados["valor_liquido"] = dados["valor_venda"] - dados["imposto_pago"]
#print(dados)


# ******************************************************************************
# Missão 6: Categorizar a Idade dos Clientes
def classificar_faixas(idade):
    if idade < 30:
        return "Jovem"
    elif idade >= 50:
        return "Sênior"
    elif idade >= 30 and idade <= 49:
        return "Adulto"
    else:
        return "INVÁLIDA"
  
dados["faixa_etaria"] = dados["idade"].apply (classificar_faixas)  
print(dados)


# ******************************************************************************
# Missão 7: Agregações Gerais
bruta = dados["valor_venda"].sum()
print(f"Total de Vendas Brutas: {locale.currency(bruta, grouping=True)}")

liquida = dados["valor_liquido"].sum()
print(f"Total de Vendas Líquidas: {locale.currency(liquida, grouping=True)}")

imposto = dados["imposto_pago"].sum()
print(f"Total de Impostos: {locale.currency(imposto, grouping=True)}")

venda = len(dados)
print(f"Número Total de Vendas: {venda}")

vendedores_unicos = dados["vendedor"].nunique()
print(f"Número de Vendedores Unicos: {vendedores_unicos}")

clientes_unicos = dados["cliente"].nunique()
print(f"Número de Clientes Unicos: {clientes_unicos}")

media_venda = dados["valor_venda"].mean()
print(f"Média do Valor da Venda: {locale.currency(media_venda, grouping=True)}")

ticket = dados["valor_liquido"].mean() 
print(f"Ticket Médio: {locale.currency(ticket, grouping=True)}")



# ******************************************************************************
# Missão 8: Análises por Agrupamento
faturamento_vendedor = (dados.groupby('vendedor').agg(
        total_valor_venda=('valor_venda', 'sum'),
        total_valor_liquido=('valor_liquido', 'sum'),
        total_imposto=('imposto', 'sum'),
        qtd_vendas=('valor_venda', 'count')
    )
    .reset_index())

for col in ['total_valor_venda', 'total_valor_liquido', 'total_imposto']:
    faturamento_vendedor[col] = faturamento_vendedor[col].apply(
        lambda x: locale.currency(x, grouping=True))

print(f"Faturamento por Vendedor: \n {faturamento_vendedor}")



faturamento_nivel_venda = (dados.groupby('nivel_venda').agg(
        total_valor_venda=('valor_venda', 'sum'),
        total_valor_liquido=('valor_liquido', 'sum'),
        total_imposto=('imposto', 'sum'),
        qtd_vendas=('valor_venda', 'count')
    )
    .reset_index())

for col in ['total_valor_venda', 'total_valor_liquido', 'total_imposto']:
    faturamento_nivel_venda[col] = faturamento_nivel_venda[col].apply(
        lambda x: locale.currency(x, grouping=True))

print(f"Faturamento por Nível da Venda: \n {faturamento_nivel_venda}")


faturamento_faixa_etaria = (dados.groupby('faixa_etaria').agg(
        total_valor_venda=('valor_venda', 'sum'),
        total_valor_liquido=('valor_liquido', 'sum'),
        total_imposto=('imposto', 'sum'),
        qtd_vendas=('valor_venda', 'count')
    )
    .reset_index())

for col in ['total_valor_venda', 'total_valor_liquido', 'total_imposto']:
    faturamento_faixa_etaria[col] = faturamento_faixa_etaria[col].apply(
        lambda x: locale.currency(x, grouping=True)
    )

print(f"Faturamento por Faixa Etária: \n {faturamento_faixa_etaria}")




# ******************************************************************************
# Missão Final: Exportar para Excel com Múltiplas Planilhas

# Criar um ExcelWriter para salvar múltiplas planilhas
with pd.ExcelWriter('analise_vendas_final.xlsx', engine='openpyxl') as writer:
    # Planilha 1: Dados completos
    dados.to_excel(writer, sheet_name='Dados', index=False)

    # Planilha 2: Resumo das análises
    # Criar um DataFrame de resumo
    resumo_data = {
        'Métrica': [
            'Total Vendas Brutas',
            'Total Vendas Líquidas',
            'Total Impostos',
            'Número Total de Vendas',
            'Número de Vendedores Únicos',
            'Número de Clientes Únicos',
            'Ticket Médio Bruto',
            'Ticket Médio Líquido'
        ],
        'Valor': [
            dados['valor_venda'].sum(),
            dados['valor_liquido'].sum(),
            dados['imposto'].sum(),
            dados.shape[0],
            dados['vendedor'].nunique(),
            dados['cliente'].nunique(),
            dados['valor_venda'].mean(),
            dados['valor_liquido'].mean()
        ]
    }

    resumo_dados = pd.DataFrame(resumo_data)
    resumo_dados.to_excel(writer, sheet_name='Resumo', index=False)

    # Adicionar mais abas com os agrupamentos (opcional)
    faturamento_vendedor = dados.groupby('vendedor').agg({
        'valor_venda': 'sum',
        'valor_liquido': 'sum',
        'imposto': 'sum',
        'id_venda': 'count'
    }).rename(columns={'id_venda': 'Qtd_Vendas'})

    faturamento_vendedor.to_excel(writer, sheet_name='Por Vendedor')

print("Arquivo 'analise_vendas_final.xlsx' salvo com sucesso!")
print("Contém 3 planilhas: Dados, Resumo e Por Vendedor")




