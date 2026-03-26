import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import json
import urllib.request
warnings.filterwarnings('ignore')

print("Bibliotheques importees")

# ==================================================
# EXERCICE 1 - Introduction a l'Analyse de Donnees
# ==================================================

"""
Qu'est-ce que l'analyse de donnees ?
L'analyse de donnees est le processus d'inspection, de nettoyage et de
transformation de donnees brutes pour decouvrir des informations utiles
et soutenir la prise de decision.

Pourquoi est-elle importante ?
- Remplace les intuitions par des preuves concretes
- Permet de predire des tendances futures
- Optimise les performances des entreprises
- Personnalise l'experience utilisateur

3 domaines d'application :
1. Sante : Detection precoce de maladies grace a l'analyse de dossiers medicaux
2. Finance : Detection de fraudes en temps reel, evaluation des risques
3. Commerce : Recommandations personnalisees comme Amazon et Netflix
"""

print("Exercice 1 termine")

# ==================================================
# EXERCICE 2 - Chargement des datasets
# ==================================================

# Dataset 1 : Sleep
np.random.seed(42)
sleep_data = pd.DataFrame({
    'Age': np.random.randint(18, 80, 200),
    'Gender': np.random.choice(['Male', 'Female'], 200),
    'Sleep_Hours': np.round(np.random.normal(6.8, 1.2, 200), 1),
    'Work_Hours': np.random.randint(20, 60, 200),
    'Health_Status': np.random.choice(['Excellent', 'Good', 'Fair', 'Poor'], 200),
    'Has_Insomnia': np.random.choice([True, False], 200),
    'Region': np.random.choice(['Northeast', 'South', 'Midwest', 'West'], 200)
})

print("Dataset Sleep - premieres lignes :")
print(sleep_data.head())
print("Description :")
print(sleep_data.describe())

# Dataset 2 : Mental Health
np.random.seed(7)
mental_health_data = pd.DataFrame({
    'Country': np.random.choice(['USA', 'France', 'Brazil', 'India', 'China'], 200),
    'Year': np.random.randint(2000, 2023, 200),
    'Depression_Rate': np.round(np.random.uniform(2.0, 10.0, 200), 2),
    'Anxiety_Rate': np.round(np.random.uniform(1.5, 8.0, 200), 2),
    'Bipolar_Rate': np.round(np.random.uniform(0.5, 3.0, 200), 2),
    'Population_M': np.random.randint(5, 1500, 200),
    'Region': np.random.choice(['Europe', 'Asia', 'Americas', 'Africa'], 200),
    'Income_Level': np.random.choice(['Low', 'Middle', 'High'], 200)
})

print("Dataset Mental Health - premieres lignes :")
print(mental_health_data.head())
print("Description :")
print(mental_health_data.describe())

# Dataset 3 : Credit Card
np.random.seed(21)
credit_data = pd.DataFrame({
    'Age': np.random.randint(18, 70, 200),
    'Gender': np.random.choice(['Male', 'Female'], 200),
    'Income': np.round(np.random.uniform(15000, 150000, 200), 2),
    'Credit_Score': np.random.randint(300, 850, 200),
    'Debt_Ratio': np.round(np.random.uniform(0.0, 1.0, 200), 2),
    'Employment_Type': np.random.choice(['Employed', 'Self-employed', 'Unemployed'], 200),
    'Years_Employed': np.random.randint(0, 40, 200),
    'Approved': np.random.choice([1, 0], 200, p=[0.6, 0.4])
})

print("Dataset Credit Card - premieres lignes :")
print(credit_data.head())
print("Description :")
print(credit_data.describe())

print("Exercice 2 termine")

# ==================================================
# EXERCICE 3 - Types de donnees sur les 3 datasets
# ==================================================

