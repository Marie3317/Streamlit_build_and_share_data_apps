import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

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

#Création liste pour pays
liste_pays = list(df_car["continent"].unique())

#Affichage d'une map de corrélation
st.write("Voici une map de corrélation.")
viz_correlation = sns.heatmap(df_car.corr(), center=0, cmap = sns.color_palette("vlag", as_cmap=True))

st.pyplot(viz_correlation.figure)
######

st.area_chart(df_car)


#####

#Affichage d'un graph mpg avec la liste des pays
# Now this will show the filtered row in the dataframe as you change the inputs
filter = st.selectbox('filter data', df_car['continent'].unique())
st.line_chart(df_car[df_car['continent'] == filter])


#######

