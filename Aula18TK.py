# Carregar dados da base Loja, exibir a lista de vendas e exibir o total de vendas realizadas.

# Carregar dados
import baseLoja

lista_vendas = baseLoja.vendas["vendas"]

# Exibir a lista de Vendas
print("Lista de Vendas:")
print("ID | Produto | Categoria | Valor Unitário(R$) | Quantidade")

for venda in lista_vendas:
    print(f"{venda["id"]} | {venda["produto"]} | {venda["categoria"]} | R$ {venda["valor_unitario"]:.2f} | {venda["quantidade"]}")

# Produzir as métricas e exibi-las ao usuário:
print()
print("------- RESUMO ------")
# 1. Total e Média das vendas gerais

total_geral = 0
media_geral = 0

for venda in lista_vendas:
    total_geral += venda["quantidade"] * venda["valor_unitario"]

media_geral = total_geral/len(lista_vendas)
print(f"Total das vendas: R$ {total_geral:.2f}")
print(f"Ticket Médio: R$ {media_geral}")
print(f"Quantidade de Vendas: {len(lista_vendas)}")
#Exibir total de unidades vendidas
print(f"Total de Unidades Vendidas: {sum(venda['quantidade'] for venda in lista_vendas)}")


#Maior e Menor Venda
print("\n------- MAIOR E MENOR VENDA ------")
maior_venda = lista_vendas[0]["valor_unitario"] * lista_vendas[0]["quantidade"] 
menor_venda = lista_vendas[0]["valor_unitario"] * lista_vendas[0]["quantidade"] 

for venda in lista_vendas:
    total_venda = venda["quantidade"] * venda["valor_unitario"]

    if total_venda > maior_venda:
        maior_venda = total_venda

    if total_venda < menor_venda:
        menor_venda = total_venda

print(f"Maior Valor de Venda: R$ {maior_venda}")
print(f"Menor Valor de Venda: R$ {menor_venda}")

#Exibir o nome dos Vendedores
print("\n------- LISTA DE VENDEDORES ------")
lista_vendedores = []
print("Lista de Vendedores:")
for venda in lista_vendas:
    if venda["vendedor"] not in lista_vendedores:
        lista_vendedores.append(venda["vendedor"])

lista_vendedores.sort()
for vendedor in lista_vendedores:
    print(vendedor)

print(f"Quantidade de Vendedores: {len(lista_vendedores)}")

#Exibir o nome das Regiões
print("\n------- LISTA DAS REGIÕES ------")
lista_regioes = []
for venda in lista_vendas:
    if venda["regiao"] not in lista_regioes:
        lista_regioes.append(venda["regiao"])

lista_regioes.sort()

for contador, regiao in enumerate(lista_regioes):
    print(f"{contador+1}. {regiao}")
    

print(f"Quantidade de Regiões: {len(lista_regioes)}")


# 2. Total das vendas por categoria
print("\n------- VENDAS POR CATEGORIA ------")
categorias = {}
for venda in lista_vendas:
    categoria = venda["categoria"]
    total_venda = venda["quantidade"] * venda["valor_unitario"]
    if categoria in categorias:
        categorias[categoria] += total_venda
    else:
        categorias[categoria] = total_venda
print("Total das vendas por categoria:")
for categoria, total in categorias.items():
    print(f"- {categoria}: R$ {total:.2f}")

# 3. Total das vendas por vendedor
print("\n------- VENDAS POR VENDEDOR ------")
vendas_por_vendedor = {}    
for venda in lista_vendas:
    vendedor = venda["vendedor"]
    total_venda = venda["quantidade"] * venda["valor_unitario"]
    if vendedor in vendas_por_vendedor:
        vendas_por_vendedor[vendedor] += total_venda
    else:
        vendas_por_vendedor[vendedor] = total_venda 
print("Total das vendas por vendedor:")
for vendedor, total in vendas_por_vendedor.items(): 
    print(f"- {vendedor}: R$ {total:.2f}")  

# 4. Total das vendas por região
print("\n------- VENDAS POR REGIÃO ------")
vendas_por_regiao = {}
for venda in lista_vendas:
    regiao = venda["regiao"]
    total_venda = venda["quantidade"] * venda["valor_unitario"]
    if regiao in vendas_por_regiao:
        vendas_por_regiao[regiao] += total_venda
    else:
        vendas_por_regiao[regiao] = total_venda
print("Total das vendas por região:")
for regiao, total in vendas_por_regiao.items():
    print(f"- {regiao}: R$ {total:.2f}")


#Exibir a quantidade de vendas que superou a meta de venda de 5000 reais
print("\n------- VENDAS QUE SUPERARAM A META DE R$ 5000,00 ------")
meta_venda = 5000.00
vendas_que_superaram_meta = [venda for venda in lista_vendas if venda["quantidade"] * venda["valor_unitario"] > meta_venda]
print(f"Quantidade de vendas que superaram a meta de R$ {meta_venda:.2f}= {len(vendas_que_superaram_meta)}")
for venda in vendas_que_superaram_meta:
    total_venda = venda["quantidade"] * venda["valor_unitario"]
    print(f"- ID {venda['id']}: R$ {total_venda:.2f}")

    #teste