import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.impute import SimpleImputer
warnings.filterwarnings('ignore')

# Chargement du dataset Titanic
url_titanic = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url_titanic)

print("Dataset Titanic charge")
print("Dimensions initiales :", df.shape)
print(df.head())

# ==================================================
# EXERCICE 1 - Duplicate Detection And Removal
# ==================================================

print("\n--- EXERCICE 1 : Doublons ---")

# Nombre de lignes avant
rows_before = df.shape[0]
print("Nombre de lignes avant :", rows_before)

# Detecter les doublons
duplicates = df.duplicated()
print("Nombre de doublons trouves :", duplicates.sum())

# Supprimer les doublons
df = df.drop_duplicates()

# Nombre de lignes apres
rows_after = df.shape[0]
print("Nombre de lignes apres :", rows_after)
print("Lignes supprimees :", rows_before - rows_after)

# Verification
print("Doublons restants :", df.duplicated().sum())
print("Exercice 1 termine")

# ==================================================
# EXERCICE 2 - Handling Missing Values
# ==================================================

print("\n--- EXERCICE 2 : Valeurs manquantes ---")

# Identifier les colonnes avec valeurs manquantes
print("Valeurs manquantes par colonne :")
print(df.isnull().sum())
print("")
print("Pourcentage de valeurs manquantes :")
print(round(df.isnull().sum() / len(df) * 100, 2))

# Strategie 1 : Imputation par la mediane pour Age
# On utilise la mediane car Age peut avoir des valeurs extremes
imputer = SimpleImputer(strategy='median')
df['Age'] = imputer.fit_transform(df[['Age']])
print("Age : valeurs manquantes remplies par la mediane :", df['Age'].median())

# Strategie 2 : Remplir par la valeur la plus frequente pour Embarked
# Embarked a seulement 2 valeurs manquantes
embarked_mode = df['Embarked'].mode()[0]
df['Embarked'] = df['Embarked'].fillna(embarked_mode)
print("Embarked : valeurs manquantes remplies par :", embarked_mode)

# Strategie 3 : Supprimer la colonne Cabin
# Cabin a trop de valeurs manquantes (77%) donc inutilisable
df = df.drop(columns=['Cabin'])
print("Cabin : colonne supprimee car trop de valeurs manquantes")

# Verification
print("\nValeurs manquantes apres traitement :")
print(df.isnull().sum())
print("Exercice 2 termine")

# ==================================================
# EXERCICE 3 - Feature Engineering
# ==================================================

print("\n--- EXERCICE 3 : Feature Engineering ---")

# Nouvelle feature : Family Size
# On additionne SibSp (freres/soeurs/conjoint) et Parch (parents/enfants) + 1 (la personne elle-meme)
df['Family_Size'] = df['SibSp'] + df['Parch'] + 1
print("Family_Size creee :")
print(df['Family_Size'].value_counts())

# Nouvelle feature : Is_Alone
# Si la personne voyage seule
df['Is_Alone'] = (df['Family_Size'] == 1).astype(int)
print("\nIs_Alone :")
print(df['Is_Alone'].value_counts())

# Nouvelle feature : Title (extrait du nom)
# Le nom contient toujours un titre comme Mr, Mrs, Miss, Master
df['Title'] = df['Name'].str.extract(r' ([A-Za-z]+)\.', expand=False)
print("\nTitres trouves :")
print(df['Title'].value_counts())

