# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd

# Simulation des taux moyens de taxe fonci�re selon l'activit� et la commune
data_tfpb = {
    "commune": ["Arras", "Lens", "Boulogne-sur-Mer", "Calais", "Saint-Omer"],
    "Commerce": [35, 38, 40, 37, 36],
    "H�tellerie": [30, 32, 35, 33, 31],
    "Restauration": [33, 34, 36, 35, 32],
    "Industrie": [25, 28, 30, 27, 26],
    "Bureaux": [40, 42, 45, 41, 39]
}

df_tfpb = pd.DataFrame(data_tfpb)

def calculer_taxe(commune, activite, surface):
    taux = df_tfpb.loc[df_tfpb["commune"] == commune, activite].values[0]
    valeur_locative_m2 = 100  # Valeur locative fictive au m�
    valeur_locative_totale = valeur_locative_m2 * surface
    taxe_fonciere = (valeur_locative_totale * taux) / 100
    return taxe_fonciere

# Interface utilisateur avec Streamlit
st.title("Simulateur de Taxe Fonci�re Professionnelle")

# S�lection de la commune
commune = st.selectbox("S�lectionnez votre commune", df_tfpb["commune"].unique())

# S�lection de l'activit�
activite = st.selectbox("S�lectionnez votre activit�", df_tfpb.columns[1:])

# Saisie de la surface occup�e
surface = st.number_input("Surface occup�e en m�", min_value=1, max_value=10000, value=100)

# Calcul de la taxe fonci�re
if st.button("Calculer la taxe fonci�re"):
    taxe = calculer_taxe(commune, activite, surface)
    st.success(f"Montant estim� de votre taxe fonci�re : {taxe:.2f} �")

