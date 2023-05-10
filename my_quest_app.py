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

#Liste des noms des colonnes : continent(pays), cubicinches(measure of the swept volume of all of the pistons in the bores),
#cylinders(cylindres), hp, mpg(miles per gallon), time-to-60(0 à 100km/h), weightlbs(masse), year(années)
#Mise en format date de la colonne year
#df_car["year"] = pd.to_datetime(df_car["year"]).dt.year
# Mise en format de la colonne contient
df_car['continent'] = df_car['continent'].str.replace('.', '')
# Création liste pays
pays = ["US", "Europe", "Japan"]

#Sidebar
def main():
	st.sidebar.header("Les filtres des pays ici :")
	pays_unique = df_car["continent"].unique()
	pays_choisi = st.sidebar.selectbox('Sélectionner un pays', pays_unique)
	#st.multiselect('Sélectionner les pays', df_selected_region.columns)
	df_select_pays = df_car[df_car['continent'] == pays_choisi]
	
	# afficher df
	st.dataframe(df_select_pays)
	
	# Afficher une analyse de corrélation
	st.header('Map de corrélation du dataframe complet.')
	fig1, ax = plt.subplots()
	sns.heatmap(df_car.corr(), center=0,cmap = sns.color_palette("vlag", as_cmap=True))
	st.pyplot(fig1)	
	st.markdown("On constate que 4 items sont fortement corrélés positivement entre eux. Ce sont les cylinders, les cubicinches, les hp et enfin les weightlbs.")
	st.write("Cela signifie que la puissance des voitures, la taille des moteurs, la consommation des voitures et leur masse sont corrélés. Cela est plutôt logique.)
	st.write("On constate une corrélation négative entre la consommation et l'année, ce qui signifie que les constructeurs ont tendance à faire des véhicules moins gourmands au fil des améliorations techniques.")
	st.write("Sans suprise, les véhicules plus lourds ont un moteur plus gros et une consommation supérieure aux plus légers.")

	
	# Ajouter un regplot de la relation entre puissance moteur et consommation
	#st.subheader('Relation entre puissance moteur et consommation')
	fig2, ax = plt.subplots()
	sns.regplot(x="hp", y="time-to-60", data=df_select_pays, ax=ax)
	st.pyplot(fig2)
	st.write("Nous ne serons pas étonnés de vérifier la forte corrélation entre la puissance et la taille du moteur et sa consommation en carburant.")
		
	#bar chart
	fig3, ax = plt.subplots()
	sns.histplot(df_car, x= "cylinders" , hue="year", multiple="stack", palette="light:m_r", edgecolor=".3", linewidth=.5, log_scale=True,)
	st.pyplot(fig3)
	
	#commentaires
	st.write("D'après l'histogramme de distribution, nous pouvons voir que :")
	st.write("Sur 261 véhicules, 125 sont en 4 cylindres ( 47,89 % ) , 55 en 6 cylindres (21 % ) et 76 en 8 cylindres (29 %)")
	st.write("Si la moyenne des tailles des moteurs est à 3291 cm³, c'est parce qu'il y a un fort déséquilibre entre les véhicules de la région US par rapport aux régions Japan et Europe.")
	st.write("Si les véhicules japonais sont souvent bien moins gourmands que la moyenne, les records de consommation se trouvent encore du côté de la région US")
	st.write("Enfin, il serait très intéressant d'avoir un plus grand jeu de données sur des véhicules plus récents afin de vérifier si nos prédictions de baisse de consommation sont réalisées.")
	
if __name__ == '__main__':
	main()
