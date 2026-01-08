import json

#Carregar dados de um JSON

with open("baseAcademia.json","r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

lista_alunos = dados["alunos"]

# 1. Exibir a lista de alunos contendo Nome | Mensalidade R$ | Tipo de Plano | Frequência
print("Lista de Alunos:")
for aluno in lista_alunos:
    nome = aluno["nome"]
    mensalidade = aluno["mensalidade"]
    tipo_plano = aluno["tipo_plano"]
    frequencia = aluno["frequencia"]
    print(f"- {nome} | Mensalidade: R$ {mensalidade:.2f} | Plano: {tipo_plano} | Frequência: {frequencia} vezes/semana")

# 2. Exibir total de mensalidade por mês da academia
# 3. Exibir a média de idade dos alunos da academia
# 4. Frequência total por tipo de plano da academia