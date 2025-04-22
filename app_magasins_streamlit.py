
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Titre de l'application
st.set_page_config(page_title="Carte des magasins", layout="wide")
st.title("🗺️ Carte interactive des magasins")

# Chargement des données
@st.cache_data
def load_data():
    df = pd.read_excel("Clients CA.xlsx", engine="openpyxl", skiprows=6)
    df = df.dropna(subset=["Nom Magasin", "Département", "Latitude", "Longitude"])
    return df

df = load_data()

# Filtre par département
departements = sorted(df["Département"].dropna().unique())
departement_selectionne = st.selectbox("📍 Choisis un département :", ["Tous"] + list(departements))

# Filtrage des données
if departement_selectionne != "Tous":
    df = df[df["Département"] == departement_selectionne]

# Création de la carte
m = folium.Map(location=[48.5, 3.5], zoom_start=7)

for _, row in df.iterrows():
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=row["Nom Magasin"],
        icon=folium.Icon(color="blue", icon="shopping-cart", prefix="fa"),
    ).add_to(m)

# Affichage de la carte
st_folium(m, width=1000, height=600)
