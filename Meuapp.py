import streamlit as st
from PIL import Image

st.set_page_config(page_title="CV", layout="centered")

st.title("CV")
st.subheader("Luiz Eduardo Prado de Oliveira")

st.markdown("---")

# Função para copiar texto (simula com st.code)
def copy_box(title, content):
    with st.expander(title):
        st.code(content, language='text')



# --- Runas ---
st.header("🌿 Runas Recomendadas (Pós-Choque)")
st.image("https://opgg-static.akamaized.net/meta/images/lol/perk/8439.png", width=50)  # Pós-Choque

runas_texto = """
Pós-Choque • Golpe de Escudo • Osso Revestido • Crescimento Excessivo  
Fonte da Vida • Perspicácia Cósmica
"""
copy_box("Copiar Runas", runas_texto)

# --- Itens Principais ---
st.header("🛡️ Itens Principais")
itens_principais = [
    ("Juramento do Cavaleiro", "https://opgg-static.akamaized.net/meta/images/lol/item/3109.png"),
    ("Convergência de Zeke", "https://opgg-static.akamaized.net/meta/images/lol/item/3050.png"),
    ("Medalhão dos Solari de Ferro", "https://opgg-static.akamaized.net/meta/images/lol/item/3190.png"),
]

cols = st.columns(len(itens_principais))
for col, (nome, img) in zip(cols, itens_principais):
    col.image(img, width=64)
    col.caption(nome)

itens_texto = "Juramento do Cavaleiro, Convergência de Zeke, Medalhão dos Solari de Ferro"
copy_box("Copiar Itens", itens_texto)

# --- Itens Situacionais ---
st.header("🧰 Itens Situacionais")
itens_situacionais = [
    ("Putrificador Quimtec", "https://opgg-static.akamaized.net/meta/images/lol/item/3011.png"),
    ("Força da Natureza", "https://opgg-static.akamaized.net/meta/images/lol/item/3111.png"),
    ("Placa Gargolítica", "https://opgg-static.akamaized.net/meta/images/lol/item/3193.png"),
]

cols2 = st.columns(len(itens_situacionais))
for col, (nome, img) in zip(cols2, itens_situacionais):
    col.image(img, width=64)
    col.caption(nome)

# --- Botas ---
st.header("🥾 Botas Recomendadas")
st.image("https://opgg-static.akamaized.net/meta/images/lol/item/3117.png", width=50)
st.caption("Botas da Mobilidade")

# --- Dicas Extras ---
st.markdown("---")
st.subheader("📌 Dicas Rápidas")
st.markdown("""
- Sempre tenha visão com as **Sentinelas de Controle**.
- Use o **Q (Sentença)** com paciência para pegar inimigos fora de posição.
- O **E (Esfolar)** pode ser usado para interromper dashes e canais.
- O **W (Passagem Sombria)** salva aliados com um bom timing.
""")

st.markdown("---")
st.markdown("Nada ave")
