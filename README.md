import streamlit as st
import pandas as pd

st.set_page_config(page_title="PupRadar - Onderzoek Hondenhandel", layout="wide")

st.title("🐾 PupRadar – Illegale hondenhandel opsporen")
st.write("Voer hier handmatig advertenties in of analyseer verdachte kenmerken.")

st.subheader("📋 Voeg een advertentie toe")
with st.form("add_ad"):
    titel = st.text_input("Titel advertentie")
    beschrijving = st.text_area("Beschrijving")
    telefoon = st.text_input("Telefoonnummer")
    locatie = st.text_input("Plaats")
    prijs = st.number_input("Prijs (€)", min_value=0)
    leeftijd = st.number_input("Leeftijd pup (in weken)", min_value=0)
    submitted = st.form_submit_button("Toevoegen")
    if submitted:
        st.session_state.get("data", []).append({
            "Titel": titel, "Beschrijving": beschrijving,
            "Telefoon": telefoon, "Locatie": locatie,
            "Prijs": prijs, "Leeftijd": leeftijd
        })
        st.success("Toegevoegd.")

st.subheader("🔎 Advertentie-overzicht en analyse")
data = pd.DataFrame(st.session_state.get("data", []))
if not data.empty:
    st.dataframe(data)

    st.markdown("### 🚨 Mogelijke verdachte patronen")
    dupes = data[data.duplicated("Telefoon", keep=False)]
    jonge_pups = data[data["Leeftijd"] < 15]
    if not dupes.empty:
        st.warning("Meerdere advertenties met hetzelfde telefoonnummer:")
        st.dataframe(dupes)
    if not jonge_pups.empty:
        st.warning("Pups jonger dan 15 weken (mogelijk illegale import):")
        st.dataframe(jonge_pups)

    st.download_button("📥 Download als CSV", data.to_csv(index=False), "pup_data.csv", "text/csv")
else:
    st.info("Nog geen advertenties ingevoerd.")
