import streamlit as st

# Add custom CSS to hide the GitHub icon
hide_github_icon = """
#GithubIcon {
  visibility: hidden;
}
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)

st.set_page_config(
    page_title="Klasifikasi Persona Anak",
    page_icon="👋",
)

st.title('Klasifikasi Gaya Belajar Anak')
st.text('Selamat di aplikasi web untuk klasifikasi persona anak menggunakan child-based\npersona framework.')
st.text('Anda akan diminta untuk mengisi beberapa pertanyaan seputar kebutuhan, kemampuan\ndan pengalaman anak anda selama mengikuti kegiatan belajar mengajar baik \ndi rumah, di sekolah, atau di luar sekolah.')
st.text("\n")

