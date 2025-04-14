import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

st.set_page_config(page_title="CV", layout="centered")

st.title("CV")
st.subheader("Luiz Eduardo Prado de Oliveira")

st.markdown("---")

# Link do Google Drive com preview
pdf_google = "https://drive.google.com/file/d/1a6Ro_LGdcc9SrBPYjL2OB8ZD-TG4TLQl/preview"

# Exibe o PDF com iframe
components.html(f'''
    <iframe src="{pdf_google}" width="700" height="1000" allow="autoplay"></iframe>
''', height=1000)

# URL direta para o PDF (link raw do GitHub)
pdf_url = "https://raw.githubusercontent.com/LuizEduardoPrado/LuizPrado/main/LUIZ%20PRADO%20CV.pdf"

# Botão de download / abrir em nova aba
st.markdown(f"[📄 Clique aqui para abrir o PDF em nova aba]({pdf_url})")

st.markdown("---")
