import requests
import pandas as pd

# Faça uma requisição da api do IMDB e crie uma tabela com os 50 melhores filmes de todos os tempos de um gênero a sua escolha. Guarde os resultados em uma tabela excel que contenha Titulo, Ano Lançamento, Nota do Filme, Quantidade de Votos

respostas = requests.get("https://api.imdbapi.dev/titles")

listaFilmes = respostas.json()["titles"]

colecaoFilmes = []

for filme in listaFilmes:
    if filme["titleType"] != "movie":
        continue

    nome = filme["primaryTitle"]
    anoLancamento = filme["startYear"]
    nota = filme.get("averageRating", None)
    votos = filme.get("numVotes", None)

    dadosFilme = {
        "Titulo": nome,
        "Ano Lancamento": anoLancamento,
        "Nota do Filme": nota,
        "Quantidade de Votos": votos
    }

    colecaoFilmes.append(dadosFilme)

    if len(colecaoFilmes) == 50:
        break

df = pd.DataFrame(colecaoFilmes)

df.to_excel("filmes.xlsx", index=False)

print("Arquivo Excel criado com sucesso!")

