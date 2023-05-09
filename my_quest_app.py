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

#Sidebar
def main():
	st.sidebar.header("Les filtres des pays ici :")
	pays = st.sidebar.multiselect("Sélectionne le ou les pays :", options = df_car["continent"].unique())


# Affichage df
	st.dataframe(df_car)

if __name__ == '__main__':
	main()
	
	
# Map corrélation
	viz_correlation = sns.heatmap(df_car.corr(), center=0,cmap = sns.color_palette("vlag", as_cmap=True))
	st.pyplot(viz_correlation.figure)


# Bar chart
	fig, ax = plt.subplots(1,1)
	ax.scatter(df_car["hp"], df_car["time-to-60"])
	ax.set_xlabel("Année")
	ax.set_ylabel("mpg")
	fig.suptitle("mpg/année")
	st.pyplot(fig)

# 
	fig2, ax = plt.subplots(1,1)
	ax.plot(df_car["year"], df_car["cubicinches"])
	ax.set_xlabel("Année")
	ax.set_ylabel("cubicinches")
	fig2.suptitle("mpg/année")
	st.pyplot(fig2)

#
