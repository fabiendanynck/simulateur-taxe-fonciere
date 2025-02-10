# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd

# Simulation des taux moyens de taxe foncière selon l'activité et la commune
data_tfpb = {
    "commune": ["Arras", "Lens", "Boulogne-sur-Mer", "Calais", "Saint-Omer"],
    "Commerce": [35, 38, 40, 37, 36],
    "Hôtellerie": [30, 32, 35, 33, 31],
    "Restauration": [33, 34, 36, 35, 32],
    "Industrie": [25, 28, 30, 27, 26],
    "Bureaux": [40, 42, 45, 41, 39]
}

df_tfpb = pd.DataFrame(data_tfpb)

def calculer_taxe(commune, activite, surface):
    taux = df_tfpb.loc[df_tfpb["commune"] == commune, activite].values[0]
    valeur_locative_m2 = 100  # Valeur locative fictive au m²
    valeur_locative_totale = valeur_locative_m2 * surface
    taxe_fonciere = (valeur_locative_totale * taux) / 100
    return taxe_fonciere

# Interface utilisateur avec Streamlit
st.title("Simulateur de Taxe Foncière Professionnelle")

# Sélection de la commune
commune = st.selectbox("Sélectionnez votre commune", df_tfpb["commune"].unique())

# Sélection de l'activité
activite = st.selectbox("Sélectionnez votre activité", df_tfpb.columns[1:])

# Saisie de la surface occupée
surface = st.number_input("Surface occupée en m²", min_value=1, max_value=10000, value=100)

# Calcul de la taxe foncière
if st.button("Calculer la taxe foncière"):
    taxe = calculer_taxe(commune, activite, surface)
    st.success(f"Montant estimé de votre taxe foncière : {taxe:.2f} €")

