import streamlit as st
st.set_page_config(layout="wide", 
                    page_title="Data Hackers Challenge 2022 DashBoard",
                    page_icon="src/fav.png")

with open ('src/style.css') as f:
			st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

col1, col2, col3 = st.sidebar.columns([0.25,0.5,0.25])
col2.image("src/header.png", width=150)
st.sidebar.title("Challenge State of Data Brazil 2021")
st.sidebar.markdown("<p align='right' style='font-family:Trebuchet MS;'>Por Leonardo Valadão, 2022.</p>", True)

pages = ["Home", "Perfis", "Cargos", "Salários", "Tecnologias", "Os Melhores"]
page_selection = st.sidebar.selectbox("Escolha uma página:", pages)


st.image("src/dataset-cover.png")
st.title("Challenge State of Data Brazil 2021")
st.markdown("<p align='right' style='font-family:Trebuchet MS;'>Por Leonardo Valadão, 2022.</p>", True)

st.image("src/left-arrow.png", width=350) # Icon from https://www.flaticon.com/

st.markdown("Olá, viajante da internet! ")
st.markdown("Este site é dedicado aos resultados da pesquisa State of Data Brazil 2021, realizada pela Data Hackers. Os resultados estudados neste site foram feitos no contexto do desafio Challenge State of Data Brazil 2021, promovido também pela Data Hackers em 2022. ")
st.markdown("..........Onde podem ser encontrados os dados, link do data hackers, link do desafio..........")