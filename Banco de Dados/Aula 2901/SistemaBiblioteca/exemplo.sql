CREATE TABLE "Membro"(
    membro_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    membro_nome varchar(255) NOT NULL,
    membro_email varchar(255) NOT NULL,
    CONSTRAINT chk_email_valido CHECK(membro_email LIKE '%@%')
);



CREATE TABLE "Autores"(
    autores_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    autores_nome varchar(255) NOT NULL,
);




CREATE TABLE "Livros"(
    livros_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    livros_titulo varchar(255) NOT NULL,
    livros_ano_pub integer,
    autores_id integer,
    CONSTRAINT fk_livros_autores foreign KEY (autores_id) references "Autores" (autores_id)
);



CREATE TABLE "Emprestimo"(
    emp_id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_livro integer NOT NULL,
    id_membro integer NOT NULL,
    emp_data date NOT NULL default current_date,
    emp_devolucao date,
    CONSTRAINT fk_emp_livro foreign KEY (id_livro) references "Livro" (livros_id),
    CONSTRAINT fk_emp_membro foreign KEY (id_membro) references "Membro" (membro_id)
);