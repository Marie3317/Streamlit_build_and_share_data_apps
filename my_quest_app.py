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
	pays_unique = df_car["continent"].unique()
	pays_choisi = st.sidebar.selectbox('Sélectionner un pays', pays_unique)
	df_selected_region = df_car[df_car['continent'] == pays_choisi]
	
	# afficher df
	st.dataframe(df_car)
	
	# Afficher une analyse de corrélation
    	#st.subheader('Analyse de corrélation')
	viz_correlation = sns.heatmap(df_car.corr(), center=0,cmap = sns.color_palette("vlag", as_cmap=True))
	st.pyplot(viz_correlation.figure)	
		
	st.markdown("À partir de la carte thermique de corrélation, nous pouvons voir que la consommation des véhicules est fortement corrélée à leur puissance, leur masse et la taille de leur moteur. ")
	st.write("On constate une corrélation négative entre la consommation et l'année, ce qui signifie que les constructeurs ont tendance à faire des véhicules moins gourmands au fil des améliorations techniques.")
	st.write("Sans suprise, les véhicules plus lourds ont un moteur plus gros et une consommation supérieure aux plus légers.")

if __name__ == '__main__':
	main()