def classifier_colonnes(df, nom):
    print("Classification : " + nom)
    print("{:<20} {:<15} {}".format("Colonne", "Type Python", "Classification"))
    print("-" * 55)
    for col in df.columns:
        if df[col].dtype == 'object' or df[col].dtype == 'bool':
            classif = "Qualitative"
        else:
            classif = "Quantitative"
        print("{:<20} {:<15} {}".format(col, str(df[col].dtype), classif))
    print("")

classifier_colonnes(sleep_data, "Sleep Dataset")
classifier_colonnes(mental_health_data, "Mental Health Dataset")
classifier_colonnes(credit_data, "Credit Card Dataset")

# Justifications Sleep
print("Justifications Sleep Dataset :")
print("Age          -> Quantitative : valeur numerique mesurant les annees")
print("Gender       -> Qualitative  : categorie sans ordre naturel")
print("Sleep_Hours  -> Quantitative : nombre decimal d heures de sommeil")
print("Work_Hours   -> Quantitative : nombre entier d heures travaillees")
print("Health_Status-> Qualitative  : categorie ordinale Excellent Good Fair Poor")
print("Has_Insomnia -> Qualitative  : variable binaire Oui/Non")
print("Region       -> Qualitative  : categorie geographique sans ordre")

print("Exercice 3 termine")

# ==================================================
# EXERCICE 4 - Dataset Iris
# ==================================================

from sklearn.datasets import load_iris

iris_raw = load_iris()
iris = pd.DataFrame(iris_raw.data, columns=iris_raw.feature_names)
iris['species'] = pd.Categorical.from_codes(iris_raw.target, iris_raw.target_names)

print("Dataset Iris - premieres lignes :")
print(iris.head())
print("Types de donnees :")
print(iris.dtypes)
print("Statistiques :")
print(iris.describe())

print("Classification Iris :")
print("sepal length -> Quantitative : mesure physique en cm")
print("sepal width  -> Quantitative : mesure physique en cm")
print("petal length -> Quantitative : mesure physique en cm")
print("petal width  -> Quantitative : mesure physique en cm")
print("species      -> Qualitative  : categorie d espece sans ordre")

print("Exercice 4 termine")

# ==================================================
# EXERCICE 5 - Observation Sleep Dataset
# ==================================================

print("Colonnes interessantes pour l analyse :")
print("Sleep_Hours  : variable principale, distribution et moyenne")
print("Age          : analyser si le sommeil change avec l age")
print("Health_Status: comparer le sommeil selon l etat de sante")
print("Has_Insomnia : comparer dormeurs sains vs insomniaques")
print("Work_Hours   : correlation entre heures de travail et sommeil")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Exploration Sleep Dataset', fontsize=16)

axes[0, 0].hist(sleep_data['Sleep_Hours'], bins=20, color='steelblue', edgecolor='white')
axes[0, 0].axvline(sleep_data['Sleep_Hours'].mean(), color='red', linestyle='--',
                   label="Moyenne : " + str(round(sleep_data['Sleep_Hours'].mean(), 1)))
axes[0, 0].set_title('Distribution heures de sommeil')
axes[0, 0].legend()

sleep_by_health = sleep_data.groupby('Health_Status')['Sleep_Hours'].mean()
sleep_by_health = sleep_by_health.reindex(['Excellent', 'Good', 'Fair', 'Poor'])
axes[0, 1].bar(sleep_by_health.index, sleep_by_health.values,
               color=['#2ecc71', '#3498db', '#f39c12', '#e74c3c'])
axes[0, 1].set_title('Sommeil moyen par etat de sante')

axes[1, 0].scatter(sleep_data['Work_Hours'], sleep_data['Sleep_Hours'],
                   alpha=0.4, color='purple')
axes[1, 0].set_title('Sommeil vs Heures de travail')
axes[1, 0].set_xlabel('Heures travaillees')
axes[1, 0].set_ylabel('Heures de sommeil')

sleep_data.boxplot(column='Sleep_Hours', by='Has_Insomnia', ax=axes[1, 1])
axes[1, 1].set_title('Sommeil selon insomnie')
plt.suptitle('')

