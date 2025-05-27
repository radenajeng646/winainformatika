import streamlit as st

st.title("🩷 I love lowinn")
st.write(
    "lowin is tthe best guyss"
)
st.image("#Pak_Solomon.jpeg")
st.title("Aplikasi Sederhana")
st.header("aplikasi Mengecek Nilai Genap/ Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st.write(f"{angka} adalah Bilangan Ganjil")
