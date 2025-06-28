import streamlit as st

st.set_page_config(page_title="Google Query Generator - Hondenhandel", layout="centered")
st.title("🔍 Google Query Generator – Opsporing Illegale Hondenhandel")

st.markdown("Vul hieronder in wat je zoekt, en klik op de link om direct in Google te zoeken binnen Marktplaats.")

ras = st.text_input("Ras (bijv. pomeriaan, toypoedel, maltezer)")
leeftijd = st.text_input("Leeftijd (bijv. 8 weken, 10 weken, jonger dan 15 weken)")
land = st.text_input("Herkomst of land (bijv. Roemenië, Bulgarije)")
verdacht = st.text_input("Verdachte termen (bijv. geen moeder, paspoort, ready to go)")

if st.button("Genereer zoekopdracht"):
    base = "site:marktplaats.nl"
    terms = [ras, leeftijd, land, verdacht]
    query = " ".join([f'"{t.strip()}"' for t in terms if t.strip()])
    url = f"https://www.google.com/search?q={base}+{query.replace(' ', '+')}"
    st.markdown(f"🔗 [Klik hier om te zoeken in Google]({url})", unsafe_allow_html=True)