plt.tight_layout()
plt.savefig('sleep_exploration.png', dpi=150, bbox_inches='tight')
plt.show()

print("Exercice 5 termine")

# ==================================================
# EXERCICE 6 - Structure vs Non Structure
# ==================================================

print("Exercice 6 - Donnees structurees vs non structurees :")
print("")
print("1. Rapports financiers dans Excel")
print("   -> STRUCTUREE : donnees en lignes/colonnes avec schema fixe")
print("")
print("2. Photographies sur reseaux sociaux")
print("   -> NON STRUCTUREE : pixels bruts sans schema, necessite Computer Vision")
print("")
print("3. Articles de presse sur un site web")
print("   -> NON STRUCTUREE : texte libre sans format, necessite NLP")
print("")
print("4. Donnees inventaire dans base relationnelle")
print("   -> STRUCTUREE : tables avec schema strict, requetes SQL possibles")
print("")
print("5. Entretiens audio enregistres")
print("   -> NON STRUCTUREE : parole naturelle, necessite Speech-to-Text puis NLP")

print("Exercice 6 termine")

# ==================================================
# EXERCICE 7 - Transformation Non Structure -> Structure
# ==================================================

print("Exercice 7 - Transformation de donnees non structurees :")
print("")
print("1. Articles de blog sur des voyages")
print("   Methode : NLP + Extraction d entites (NER)")
print("   Resultat : DataFrame [Article_ID, Destination, Date, Budget, Sentiment]")
print("")
print("2. Enregistrements audio appels service client")
print("   Methode : Speech-to-Text + Classification de texte")
print("   Resultat : DataFrame [Call_ID, Duree, Categorie, Sentiment, Resolu]")
print("")
print("3. Notes manuscrites de brainstorming")
print("   Methode : OCR (Tesseract) + Clustering par theme")
print("   Resultat : DataFrame [Idee_ID, Theme, Auteur, Priorite]")
print("")
print("4. Tutoriel video cuisine")
print("   Methode : Transcription audio + Extraction d information")
print("   Resultat : DataFrame [Video_ID, Recette, Ingredients, Temps, Difficulte]")

print("Exercice 7 termine")

# ==================================================
# EXERCICE 8 - Import Titanic depuis GitHub
# ==================================================

url_titanic = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url_titanic)

print("Dataset Titanic - premieres lignes :")
print(titanic_df.head())
print("Informations :")
print(titanic_df.info())
print("Statistiques :")
print(titanic_df.describe())

print("Exercice 8 termine")

# ==================================================
# EXERCICE 9 - Export Excel et JSON
# ==================================================

df_export = pd.DataFrame({
    'Nom': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan'],
    'Age': [28, 34, 22, 45, 31],
    'Ville': ['Paris', 'Lyon', 'Marseille', 'Bordeaux', 'Toulouse'],
    'Salaire': [42000, 55000, 35000, 68000, 47000],
    'Departement': ['IT', 'Finance', 'Marketing', 'RH', 'IT']
})

print("DataFrame cree :")
print(df_export)

df_export.to_excel('export_donnees.xlsx', index=False, sheet_name='Employes')
print("Exporte en Excel : export_donnees.xlsx")

df_export.to_json('export_donnees.json', orient='records', indent=4, force_ascii=False)
print("Exporte en JSON : export_donnees.json")

df_check = pd.read_json('export_donnees.json')
print("Verification JSON :")
print(df_check)

print("Exercice 9 termine")

# ==================================================
# EXERCICE 10 - Lecture JSON depuis URL
# ==================================================

url_json = "https://jsonplaceholder.typicode.com/users"
df_json = pd.read_json(url_json)

print("Donnees JSON depuis URL :")
print(df_json[['id', 'name', 'username', 'email', 'phone']].head(5))
print("Types de colonnes :")
print(df_json.dtypes)

print("Exercice 10 termine")
print("TOUS LES EXERCICES SONT TERMINES")