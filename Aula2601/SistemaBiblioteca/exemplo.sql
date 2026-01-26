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