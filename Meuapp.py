import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

st.set_page_config(page_title="CV", layout="centered")

st.title("CV")
st.subheader("Luiz Eduardo Prado de Oliveira")

st.markdown("---")

# URL direta para o PDF (link raw do GitHub)
pdf_url = "https://raw.githubusercontent.com/LuizEduardoPrado/LuizPrado/main/LUIZ%20PRADO%20CV.pdf"

# Exibe o PDF com iframe
components.html(f'''
    <iframe src="{pdf_url}" width="700" height="1000" type="application/pdf"></iframe>
''', height=1000)

# Botão de download / abrir em nova aba
st.markdown(f"[📄 Clique aqui para abrir o PDF em nova aba]({pdf_url})")
