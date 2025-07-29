# -instalando o streamlit-
import streamlit as st # type: ignore

st.title("Portfólio de Ualison Ramos Tomaz")
st.write("📊 Especialista em Dados e Processamento de Linguagem Natural")
st.write("💼 Experiência: Projetos em Python, FastAPI e NLP")
st.write("📂 GitHub: [seu-link-github](https://github.com/seuusuario)")

st.header("Sobre Mim")
st.write("""
    Olá, meu nome é Ualison Ramos Tomaz. Sou um entusiasta de dados e inteligência artificial, 
    com experiência na análise de dados e processamento de linguagem natural. Minha jornada começou 
    na área de tecnologia, onde me formei em Análise e Desenvolvimento de Sistemas. Atualmente, estou 
    aprofundando meus conhecimentos com um MBA em Análise de Dados.
    Eu sou apaixonado por transformar dados em insights valiosos para as empresas!
""")
#--Adicionando um "GitHub" ou "Projetos"--

st.header("Meus Projetos")
st.write("Confira alguns dos meus projetos desenvolvidos no GitHub:")

# Link para seu GitHub
st.markdown("[GitHub - Ualison](https://github.com/seuusuario)")

# Se quiser incluir diretamente os repositórios em seu portfólio:
st.write("**Exemplo de Projeto 1**")
st.write("Descrição do projeto 1")
st.markdown("[Repositório do Projeto 1](https://github.com/seuusuario/projeto1)")

st.write("**Exemplo de Projeto 2**")
st.write("Descrição do projeto 2")
st.markdown("[Repositório do Projeto 2](https://github.com/seuusuario/projeto2)")



#-- Adicionando Gráficos ou Análises de Dados--

import matplotlib.pyplot as plt

st.header("Análise de Dados")
st.write("Aqui está uma análise visual dos meus dados:")

# Exemplo de gráfico simples
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.title("Gráfico Exemplo")
plt.xlabel("X")
plt.ylabel("Y")
st.pyplot(plt)

#--Seção de Contato--

st.header("Entre em Contato")
st.write("""
    Caso queira saber mais sobre meus projetos ou discutir uma oportunidade de trabalho, 
    fique à vontade para entrar em contato!
""")

# Pode adicionar seu e-mail ou formulário de contato
st.markdown("[Email: ualison@exemplo.com](mailto:ualison@exemplo.com)")

#--Finalizando com um Rodapé e Links--

st.markdown("""
    ---
    Feito por [Ualison Ramos Tomaz](https://www.linkedin.com/in/ualisonramos/)
    """)
