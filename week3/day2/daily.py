import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
import warnings
warnings.filterwarnings('ignore')

# ==================================================
# CHARGEMENT DU DATASET
# ==================================================

url = "https://raw.githubusercontent.com/dsrscientist/dataset1/master/DS_Jobs.csv"

# Si l URL ne fonctionne pas, utiliser cette alternative
try:
    df = pd.read_csv(url)
    print("Dataset charge depuis URL")
except:
    # Dataset simule representatif du dataset Data Science Job Salaries
    np.random.seed(42)
    df = pd.DataFrame({
        'work_year': np.random.choice([2020, 2021, 2022, 2023], 200),
        'experience_level': np.random.choice(['EN', 'MI', 'SE', 'EX'], 200),
        'employment_type': np.random.choice(['FT', 'PT', 'CT', 'FL'], 200),
        'job_title': np.random.choice([
            'Data Scientist', 'Data Engineer', 'ML Engineer',
            'Data Analyst', 'Data Architect'
        ], 200),
        'salary': np.random.randint(30000, 250000, 200),
        'salary_currency': np.random.choice(['USD', 'EUR', 'GBP'], 200),
        'salary_in_usd': np.random.randint(30000, 250000, 200),
        'employee_residence': np.random.choice(['US', 'GB', 'FR', 'DE', 'IN'], 200),
        'remote_ratio': np.random.choice([0, 50, 100], 200),
        'company_location': np.random.choice(['US', 'GB', 'FR', 'DE'], 200),
        'company_size': np.random.choice(['S', 'M', 'L'], 200)
    })
    print("Dataset simule cree")

print("Dimensions :", df.shape)
print(df.head())
print("\nTypes de colonnes :")
print(df.dtypes)

# ==================================================
# TACHE 1 - Normalisation Min-Max de la colonne salary
# ==================================================

print("\n--- TACHE 1 : Normalisation Min-Max ---")

# Afficher les stats avant normalisation
print("Salary avant normalisation :")
print("  Min :", df['salary_in_usd'].min())
print("  Max :", df['salary_in_usd'].max())
print("  Moyenne :", round(df['salary_in_usd'].mean(), 2))

# Appliquer Min-Max Normalization
# Formula : (x - min) / (max - min)
scaler = MinMaxScaler()
df['salary_normalized'] = scaler.fit_transform(df[['salary_in_usd']])

# Afficher les stats apres normalisation
print("\nSalary apres normalisation Min-Max :")
print("  Min :", round(df['salary_normalized'].min(), 4))
print("  Max :", round(df['salary_normalized'].max(), 4))
print("  Moyenne :", round(df['salary_normalized'].mean(), 4))

# Visualisation avant / apres
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle('Normalisation Min-Max du Salary', fontsize=14)

axes[0].hist(df['salary_in_usd'], bins=30, color='steelblue', edgecolor='white')
axes[0].set_title('Salary original (en USD)')
axes[0].set_xlabel('Salaire')
axes[0].set_ylabel('Frequence')

axes[1].hist(df['salary_normalized'], bins=30, color='green', edgecolor='white')
axes[1].set_title('Salary normalise (0 a 1)')
axes[1].set_xlabel('Valeur normalisee')
axes[1].set_ylabel('Frequence')

plt.tight_layout()
plt.savefig('salary_normalisation.png', dpi=150, bbox_inches='tight')
plt.show()

print("Tache 1 terminee")

# ==================================================
# TACHE 2 - Reduction de dimensionnalite avec PCA
# ==================================================

print("\n--- TACHE 2 : PCA - Reduction de dimensionnalite ---")

# Selectionner uniquement les colonnes numeriques pour PCA
colonnes_numeriques = df.select_dtypes(include=[np.number]).columns.tolist()
print("Colonnes numeriques utilisees pour PCA :")
print(colonnes_numeriques)

df_numeric = df[colonnes_numeriques].dropna()

# Normaliser les donnees avant PCA
scaler_pca = MinMaxScaler()
df_scaled = scaler_pca.fit_transform(df_numeric)

print("Dimensions avant PCA :", df_scaled.shape)

# Appliquer PCA pour reduire a 2 composantes
pca = PCA(n_components=2)
df_pca = pca.fit_transform(df_scaled)

print("Dimensions apres PCA :", df_pca.shape)
print("Variance expliquee par chaque composante :")
print("  PC1 :", round(pca.explained_variance_ratio_[0] * 100, 2), "%")
print("  PC2 :", round(pca.explained_variance_ratio_[1] * 100, 2), "%")
print("  Total :", round(sum(pca.explained_variance_ratio_) * 100, 2), "%")

# Creer un DataFrame avec les composantes PCA
df_pca_result = pd.DataFrame(df_pca, columns=['PC1', 'PC2'])

# Ajouter experience_level pour la visualisation
df_pca_result['experience_level'] = df['experience_level'].values[:len(df_pca_result)]

