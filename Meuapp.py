import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

st.set_page_config(page_title="CV", layout="centered")

st.title("CV")
st.subheader("Luiz Eduardo Prado de Oliveira")

st.markdown("---")

# URL direta para o PDF (link raw do GitHub)
pdf_google = "https://drive.google.com/file/d/1a6Ro_LGdcc9SrBPYjL2OB8ZD-TG4TLQl/view?usp=drive_link"

components.html(f'''
    <iframe src="{pdf_google}" width="700" height="1000" allow="autoplay"></iframe>
''', height=1000)

# Botão de download / abrir em nova aba
st.markdown(f"[📄 Clique aqui para abrir o PDF em nova aba]({pdf_url})")