# Simplifier les titres rares
df['Title'] = df['Title'].replace(
    ['Lady', 'Countess', 'Capt', 'Col', 'Don', 'Dr',
     'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare'
)
df['Title'] = df['Title'].replace('Mlle', 'Miss')
df['Title'] = df['Title'].replace('Ms', 'Miss')
df['Title'] = df['Title'].replace('Mme', 'Mrs')

print("\nTitres simplifies :")
print(df['Title'].value_counts())

# Encoder Title avec Label Encoding
le = LabelEncoder()
df['Title_Encoded'] = le.fit_transform(df['Title'])
print("\nTitle encode :")
print(df[['Title', 'Title_Encoded']].drop_duplicates().sort_values('Title_Encoded'))

print("Exercice 3 termine")

# ==================================================
# EXERCICE 4 - Outlier Detection And Handling
# ==================================================

print("\n--- EXERCICE 4 : Valeurs aberrantes ---")

# Visualisation avant traitement
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Distribution avant traitement des outliers', fontsize=14)

axes[0, 0].hist(df['Fare'], bins=50, color='steelblue', edgecolor='white')
axes[0, 0].set_title('Fare - avant')

axes[0, 1].boxplot(df['Fare'].dropna())
axes[0, 1].set_title('Fare - boxplot avant')

axes[1, 0].hist(df['Age'], bins=30, color='orange', edgecolor='white')
axes[1, 0].set_title('Age - avant')

axes[1, 1].boxplot(df['Age'].dropna())
axes[1, 1].set_title('Age - boxplot avant')

plt.tight_layout()
plt.savefig('outliers_avant.png', dpi=150, bbox_inches='tight')
plt.show()

# Methode IQR pour Fare
Q1_fare = df['Fare'].quantile(0.25)
Q3_fare = df['Fare'].quantile(0.75)
IQR_fare = Q3_fare - Q1_fare
lower_fare = Q1_fare - 1.5 * IQR_fare
upper_fare = Q3_fare + 1.5 * IQR_fare

print("Fare - Q1 :", round(Q1_fare, 2))
print("Fare - Q3 :", round(Q3_fare, 2))
print("Fare - IQR :", round(IQR_fare, 2))
print("Fare - Borne basse :", round(lower_fare, 2))
print("Fare - Borne haute :", round(upper_fare, 2))
print("Fare - Outliers detectes :", ((df['Fare'] < lower_fare) | (df['Fare'] > upper_fare)).sum())

# Capping par quantile 0.98 pour Fare
fare_cap = df['Fare'].quantile(0.98)
df['Fare'] = df['Fare'].clip(upper=fare_cap)
print("Fare - Plafonne a :", round(fare_cap, 2))

# Log transformation pour Fare
df['Fare_Log'] = np.log1p(df['Fare'])
print("Fare_Log creee avec log transformation")

# Methode IQR pour Age
Q1_age = df['Age'].quantile(0.25)
Q3_age = df['Age'].quantile(0.75)
IQR_age = Q3_age - Q1_age
lower_age = Q1_age - 1.5 * IQR_age
upper_age = Q3_age + 1.5 * IQR_age

print("\nAge - Outliers detectes :", ((df['Age'] < lower_age) | (df['Age'] > upper_age)).sum())

# Capping Age
age_cap = df['Age'].quantile(0.98)
df['Age'] = df['Age'].clip(upper=age_cap)
print("Age - Plafonne a :", round(age_cap, 2))

# Visualisation apres traitement
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Distribution apres traitement des outliers', fontsize=14)

axes[0, 0].hist(df['Fare'], bins=50, color='steelblue', edgecolor='white')
axes[0, 0].set_title('Fare - apres capping')

axes[0, 1].hist(df['Fare_Log'], bins=50, color='green', edgecolor='white')
axes[0, 1].set_title('Fare_Log - apres log transform')

axes[1, 0].hist(df['Age'], bins=30, color='orange', edgecolor='white')
axes[1, 0].set_title('Age - apres capping')

axes[1, 1].boxplot(df['Age'].dropna())
axes[1, 1].set_title('Age - boxplot apres')

plt.tight_layout()
plt.savefig('outliers_apres.png', dpi=150, bbox_inches='tight')
plt.show()

print("Exercice 4 termine")

# ==================================================
# EXERCICE 5 - Data Standardization And Normalization
# ==================================================

print("\n--- EXERCICE 5 : Standardisation et Normalisation ---")

# StandardScaler pour Age (distribution normale)
scaler_standard = StandardScaler()
df['Age_Scaled'] = scaler_standard.fit_transform(df[['Age']])
print("Age_Scaled avec StandardScaler (moyenne=0, std=1) :")
print("  Moyenne :", round(df['Age_Scaled'].mean(), 4))
print("  Ecart-type :", round(df['Age_Scaled'].std(), 4))

# MinMaxScaler pour Fare_Log (distribution asymetrique)
scaler_minmax = MinMaxScaler()
df['Fare_Normalized'] = scaler_minmax.fit_transform(df[['Fare_Log']])
print("\nFare_Normalized avec MinMaxScaler (min=0, max=1) :")
print("  Min :", round(df['Fare_Normalized'].min(), 4))
print("  Max :", round(df['Fare_Normalized'].max(), 4))

# StandardScaler pour Family_Size
df['Family_Size_Scaled'] = scaler_standard.fit_transform(df[['Family_Size']])
print("\nFamily_Size_Scaled :")
print("  Moyenne :", round(df['Family_Size_Scaled'].mean(), 4))
print("  Ecart-type :", round(df['Family_Size_Scaled'].std(), 4))

print("Exercice 5 termine")

# ==================================================
# EXERCICE 6 - Feature Encoding
# ==================================================

print("\n--- EXERCICE 6 : Encodage des variables categoriques ---")

# One-Hot Encoding pour Sex (variable nominale)
sex_dummies = pd.get_dummies(df['Sex'], prefix='Sex')
df = pd.concat([df, sex_dummies], axis=1)
print("Sex encode en one-hot :")
print(df[['Sex', 'Sex_female', 'Sex_male']].head())

# One-Hot Encoding pour Embarked (variable nominale)
embarked_dummies = pd.get_dummies(df['Embarked'], prefix='Embarked')
df = pd.concat([df, embarked_dummies], axis=1)
print("\nEmbarked encode en one-hot :")
print(df[['Embarked', 'Embarked_C', 'Embarked_Q', 'Embarked_S']].head())

# Supprimer les colonnes originales qui ont ete encodees
df = df.drop(columns=['Sex', 'Embarked', 'Name', 'Ticket'])
print("\nColonnes apres encodage :")
print(df.columns.tolist())

print("\nDimensions finales :", df.shape)
print("Exercice 6 termine")

# ==================================================
# EXERCICE 7 - Data Transformation For Age Feature
# ==================================================

print("\n--- EXERCICE 7 : Transformation de la feature Age ---")

# Creer des groupes d age avec pd.cut()
bins = [0, 12, 18, 60, 100]
labels = ['Child', 'Teen', 'Adult', 'Senior']

df['Age_Group'] = pd.cut(
    df['Age'],
    bins=bins,
    labels=labels,
    right=True
)

print("Groupes d age crees :")
print(df['Age_Group'].value_counts().sort_index())

# Visualisation des groupes d age
plt.figure(figsize=(8, 5))
df['Age_Group'].value_counts().sort_index().plot(
    kind='bar',
    color=['#3498db', '#2ecc71', '#f39c12', '#e74c3c'],
    edgecolor='white'
)
plt.title('Repartition des groupes d age - Titanic')
plt.xlabel('Groupe d age')
plt.ylabel('Nombre de passagers')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('age_groups.png', dpi=150, bbox_inches='tight')
plt.show()

# One-Hot Encoding des groupes d age
age_dummies = pd.get_dummies(df['Age_Group'], prefix='Age_Group')
df = pd.concat([df, age_dummies], axis=1)
df = df.drop(columns=['Age_Group'])

print("\nAge_Group encode en one-hot :")
print(df[['Age_Group_Child', 'Age_Group_Teen',
          'Age_Group_Adult', 'Age_Group_Senior']].head(10))

print("\nDimensions finales du dataset :", df.shape)
print("\nApercu final du dataset :")
print(df.head())

print("\nTOUS LES EXERCICES SONT TERMINES")
print("N oublie pas de push sur GitHub !")