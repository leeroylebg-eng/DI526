"""
main.py
-------
Point d'entrée du Générateur de Contenu Musical Personnalisé.

Lance toutes les étapes dans l'ordre :
1. Génération des données
2. Recommandations (règles + collaboratif)
3. Analyses statistiques (Chi2, cosinus, Pearson, K-Means)
4. Visualisations (5 graphiques)
"""

import os
import sys
import warnings
warnings.filterwarnings("ignore")

# Assure que les imports relatifs fonctionnent depuis n'importe où
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from data.generate_data        import generate_users, users_to_dataframe
from engine.recommender        import (rule_based_recommendation,
                                       collaborative_recommendation,
                                       find_neighbors)
from analysis.stats            import (chi_square_genre_distribution,
                                       compute_similarity_matrix,
                                       most_similar_pairs,
                                       pearson_correlations,
                                       cluster_users)
from visualization.charts      import (plot_genres_by_cluster,
                                       plot_listening_heatmap,
                                       plot_genre_distribution,
                                       plot_weekly_listening,
                                       plot_cosine_similarity)

OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

SEPARATOR = "═" * 60


def print_section(title: str):
    print(f"\n{SEPARATOR}")
    print(f"  {title}")
    print(SEPARATOR)


# ─────────────────────────────────────────────
# ÉTAPE 1 : Génération des données
# ─────────────────────────────────────────────

def step1_generate(n: int = 50):
    print_section("ÉTAPE 1 — Génération des données synthétiques")
    users = generate_users(n)
    df    = users_to_dataframe(users)

    print(f"  ✓ {len(users)} utilisateurs générés")
    print(f"  Types : {df['type'].value_counts().to_dict()}")
    print(f"  Âge moyen : {df['age'].mean():.1f} ans")
    print(f"  Heures d'écoute moyennes/semaine : {df['total_hours'].mean():.1f}h")
    print(f"\n  Aperçu des 5 premiers profils :")
    print(df[["name", "age", "type", "top_genre", "total_hours"]].head().to_string(index=False))

    return users, df


# ─────────────────────────────────────────────
# ÉTAPE 2 : Recommandations
# ─────────────────────────────────────────────

def step2_recommendations(users: list):
    print_section("ÉTAPE 2 — Moteur de Recommandation")

    # 2a. Polymorphisme : get_recommendation() selon le type
    print("\n  [A] Recommandations polymorphes (get_recommendation) :")
    for user in users[:3]:
        print(f"\n  {user.get_recommendation()}")

    # 2b. Règles métier
    print("\n\n  [B] Recommandations basées sur les règles métier :")
    for user in users[:2]:
        rec = rule_based_recommendation(user)
        print(f"\n  👤 {rec['user']} | Genre principal : {rec['top_genre']}")
        print(f"     Playlists : {', '.join(rec['playlists'][:2])}")
        print(f"     Artistes  : {', '.join(rec['artists'])}")
        if rec["events"]:
            print(f"     Événements: {', '.join(rec['events'])}")

    # 2c. Recommandation collaborative (voisins musicaux)
    print("\n\n  [C] Recommandation collaborative (voisins musicaux) :")
    collab = collaborative_recommendation(users[0], users, n_neighbors=3)
    print(f"\n  👤 {collab['user']}")
    print(f"     Voisins musicaux  : {', '.join(collab['neighbors'])}")
    print(f"     Genres à découvrir: {', '.join(collab['discovery_genres'])}")
    if collab["discovery_playlists"]:
        print(f"     Playlists découverte : {', '.join(collab['discovery_playlists'])}")


# ─────────────────────────────────────────────
# ÉTAPE 3 : Analyses statistiques
# ─────────────────────────────────────────────

def step3_statistics(users: list, df):
    print_section("ÉTAPE 3 — Analyses Statistiques (NumPy + SciPy)")

    # 3a. Chi-Square
    print("\n  [1] Chi-Square — Distribution des genres :")
    chi = chi_square_genre_distribution(df)
    print(f"     Chi2 = {chi['chi2_stat']}  |  p = {chi['p_value']}")
    print(f"     → {chi['conclusion']}")
    print(f"     Distribution observée : {chi['genre_counts']}")

    # 3b. Similarité cosinus + euclidienne
    print("\n  [2] Distances cosinus & euclidiennes :")
    cos_mat, euc_mat = compute_similarity_matrix(users)
    top_pairs = most_similar_pairs(users, cos_mat, top_n=5)
    print(f"     Top 5 paires les plus similaires (cosinus) :")
    for pair in top_pairs:
        print(f"       {pair['user_1']:<12} ↔ {pair['user_2']:<12} : {pair['cosine_sim']:.4f}")

    # 3c. Pearson
    print("\n  [3] Corrélations de Pearson :")
    pearson_df = pearson_correlations(df)
    print(pearson_df[["Paire", "Pearson r", "Significant", "Interprétation"]].to_string(index=False))

    # 3d. K-Means
    print("\n  [4] Clustering K-Means (k=4) :")
    df_clustered, centroids, cluster_labels = cluster_users(users, df, k=4)
    print(f"\n     Labels des clusters : {cluster_labels}")

    return df_clustered, cos_mat


# ─────────────────────────────────────────────
# ÉTAPE 4 : Visualisations
# ─────────────────────────────────────────────

def step4_visualizations(users: list, df, cos_mat):
    print_section("ÉTAPE 4 — Visualisations (Matplotlib + Seaborn)")
    print(f"  Output directory : {OUTPUT_DIR}\n")

    print("  → Chart 1 : Top genres par cluster...")
    plot_genres_by_cluster(df, OUTPUT_DIR)

    print("  → Chart 2 : Heatmap écoutes jour × genre...")
    plot_listening_heatmap(df, OUTPUT_DIR)

    print("  → Chart 3 : Distribution des genres (pie + bar)...")
    plot_genre_distribution(df, OUTPUT_DIR)

    print("  → Chart 4 : Évolution hebdomadaire des écoutes...")
    plot_weekly_listening(df, OUTPUT_DIR)

    print("  → Chart 5 : Similarité cosinus (PCA + heatmap)...")
    plot_cosine_similarity(users, cos_mat, df, OUTPUT_DIR)

    print(f"\n  ✓ 5 graphiques sauvegardés dans {OUTPUT_DIR}/")


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("\n🎵  GÉNÉRATEUR DE CONTENU MUSICAL PERSONNALISÉ  🎵")
    print(f"    Hackathon — GenAI & Machine Learning Bootcamp 2026")

    users, df          = step1_generate(n=50)
    step2_recommendations(users)
    df_c, cos_mat      = step3_statistics(users, df)
    step4_visualizations(users, df_c, cos_mat)

    print(f"\n{'═'*60}")
    print("  ✅ Projet terminé avec succès !")
    print(f"  📁 Graphiques disponibles dans : {OUTPUT_DIR}")
    print(f"{'═'*60}\n")
