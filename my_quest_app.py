import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import datetime

# Configuration de la page
st.set_page_config(
    page_title="Quête WildCodeSchool",
    layout="wide",
    page_icon="📐")
# titre
st.title('Hello Wilders, welcome to my application!')

#Sous_titre
st.write("I enjoy to discover streamlit possibilities")

#Sous_titre2
st.write("Voici le DF avec lequel je vais travailler.")

#Téléchargement du DF
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_car = pd.read_csv(link)

#Liste des noms des colonnes : continent, cubicinches, cylinders, hp, mpg, time-to-60, weightlbs, year
#Mise en format date de la colonne year
df_car["year"] = pd.to_datetime(df_car["year"]).dt.year
df_car['continent'] = df_car['continent'].str.replace('.', '')
pays = ["US", "Europe", "Japan"]

#Sidebar
def main():
	st.sidebar.header("Les filtres des pays ici :")
	pays_unique = df["continent"].unique()
	pays_choisi = st.sidebar.selectbox('Sélectionner un pays', pays_unique)
	df_selected_region = df_car[df_car['continent'] == pays_choisi]
	

if __name__ == '__main__':
	main()
