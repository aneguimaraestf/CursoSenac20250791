import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

NUM_TURMAS = 100
ALUNOS_BASE = 800

# -----------------------------
# CURSOS
# -----------------------------
cursos = [
    {"nome": "Python para Análise de Dados", "preco": 1800},
    {"nome": "Excel Avançado", "preco": 900},
    {"nome": "Power BI Completo", "preco": 1500},
    {"nome": "SQL para Banco de Dados", "preco": 1200},
    {"nome": "Marketing Digital", "preco": 1100},
    {"nome": "Gestão de Projetos", "preco": 2000},
    {"nome": "Data Science", "preco": 3500},
    {"nome": "Machine Learning", "preco": 4000},
]

# -----------------------------
# NOMES
# -----------------------------
nomes = ["Ana", "Carlos", "Mariana", "João", "Fernanda", "Lucas", "Juliana", "Rafael", "Camila", "Bruno"]
sobrenomes = ["Silva", "Souza", "Oliveira", "Santos", "Costa", "Pereira", "Rodrigues", "Almeida", "Nascimento", "Lima"]

def gerar_nome():
    return f"{random.choice(nomes)} {random.choice(sobrenomes)}"

# -----------------------------
# ESCOLARIDADE
# -----------------------------
escolaridades = [
    "Ensino Fundamental",
    "Ensino Médio",
    "Curso Técnico",
    "Ensino Superior",
    "Pós-graduação"
]

# -----------------------------
# STATUS DO ALUNO
# -----------------------------
status_aluno = [
    "Matricula Cancelada", "Aprovado", "Reprovado", "Participante",
    "Em Processo", "Evadido", "Desistente", "Anulada",
    "Transferência Interna mesmo Título", "Matrícula Trancada",
    "Matricula não Confirmada", "Matriculado"
]

# -----------------------------
# FUNÇÕES
# -----------------------------
def data_aleatoria(inicio, fim):
    return inicio + timedelta(days=random.randint(0, (fim - inicio).days))

def gerar_data_nascimento():
    hoje = datetime.today()
    idade = random.randint(18, 60)
    return hoje - timedelta(days=idade * 365 + random.randint(0, 365))

def gerar_situacao(estado_turma):
    if estado_turma == "Encerrada":
        return random.choices(["Concluído", "Cancelado"], weights=[75, 25])[0]
    elif estado_turma == "Ativa":
        return random.choices(["Ativo", "Cancelado"], weights=[80, 20])[0]
    else:
        return "Ativo"

# -----------------------------
# BASE DE ALUNOS (FIXA)
# -----------------------------
alunos = []
for i in range(ALUNOS_BASE):
    alunos.append({
        "id": i,
        "Nome do Aluno": gerar_nome(),
        "Sexo": random.choice(["F", "M"]),
        "Data de Nascimento": gerar_data_nascimento(),
        "Escolaridade": random.choice(escolaridades)
    })

df_alunos = pd.DataFrame(alunos)

# -----------------------------
# GERAÇÃO
# -----------------------------
linhas = []

for turma_id in range(1, NUM_TURMAS + 1):

    curso = random.choice(cursos)

    nome_turma = f"{curso['nome']} - Turma {turma_id}"
    preco_base = curso["preco"]

    data_criacao = data_aleatoria(datetime(2022,1,1), datetime(2024,12,31))
    data_inicio = data_criacao + timedelta(days=random.randint(15, 60))
    data_termino = data_inicio + timedelta(days=random.randint(30, 120))

    estado_turma = random.choice(["Ativa", "Encerrada", "Planejada"])

    if preco_base > 3000:
        num_alunos = random.randint(15, 20)
    elif preco_base > 2000:
        num_alunos = random.randint(18, 25)
    else:
        num_alunos = random.randint(22, 30)

    vagas = num_alunos + random.randint(0, 10)

    turma_info = {
        "Código da Turma": turma_id,
        "Nome da Turma": nome_turma,
        "Sigla": f"T{turma_id:03d}",
        "Data de Criação": data_criacao,
        "Data Início": data_inicio,
        "Data Término": data_termino,
        "Vagas Disponíveis": vagas,
        "Matrículas": num_alunos,
        "Reservas": random.randint(0, 5),
        "Centro de Custo": f"CC{random.randint(100,999)}",
        "Recurso Financeiro": random.choice(["Próprio", "Terceiros"]),
        "Código do Projeto": f"PRJ{random.randint(1000,9999)}",
        "Unidade Operativa": random.choice(["Unidade A", "Unidade B", "Unidade C"]),
        "CH": random.randint(40, 180),
        "Dias de Execução": random.choice(["Seg-Sex", "Fins de Semana"]),
        "Horário": random.choice(["Manhã", "Tarde", "Noite"]),
        "Estado da Turma": estado_turma,
        "Local": random.choice(["Sala 1", "Sala 2", "Online"]),
        "Pré-requisitos": random.choice(["Nenhum", "Básico", "Intermediário"]),
        "Segmento": "Tecnologia",
        "Formas de Pagamento": random.choice(["Cartão", "Boleto", "Pix"]),
        "Valor Turma": preco_base,
        "Valores Ofertas": round(preco_base * random.uniform(0.7, 0.95), 2),
        "Impresso por": "Sistema",
        "Data da Impressão": data_aleatoria(data_inicio, data_termino)
    }

    alunos_sorteados = df_alunos.sample(num_alunos)

    for _, aluno in alunos_sorteados.iterrows():

        data_matricula = data_aleatoria(data_criacao, data_inicio)
        situacao = gerar_situacao(estado_turma)

        if situacao == "Cancelado":
            data_ocorrencia = data_inicio + timedelta(days=random.randint(1, 15))
        elif situacao == "Concluído":
            data_ocorrencia = data_termino
        else:
            data_ocorrencia = data_aleatoria(data_matricula, data_termino)

        linha = {
            **turma_info,

            "Matrícula": random.randint(100000, 999999),
            "Nome do Aluno": aluno["Nome do Aluno"],
            "Sexo": aluno["Sexo"],
            "Data de Nascimento": aluno["Data de Nascimento"],
            "Escolaridade": aluno["Escolaridade"],

            "Data da Matrícula": data_matricula,
            "Estado": random.choice(status_aluno),
            "Data de Ocorrência": data_ocorrencia,
            "Contrato da Matrícula": f"CTR{random.randint(10000,99999)}",
            "Situação do Contrato": situacao
        }

        linhas.append(linha)

df = pd.DataFrame(linhas)

df.to_excel("base_final_completa.xlsx", index=False)

print("Base completa e profissional!")
print(df.shape)