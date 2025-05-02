import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

st.set_page_config(page_title="CV", layout="centered")



st.title("CV")
st.subheader("Luiz Eduardo Prado de Oliveira")

st.markdown("---")

# Link do Google Drive com preview
pdf_portugues = "https://drive.google.com/file/d/1mZJAUdo3Vt7j4SdCU64Ar08aJAEgWU7n/preview"
pdf_google = "https://drive.google.com/file/d/1a6Ro_LGdcc9SrBPYjL2OB8ZD-TG4TLQl/preview"
pdf_ingles = "https://drive.google.com/file/d/1tcn9aDchDT4V74qHcigpif5yEX0T58QW/preview"

# URL direta para o PDF (link raw do GitHub)
pdf_url = "https://raw.githubusercontent.com/LuizEduardoPrado/LuizPrado/main/LUIZ%20PRADO%20CV.pdf"

# Botão de download / abrir em nova aba
# Link com ícone de PDF como "botão"
st.markdown(f'''
<a href="{pdf_url}" target="_blank" style="text-decoration: none;">
    <img src="https://cdn-icons-png.flaticon.com/512/337/337946.png" width="20" style="vertical-align: middle; margin-right: 8px;" />
    <span style="font-size: 16px; vertical-align: middle;">PDF [PT-BR]</span>
</a>
''', unsafe_allow_html=True)

linkedin_url = "https://www.linkedin.com/in/luiz-prado-3028ab248/"

st.markdown(f'''
<a href="{linkedin_url}" target="_blank" style="text-decoration: none;">
    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="20" style="vertical-align: middle; margin-right: 8px;" />
    <span style="font-size: 16px; vertical-align: middle;">LinkedIn</span>
</a>
''', unsafe_allow_html=True)


aba1, aba2 = st.tabs(["Português", "English"])

with aba1:
    # Exibe o PDF com iframe
    components.html(f'''
        <iframe src="{pdf_portugues}" width="700" height="1000" allow="autoplay"></iframe>
    ''', height=1000)

with aba2:
    # Exibe o PDF com iframe
    components.html(f'''
        <iframe src="{pdf_ingles}" width="700" height="1000" allow="autoplay"></iframe>
    ''', height=1000)