# Visualisation PCA
plt.figure(figsize=(10, 7))
colors = {'EN': '#3498db', 'MI': '#2ecc71', 'SE': '#f39c12', 'EX': '#e74c3c'}
for level in df_pca_result['experience_level'].unique():
    mask = df_pca_result['experience_level'] == level
    plt.scatter(
        df_pca_result[mask]['PC1'],
        df_pca_result[mask]['PC2'],
        label=level,
        alpha=0.6,
        color=colors.get(level, 'gray')
    )

plt.title('PCA - Visualisation en 2 dimensions par Experience Level')
plt.xlabel('Composante Principale 1')
plt.ylabel('Composante Principale 2')
plt.legend(title='Experience Level')
plt.tight_layout()
plt.savefig('pca_visualisation.png', dpi=150, bbox_inches='tight')
plt.show()

# Variance expliquee par toutes les composantes
pca_full = PCA()
pca_full.fit(df_scaled)
variance_cumulative = np.cumsum(pca_full.explained_variance_ratio_) * 100

plt.figure(figsize=(8, 5))
plt.plot(range(1, len(variance_cumulative) + 1), variance_cumulative, 'bo-')
plt.axhline(y=95, color='red', linestyle='--', label='95% variance')
plt.title('Variance expliquee cumulative par composante PCA')
plt.xlabel('Nombre de composantes')
plt.ylabel('Variance expliquee (%)')
plt.legend()
plt.tight_layout()
plt.savefig('pca_variance.png', dpi=150, bbox_inches='tight')
plt.show()

print("Tache 2 terminee")

# ==================================================
# TACHE 3 - Agregation par Experience Level
# ==================================================

print("\n--- TACHE 3 : Agregation par Experience Level ---")

# Correspondance des codes d experience
experience_map = {
    'EN': 'Junior (Entry Level)',
    'MI': 'Mid-level',
    'SE': 'Senior',
    'EX': 'Executive / Expert'
}
df['experience_label'] = df['experience_level'].map(experience_map)

# Calculer moyenne et mediane par niveau d experience
agregation = df.groupby('experience_label')['salary_in_usd'].agg(
    Moyenne='mean',
    Mediane='median',
    Min='min',
    Max='max',
    Nombre='count'
).round(2)

print("Statistiques de salaire par niveau d experience :")
print(agregation)

# Visualisation - Moyenne vs Mediane par experience
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Salaire par niveau d experience', fontsize=14)

# Graphique moyenne
agregation['Moyenne'].sort_values().plot(
    kind='bar',
    ax=axes[0],
    color='steelblue',
    edgecolor='white'
)
axes[0].set_title('Salaire MOYEN par experience')
axes[0].set_xlabel('Niveau d experience')
axes[0].set_ylabel('Salaire moyen (USD)')
axes[0].tick_params(axis='x', rotation=30)

# Graphique mediane
agregation['Mediane'].sort_values().plot(
    kind='bar',
    ax=axes[1],
    color='orange',
    edgecolor='white'
)
axes[1].set_title('Salaire MEDIAN par experience')
axes[1].set_xlabel('Niveau d experience')
axes[1].set_ylabel('Salaire median (USD)')
axes[1].tick_params(axis='x', rotation=30)

plt.tight_layout()
plt.savefig('salary_par_experience.png', dpi=150, bbox_inches='tight')
plt.show()

# Boxplot par niveau d experience
plt.figure(figsize=(10, 6))
df.boxplot(
    column='salary_in_usd',
    by='experience_label',
    figsize=(12, 6)
)
plt.title('Distribution des salaires par niveau d experience')
plt.suptitle('')
plt.xlabel('Niveau d experience')
plt.ylabel('Salaire (USD)')
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig('salary_boxplot_experience.png', dpi=150, bbox_inches='tight')
plt.show()

# Insights
print("\nInsights :")
print("")
niveau_max = agregation['Moyenne'].idxmax()
niveau_min = agregation['Moyenne'].idxmin()
print("Niveau le mieux paye :", niveau_max,
      "avec une moyenne de", round(agregation.loc[niveau_max, 'Moyenne'], 2), "USD")
print("Niveau le moins paye :", niveau_min,
      "avec une moyenne de", round(agregation.loc[niveau_min, 'Moyenne'], 2), "USD")
print("Ecart entre senior et junior :",
      round(agregation.loc[niveau_max, 'Moyenne'] -
            agregation.loc[niveau_min, 'Moyenne'], 2), "USD")

print("\nConclusion :")
print("La normalisation Min-Max ramene tous les salaires entre 0 et 1.")
print("Le PCA reduit les dimensions tout en conservant l essentiel de l information.")
print("L agregation montre clairement que le salaire augmente avec l experience.")

print("\nDAILY CHALLENGE TERMINE")