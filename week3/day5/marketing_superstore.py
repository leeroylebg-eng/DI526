# ============================================================
# Mini-Projet : Analyse de données pour une stratégie marketing
# US Superstore Dataset
#
# Installation : pip install pandas matplotlib numpy
# Placer "Sample - Superstore.csv" dans le même dossier
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import warnings
warnings.filterwarnings('ignore')

plt.rcParams['figure.dpi'] = 120
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False

# ============================================================
# ÉTAPE 1 — Chargement et prétraitement
# ============================================================
df = pd.read_csv('Sample - Superstore.csv', encoding='latin-1')
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date']  = pd.to_datetime(df['Ship Date'])

print("=== Dimensions :", df.shape)
print("=== Valeurs manquantes :\n", df.isnull().sum())
print(df.head())

# ============================================================
# ÉTAPE 2 — Tâche 1 : États avec le plus de ventes
# ============================================================
ventes_etat = df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(15)

fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(ventes_etat.index[::-1], ventes_etat.values[::-1], color='#7F77DD')
ax.set_xlabel('Ventes totales ($)')
ax.set_title('Top 15 États par Ventes')
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))
plt.tight_layout()
plt.savefig('tache1_ventes_etats.png')
plt.show()

print("\n=== Top 5 états par ventes ===")
print(ventes_etat.head())

# ============================================================
# ÉTAPE 3 — Tâche 2 : New York vs Californie
# ============================================================
comp_etat = df[df['State'].isin(['New York', 'California'])].groupby('State')[['Sales', 'Profit']].sum()

fig, ax = plt.subplots(figsize=(7, 5))
x, w = np.arange(2), 0.35
ax.bar(x - w/2, comp_etat['Sales'],  w, label='Ventes', color='#7F77DD')
ax.bar(x + w/2, comp_etat['Profit'], w, label='Profit', color='#1D9E75')
ax.set_xticks(x)
ax.set_xticklabels(comp_etat.index)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))
ax.set_title('New York vs Californie — Ventes & Profit')
ax.legend()
plt.tight_layout()
plt.savefig('tache2_ny_vs_cali.png')
plt.show()

print("\n=== Comparaison New York / Californie ===")
print(comp_etat)

# ============================================================
# ÉTAPE 4 — Tâche 3 : Meilleur client à New York
# ============================================================
clients_ny = df[df['State'] == 'New York'].groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(10)

fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(clients_ny.index[::-1], clients_ny.values[::-1], color='#7F77DD')
ax.set_xlabel('Ventes totales ($)')
ax.set_title('Top 10 Clients à New York')
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))
plt.tight_layout()
plt.savefig('tache3_clients_ny.png')
plt.show()

print(f"\n=== Meilleur client à New York : {clients_ny.index[0]} — ${clients_ny.values[0]:,.2f} ===")

# ============================================================
# ÉTAPE 5 — Tâche 4 : Rentabilité par état
# ============================================================
profit_etat = df.groupby('State')['Profit'].sum().sort_values(ascending=False)
couleurs = ['#1D9E75' if p >= 0 else '#D85A30' for p in profit_etat.values]

fig, ax = plt.subplots(figsize=(14, 7))
ax.bar(profit_etat.index, profit_etat.values, color=couleurs)
ax.axhline(0, color='gray', linewidth=0.8, linestyle='--')
ax.set_ylabel('Profit total ($)')
ax.set_title('Profit par État  (vert = bénéfice  |  orange = perte)')
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))
plt.xticks(rotation=90, fontsize=8)
plt.tight_layout()
plt.savefig('tache4_profit_etats.png')
plt.show()

print("\n=== États en perte ===")
print(profit_etat[profit_etat < 0])

# ============================================================
# ÉTAPE 6 — Tâche 5 : Pareto — Clients & Profit
# ============================================================
profit_clients = df.groupby('Customer Name')['Profit'].sum().sort_values(ascending=False)
cumulatif      = profit_clients.cumsum() / profit_clients.sum() * 100
n_clients      = len(profit_clients)
seuil_20       = int(n_clients * 0.20)
pct_seuil      = cumulatif.iloc[seuil_20 - 1]

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(range(1, n_clients + 1), cumulatif.values, color='#534AB7', linewidth=2)
ax.axvline(seuil_20, color='#D85A30', linestyle='--', label=f'Top 20% ({seuil_20} clients)')
ax.axhline(80,       color='#1D9E75', linestyle='--', label='Seuil 80% du profit')
ax.scatter([seuil_20], [pct_seuil], color='#D85A30', zorder=5, s=80)
ax.set_xlabel('Clients classés par profit décroissant')
ax.set_ylabel('Profit cumulé (%)')
ax.set_title('Analyse de Pareto : Clients vs Profit')
ax.legend()
plt.tight_layout()
plt.savefig('tache5_pareto_profit.png')
plt.show()

