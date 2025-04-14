import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

st.set_page_config(page_title="CV", layout="centered")

st.title("CV")
st.subheader("Luiz Eduardo Prado de Oliveira")

st.markdown("---")

# Link do Google Drive com preview
pdf_google = "https://drive.google.com/file/d/1a6Ro_LGdcc9SrBPYjL2OB8ZD-TG4TLQl/preview"

# URL direta para o PDF (link raw do GitHub)
pdf_url = "https://raw.githubusercontent.com/LuizEduardoPrado/LuizPrado/main/LUIZ%20PRADO%20CV.pdf"

# Botão de download / abrir em nova aba
st.markdown(f"[📄 Clique aqui para baixar o PDF]({pdf_url})")

linkedin_url = "https://www.linkedin.com/in/luiz-prado-3028ab248/"

st.markdown(f'''
<a href="{linkedin_url}" target="_blank" style="text-decoration: none;">
    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="20" style="vertical-align: middle; margin-right: 8px;" />
    <span style="font-size: 16px; vertical-align: middle;">LinkedIn</span>
</a>
''', unsafe_allow_html=True)

st.markdown("---")

# Exibe o PDF com iframe
components.html(f'''
    <iframe src="{pdf_google}" width="700" height="1000" allow="autoplay"></iframe>
''', height=1000)

st.markdown("---")
