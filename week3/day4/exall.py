# ============================================================
# DAY 4 - Data Visualization Exercises
# Installation : pip install matplotlib seaborn pandas
# ============================================================

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

plt.rcParams['figure.dpi'] = 120
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False

# ============================================================
# EXERCISE 1 - Understanding Data Visualization
# ============================================================
print("""
=== EXERCISE 1 : Understanding Data Visualization ===

Pourquoi la visualisation de données est-elle importante ?
----------------------------------------------------------
La visualisation de données est essentielle en analyse de données
car elle permet de :
  - Comprendre rapidement des tendances et des patterns complexes
    qui seraient difficiles à détecter dans un tableau de chiffres.
  - Communiquer des résultats de manière claire et accessible
    à des personnes non techniques.
  - Identifier des valeurs aberrantes (outliers) et des anomalies.
  - Faciliter la prise de décision en rendant les données
    plus intuitives et compréhensibles.

À quoi sert un graphique en ligne (line graph) ?
-------------------------------------------------
Un graphique en ligne est utilisé pour visualiser l'évolution
d'une variable au fil du temps (données temporelles / time-series).
Il permet de :
  - Observer des tendances (hausse, baisse, stabilité).
  - Comparer plusieurs séries de données sur la même période.
  - Identifier des cycles ou des saisonnalités.
  Exemple : évolution de la température sur une semaine,
  cours d'une action en bourse, ventes mensuelles.
""")

# ============================================================
# EXERCISE 2 - Line Plot : Temperature Variation
# ============================================================
print("=== EXERCISE 2 : Line Plot - Température sur une semaine ===")

jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
temperatures = [72, 74, 76, 80, 82, 78, 75]

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(jours, temperatures, marker='o', color='#7F77DD', linewidth=2, markersize=8)
ax.set_xlabel('Day')
ax.set_ylabel('Temperature (°F)')
ax.set_title('Temperature Variation Over a Week')
ax.set_ylim(68, 86)
for i, temp in enumerate(temperatures):
    ax.annotate(f'{temp}°', (jours[i], temp), textcoords='offset points',
                xytext=(0, 10), ha='center', fontsize=10)
plt.tight_layout()
plt.savefig('exercise2_line_plot.png')
plt.show()

# ============================================================
# EXERCISE 3 - Bar Chart : Monthly Sales
# ============================================================
print("=== EXERCISE 3 : Bar Chart - Ventes mensuelles ===")

mois = ['January', 'February', 'March', 'April', 'May']
ventes = [5000, 5500, 6200, 7000, 7500]

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(mois, ventes, color='#1D9E75', edgecolor='white', width=0.6)
ax.set_xlabel('Month')
ax.set_ylabel('Sales Amount ($)')
ax.set_title('Monthly Sales of a Retail Store')
ax.set_ylim(0, 9000)
for bar, val in zip(bars, ventes):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 100,
            f'${val:,}', ha='center', va='bottom', fontsize=10)
plt.tight_layout()
plt.savefig('exercise3_bar_chart.png')
plt.show()

# ============================================================
# EXERCISES 4, 5, 6 - Student Mental Health Dataset
# Télécharger sur Kaggle :
# https://www.kaggle.com/datasets/shariful07/student-mental-health
# ============================================================

# Chargement du dataset
try:
    df = pd.read_csv('Student Mental health.csv')
    print("\nDataset chargé :", df.shape)
    print(df.columns.tolist())
except FileNotFoundError:
    print("\n[INFO] Fichier 'Student Mental health.csv' non trouvé.")
    print("Télécharge-le sur Kaggle et place-le dans ce dossier.")
    print("Les exercices 4, 5, 6 ne s'exécuteront pas.\n")
    df = None

# ============================================================
# EXERCISE 4 - Histogram : Distribution of CGPA
# ============================================================
if df is not None:
    print("=== EXERCISE 4 : Histogram - Distribution du CGPA ===")

    fig, ax = plt.subplots(figsize=(9, 5))
    sns.histplot(data=df, x='What is your CGPA?', color='#7F77DD',
                 ax=ax, shrink=0.8)
    ax.set_title('Distribution of CGPA Among Students')
    ax.set_xlabel('CGPA')
    ax.set_ylabel('Count')
    plt.tight_layout()
    plt.savefig('exercise4_histogram_cgpa.png')
    plt.show()

# ============================================================
# EXERCISE 5 - Bar Plot : Anxiety Levels Across Genders
# ============================================================
if df is not None:
    print("=== EXERCISE 5 : Bar Plot - Anxiety par genre ===")

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(data=df, x='Do you have Anxiety?', hue='Choose your gender',
                  palette=['#7F77DD', '#1D9E75'], ax=ax)
    ax.set_title('Anxiety Levels Across Different Genders')
    ax.set_xlabel('Do you have Anxiety?')
    ax.set_ylabel('Count')
    ax.legend(title='Gender')
    plt.tight_layout()
    plt.savefig('exercise5_anxiety_gender.png')
    plt.show()

# ============================================================
# EXERCISE 6 - Scatter Plot : Age vs Panic Attacks
# ============================================================
if df is not None:
    print("=== EXERCISE 6 : Scatter Plot - Age vs Panic Attacks ===")

    # Conversion Yes/No → 1/0
    df['Panic_numeric'] = df['Do you have Panic attack?'].map({'Yes': 1, 'No': 0})

    fig, ax = plt.subplots(figsize=(9, 5))
    sns.scatterplot(data=df, x='Age', y='Panic_numeric',
                    hue='Do you have Panic attack?',
                    palette={'Yes': '#D85A30', 'No': '#1D9E75'},
                    s=80, alpha=0.7, ax=ax)
    ax.set_title('Relationship Between Age and Panic Attacks')
    ax.set_xlabel('Age')
    ax.set_ylabel('Panic Attack (1 = Yes, 0 = No)')
    ax.set_yticks([0, 1])
    ax.set_yticklabels(['No', 'Yes'])
    ax.legend(title='Panic Attack')
    plt.tight_layout()
    plt.savefig('exercise6_scatter_panic.png')
    plt.show()

print("\nTous les graphiques ont ete sauvegardes en .png dans ton dossier.")