print(f"\n=== Pareto Profit : top 20% ({seuil_20} clients) = {pct_seuil:.1f}% du profit ===")
print(f"Principe de Pareto : {'VERIFIE' if pct_seuil >= 80 else 'NON verifie'}")

# ============================================================
# ÉTAPE 7 — Tâche 6 : Top 20 villes par ventes & profit
# ============================================================
ventes_ville = df.groupby('City')['Sales'].sum().nlargest(20)
profit_top20 = df.groupby('City')['Profit'].sum().loc[ventes_ville.index]

fig, axes = plt.subplots(1, 2, figsize=(16, 8))
axes[0].barh(ventes_ville.index[::-1], ventes_ville.values[::-1], color='#7F77DD')
axes[0].set_title('Top 20 Villes par Ventes')
axes[0].xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))

coul2 = ['#1D9E75' if p >= 0 else '#D85A30' for p in profit_top20.values[::-1]]
axes[1].barh(profit_top20.index[::-1], profit_top20.values[::-1], color=coul2)
axes[1].set_title('Profit des Top 20 Villes  (vert = benefice  |  orange = perte)')
axes[1].axvline(0, color='gray', linewidth=0.8)
axes[1].xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))
plt.tight_layout()
plt.savefig('tache6_villes.png')
plt.show()

tableau = pd.DataFrame({'Ventes': ventes_ville, 'Profit': profit_top20})
tableau['Marge (%)'] = (tableau['Profit'] / tableau['Ventes'] * 100).round(1)
print("\n=== Top 20 villes — Ventes, Profit, Marge ===")
print(tableau.sort_values('Marge (%)', ascending=False).to_string())

# ============================================================
# ÉTAPE 8 — Tâche 7 : Top 20 clients par ventes
# ============================================================
top_clients = df.groupby('Customer Name')['Sales'].sum().nlargest(20).sort_values()

fig, ax = plt.subplots(figsize=(9, 8))
ax.barh(top_clients.index, top_clients.values, color='#7F77DD')
ax.set_xlabel('Ventes totales ($)')
ax.set_title('Top 20 Clients par Ventes')
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))
plt.tight_layout()
plt.savefig('tache7_top_clients.png')
plt.show()

print("\n=== Top 20 clients par ventes ===")
print(top_clients[::-1].to_string())

# ============================================================
# ÉTAPE 9 — Tâche 8 : Courbe cumulative des ventes (Pareto)
# ============================================================
ventes_clients = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False)
cum_ventes     = ventes_clients.cumsum() / ventes_clients.sum() * 100
n_c            = len(ventes_clients)
seuil20        = int(n_c * 0.20)
pct_ventes20   = cum_ventes.iloc[seuil20 - 1]

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(range(1, n_c + 1), cum_ventes.values, color='#534AB7', linewidth=2)
ax.axvline(seuil20, color='#D85A30', linestyle='--', label=f'Top 20% ({seuil20} clients)')
ax.axhline(80,      color='#1D9E75', linestyle='--', label='Seuil 80% des ventes')
ax.scatter([seuil20], [pct_ventes20], color='#D85A30', zorder=5, s=80)
ax.set_xlabel('Clients classés par ventes decroissantes')
ax.set_ylabel('Ventes cumulees (%)')
ax.set_title('Courbe cumulative des ventes par clients')
ax.legend()
plt.tight_layout()
plt.savefig('tache8_pareto_ventes.png')
plt.show()

print(f"\n=== Pareto Ventes : top 20% ({seuil20} clients) = {pct_ventes20:.1f}% des ventes ===")
print(f"Principe de Pareto : {'VERIFIE' if pct_ventes20 >= 80 else 'NON verifie'}")

# ============================================================
# ÉTAPE 10 — Tâche 9 : Recommandations de stratégie marketing
# ============================================================
top3_etats  = df.groupby('State')['Sales'].sum().nlargest(3).index.tolist()
etats_perte = profit_etat[profit_etat < 0].index.tolist()
top5_villes = df.groupby('City')['Sales'].sum().nlargest(5).index.tolist()

print("""
========================================================
  TACHE 9 : Recommandations de Strategie Marketing
========================================================""")

print(f"""
ETATS A PRIORISER :
  - Top 3 etats par ventes : {', '.join(top3_etats)}
  - Etats en perte a surveiller : {', '.join(etats_perte[:5])}
  -> Revoir les remises dans ces etats deficitaires.

VILLES A PRIORISER :
  - Top 5 villes par ventes : {', '.join(top5_villes)}
  -> Croiser ventes ET marges avant d'investir.

STRATEGIE CLIENTS :
  - {seuil_20} clients (top 20%) generent {pct_seuil:.1f}% du profit.
  - {seuil20} clients (top 20%) representent {pct_ventes20:.1f}% des ventes.
  -> Creer un programme de fidelite VIP pour ces clients.
  -> Reduire les remises pour les clients peu rentables.

INSIGHT CLE :
  Ventes elevees != profit eleve.
  Concentrer le marketing sur les segments rentables.
========================================================
""")
