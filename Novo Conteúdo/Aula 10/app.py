#pip install streamlit

import streamlit as st

#Header 1
st.title("Hello World!")

#Text
st.write("Teste")

#Cabeçalhos
st.header("Início da Seção")

st.subheader("Subtítulo da Seção")

st.markdown("Texto estilizado")

#Interação

nome = st.text_input("Digite seu nome:")
idade = st.number_input(
    "Digite sua idade:",
    min_value=0,
    max_value=120,
    step=1,
    value=None
)

#Exibir na tela o nome e a idade digitados
#print(nome,idade)
#print(f'''       Nome: {nome}       Idade: {idade}      ''')

#Bônus: Exibir um trecho que informa se a pessoa é maior ou menor de idade

if nome == "":
    st.write("Nome Vazio!")

elif idade is not None:

    st.write(f'''
    Nome: {nome}    
    Idade: {idade}
    ''')

    if idade >= 18:
        st.success("Maior de idade!")
    else:
        st.warning("Menor de idade")


#Rodar no terminal o comando "streamlit run app.py"