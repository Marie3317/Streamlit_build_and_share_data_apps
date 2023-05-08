import pandas as pd
import seaborn as sns
import streamlit as st
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

#Affichage du DF
st.write(df_car)


#liste des noms des colonnes : continent, cubicinches, cylinders, hp, mpg, time-to-60, weightlbs, year
#mise en format date de la colonne year
df_car["year"] = pd.to_datetime(df_car["year"])

#Affichage d'une map de corrélation
st.write("Voici une map de corrélation.")
viz_correlation = sns.heatmap(df_car.corr(), center=0, cmap = sns.color_palette("vlag", as_cmap=True))
st.pyplot(viz_correlation.figure)
st.write("On peut s'appercevoir que cylinders, cubicinches, hp et weightlbs sont fortment corrélés.")



#Affichage d'un graph
st.write("Voici un graph global en fonction des continents.")
filter = st.multiselect('filter data', [df_car['continent'])
st.line_chart(df_car[df_car['continent'] == filter])         



#Affichage d'un graph mpg avec la liste des pays.
#Création d'un df avec juste mpg et pays
filter2 = st.selectbox('filter data', df_car['continent'].unique()], [df_car["year"].unique()])
st.write('You selected:', filter2)
st.bar_chart(df_car[df_car['contient'] == filter] | df_car[df_car['year'] == filter])

