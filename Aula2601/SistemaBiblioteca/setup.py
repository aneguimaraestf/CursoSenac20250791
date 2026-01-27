# Missões da Atividade

# 1. Criar as tabelas Autores, Livros, Membros e Empréstimo

# 2. Inserir pelo menos 10 Autores
# 3. Inserir pelo menos 20 Livros
# 4. Inserir pelo menos 5 membros
# 5. Inserir pelo menos 20 empréstimos válidos

# (Usar IA para gerar os dados)

# 6. Realizar a modificação do nome de um Membro
# 7. Remover um livro que comece com a letra "A"
# 8. Remover um empréstimo em que a data de devolução seja nula (se houver)
# 9. Modificar a data de devolução de um empréstimo para o dia de hoje

# 10. Exibir a lista de membros
# 11. Exibir a lista de livros
# 12. Exibir a lista de empréstimos, mostrando nome do livro e nome do membro
  


#Abrir o terminal e executar o comando 'pip install psycopg2'
import psycopg2
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())

DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

try:
    #Estabelece a conexão com o banco
    con = psycopg2.connect(
        dbname = DB_NAME,
        host = DB_HOST,
        port = DB_PORT,
        user = DB_USER,
        password = DB_PASSWORD
    )
    #Cria a ferramenta de interação com o banco
    cursor = con.cursor()

    #Código SQL

    #Remove as tabelas já existentes
    cursor.execute('''
    DROP TABLE IF EXISTS "Emprestimo";
''')
    cursor.execute('''
    DROP TABLE IF EXISTS "Membro";
''')
    cursor.execute('''
    DROP TABLE IF EXISTS "Livro";
''')
    cursor.execute('''
    DROP TABLE IF EXISTS "Autor";
''')
    print("TABELAS REMOVIDAS COM SUCESSO!")
    con.commit()

    #Criar a tabela de Membros (SQL)
    cursor.execute('''
    CREATE TABLE "Membro"(
    membro_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    membro_nome varchar(255) NOT NULL,
    membro_email varchar(255) NOT NULL,
    CONSTRAINT chk_email_valido CHECK(membro_email LIKE '%@%')
);
    ''')
    print("Tabela Membro Criada Com Sucesso!")

    cursor.execute('''
    CREATE TABLE "Autor"(
    autor_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    autor_nome varchar(255) NOT NULL
);
''')
    print("Tabela Autor Criada Com Sucesso!")
    
    cursor.execute('''
    CREATE TABLE "Livro"(
    livro_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    livro_titulo varchar(255) NOT NULL,
    livro_ano integer NOT NULL,
    id_autor integer NOT NULL,
    CONSTRAINT fk_livro_autor 
    FOREIGN KEY (id_autor) 
    REFERENCES "Autor"(autor_id)
);

''')
    
    print("Tabela Livro Criada Com Sucesso!")

    cursor.execute('''
CREATE TABLE "Emprestimo"(
    emp_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_livro integer NOT NULL,
    id_membro integer NOT NULL,
    emp_data date NOT NULL DEFAULT CURRENT_DATE,
    emp_devolucao date,
    CONSTRAINT fk_emp_livro FOREIGN KEY (id_livro) REFERENCES "Livro"(livro_id),
    CONSTRAINT fk_emp_membro FOREIGN KEY (id_membro) REFERENCES "Membro"(membro_id)
);
''')
    
    print("Tabela Empréstimo Criada Com Sucesso!")
    con.commit()

    print("Tabelas Criadas com Sucesso!")


    print("PREENCHENDO TABELAS DO BANCO...")

    cursor.execute('''
    INSERT INTO "Autor" (autor_nome) VALUES
    ('Machado de Assis'), 
    ('Clarice Lispector'), 
    ('George Orwell'), 
    ('J.K. Rowling'),
    ('J.R.R. Tolkien'), 
    ('Agatha Christie'), 
    ('Paulo Coelho'), 
    ('Graciliano Ramos'),
    ('Stephen King'), 
    ('C.S. Lewis')
''')
    con.commit()



    cursor.execute('''
INSERT INTO "Livro" (livro_titulo, livro_ano, id_autor) VALUES
('Dom Casmurro', 1899, 1),
('Memórias Póstumas de Brás Cubas', 1881, 1),

('A Hora da Estrela', 1977, 2),
('Perto do Coração Selvagem', 1943, 2),

('1984', 1949, 3),
('A Revolução dos Bichos', 1945, 3),

('Harry Potter e a Pedra Filosofal', 1997, 4),
('Harry Potter e a Câmara Secreta', 1998, 4),

('O Hobbit', 1937, 5),
('O Senhor dos Anéis: A Sociedade do Anel', 1954, 5),

('Assassinato no Expresso do Oriente', 1934, 6),
('E Não Sobrou Nenhum', 1939, 6),

('O Alquimista', 1988, 7),
('Brida', 1990, 7),

('Vidas Secas', 1938, 8),
('São Bernardo', 1934, 8),

('Carrie', 1974, 9),
('O Iluminado', 1977, 9),

('As Crônicas de Nárnia: O Leão, a Feiticeira e o Guarda-Roupa', 1950, 10),
('Cartas de um Diabo a Seu Aprendiz', 1942, 10);
''')

    con.commit()



    
except Exception as error:
    print(f"HOUVER UM ERRO AO OPERAR O BANCO DE DADOS! ERRO: {error} ")
finally:
    #IMPORTANTE FECHAR AS CONEXÕES AO FINALIZAR A CONSULTA
    cursor.close()
    con.close()





