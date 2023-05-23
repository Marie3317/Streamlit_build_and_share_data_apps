import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
#cylinders(cylindres), hp(horsepower), mpg(miles per gallon), time-to-60(0 à 100km/h), weightlbs(masse), year(années)

# Mise en format de la colonne contient
df_car['continent'] = df_car['continent'].str.replace('.', '')
# Création liste pays
pays = ["US", "Europe", "Japan"]

#Sidebar
def main():
	st.sidebar.header("Les filtres des continents ici :")
	pays_unique = df_car["continent"].unique()
	pays_choisi = st.sidebar.selectbox('Sélectionner un continent', pays_unique)
	df_select_pays = df_car[df_car['continent'] == pays_choisi]
	
	# Afficher df
	st.dataframe(df_select_pays)
	
	# Afficher map de corrélation
	st.header('Map de corrélation du dataframe complet.')
	fig1, ax = plt.subplots()
	sns.heatmap(df_car.corr(), center=0,cmap = sns.color_palette("vlag", as_cmap=True))
	st.pyplot(fig1)	
	st.markdown("On constate que 4 items sont fortement corrélés positivement entre eux. Ce sont les cylinders, les cubicinches, les hp et enfin les weightlbs.")
	st.write("Cela signifie que la puissance des voitures, la taille des moteurs, la consommation des voitures et leur masse sont corrélés. Cela est plutôt logique.")

	# Texte transition
	st.write("Les graphiques suivants vont explorer cette corrélation.")
	
	# Corrélation entre mpg et cubicinches
	st.header('Relation entre hp (horsepower) et cubicinches (taille des moteurs).')
	fig2, ax = plt.subplots()
	sns.regplot(x="cubicinches", y="hp", data=df_select_pays)
	st.pyplot(fig2)
	st.write("Il y a une forte corrélation entre le hp (horsepower) et le cubicinches (taille des moteurs). Les US possèdent une plus forte corrélation que le Japon ou bien l'Europe.")
		
	# Bar chart
	st.header("Relation entre weightlbs (poids moteur) et cylinders (puissance).")
	fig3, ax = plt.subplots()
	sns.histplot(df_select_pays, x= "weightlbs" , hue="cylinders", multiple="stack", palette="light:m_r", edgecolor=".3", linewidth=.5, log_scale=True,)
	st.pyplot(fig3)
	st.write("On s'apperçoit que plus le weightlbs (poids moteur) est important plus les cylinders (puissance) augmentent.")
	
	# Corrélation entre weightlbs et hp
	st.header("Relation entre hp (horse power) et cylinders (puissance).")
	fig4, ax = plt.subplots()
	sns.histplot(df_select_pays, x= "hp" , hue="cylinders", multiple="stack", palette="light:m_r", edgecolor=".3", linewidth=.5, log_scale=True,)
	st.pyplot(fig4)
	st.write("On s'apperçoit que plus le hp (horse power) est important plus les cylinders (puissance) augmentent.")
	
	# Texte transition
	st.write("Un petit apperçu des corrélations entre ces quatres items nous a permis de voir leurs liens.")
	st.write("A l'heure de la transition écologique, qu'en est-il de la consommation en mpg (miles per gallon ou xKM/100L) ?")	
	
	# Corrélation entre year et hp
	st.header('Evolution de la consommation des voitures au fil des ans.')
	fig5, ax = plt.subplots()
	sns.scatterplot(x="year", y="mpg", hue ="hp", data=df_select_pays)
	st.pyplot(fig5)
	st.write("On s'apperçoit que plus les années augmentent plus le mpg est élevé. La consommation d'une voiture diminue avec le temps.")
	
	st.write("Nous avons pu observer des corrélations et une piste d'évolution pour l'avenir.")
	st.write("Il nous manque des années et quelques données supplémentaires afin de passer d'une analyse de corrélation à une analyse des causes et des pistes d'avenir.")
if __name__ == '__main__':
	main()
