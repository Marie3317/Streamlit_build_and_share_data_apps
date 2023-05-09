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

#Sidebar
st.sidebar.header("Les filtres des pays ici :")
pays = st.sidebar.multiselect(
    "Sélectionne le ou les pays :",
    options = df_car["continent"].unique())

df_car= df_car.query("continent == @pays")

st.dataframe(df_car)

# top mpg
total_mpg = int(df_car["mpg"].sum())
average_mpg = round(df_car["mpg"].mean(),2)

# Map corrélation
viz_correlation = sns.heatmap(df_weather.corr(), center=0, cmap = sns.color_palette("vlag", as_cmap=True))
viz_correlation.update_layout(figsize =(15,15))
st.pyplot(viz_correlation.figure)

# Bar chart
#fig_XX = px.bar(df_car, x = "mpg",
                #y = "year",
                #title = "<b> Titre <b>",
                #template = "plotly_white", )
#fig_XX.update_layout(plot_bgcolor = "rgba(0,0,0,0)")

#st.plotly_chart(fig_XX)

# Deux bar chart côte à côte
#left_column, right_column = st.columns(2)
#left_column.plotly_chart(fig_XX, use_container_width = True)
#right_column.plotly_chart(fig_YY, use_container_width = True)

# Pie chart
#pie_chart = px.pie(df_car, title = "pier_chart",
                   #values = "mpg",
                   #names = "   ")
#st.plotly_chart(pie_chart)
