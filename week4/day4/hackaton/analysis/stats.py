"""
analysis/stats.py
-----------------
Analyses statistiques avancées avec NumPy et SciPy.

Fonctions implémentées :
1. scipy.stats.chisquare   → distribution des genres (aléatoire ou significative ?)
2. scipy.spatial.distance  → similarité cosinus + euclidienne entre profils
3. scipy.stats.pearsonr    → corrélations entre métriques d'écoute
4. scipy.cluster.vq.kmeans → clustering des utilisateurs en groupes musicaux
"""

import numpy as np
import pandas as pd
from scipy import stats
from scipy.spatial.distance import cosine, euclidean
from scipy.cluster.vq import kmeans, whiten, vq

ALL_GENRES = ["techno", "house", "electronic", "drum & bass", "jazz", "rap", "pop", "ambient"]


# ─────────────────────────────────────────────
# 1. Chi-Square : distribution des genres
# ─────────────────────────────────────────────

def chi_square_genre_distribution(df: pd.DataFrame) -> dict:
    """
    Teste si la distribution du genre principal (top_genre) est uniforme
    ou si certains genres sont significativement plus populaires.

    H0 : tous les genres sont également représentés (distribution uniforme)
    H1 : certains genres dominent → distribution non aléatoire
    """
    genre_counts = df["top_genre"].value_counts()

    # Fréquences observées (nombre d'utilisateurs par genre)
    observed = genre_counts.values
    n_genres = len(observed)

    # Fréquences attendues : distribution uniforme
    expected = np.full(n_genres, observed.sum() / n_genres)

    chi2, p_value = stats.chisquare(f_obs=observed, f_exp=expected)

    return {
        "test"        : "Chi-Square goodness of fit",
        "chi2_stat"   : round(chi2, 4),
        "p_value"     : round(p_value, 6),
        "significant" : p_value < 0.05,
        "conclusion"  : (
            "La distribution des genres est NON uniforme — certains genres dominent."
            if p_value < 0.05 else
            "Pas de différence significative — genres distribués aléatoirement."
        ),
        "genre_counts": genre_counts.to_dict(),
    }


# ─────────────────────────────────────────────
# 2. Distances cosinus & euclidiennes
# ─────────────────────────────────────────────

def compute_similarity_matrix(users: list) -> tuple[np.ndarray, np.ndarray]:
    """
    Calcule les matrices de similarité cosinus et de distance euclidienne
    pour tous les paires d'utilisateurs.

    Retourne :
        cosine_sim_matrix   : similarité [0, 1] — 1 = identiques
        euclidean_dist_matrix : distance ≥ 0  — 0 = identiques
    """
    n = len(users)
    vectors = np.array([
        [u.favorite_genres.get(g, 0.0) for g in ALL_GENRES]
        for u in users
    ])

    cosine_sim   = np.zeros((n, n))
    euclidean_dist = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if i == j:
                cosine_sim[i, j]    = 1.0
                euclidean_dist[i, j] = 0.0
            else:
                cosine_sim[i, j]    = round(1 - cosine(vectors[i], vectors[j]), 4)
                euclidean_dist[i, j] = round(euclidean(vectors[i], vectors[j]), 4)

    return cosine_sim, euclidean_dist


def most_similar_pairs(users: list, cosine_matrix: np.ndarray, top_n: int = 5) -> list:
    """
    Retourne les top_n paires d'utilisateurs les plus similaires
    selon la similarité cosinus.
    """
    n = len(users)
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            pairs.append({
                "user_1"     : users[i].name,
                "user_2"     : users[j].name,
                "cosine_sim" : cosine_matrix[i, j],
            })

    pairs.sort(key=lambda x: x["cosine_sim"], reverse=True)
    return pairs[:top_n]


# ─────────────────────────────────────────────
# 3. Pearson : corrélations entre métriques
# ─────────────────────────────────────────────

def pearson_correlations(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcule les corrélations de Pearson entre plusieurs paires de métriques :
    - heures d'écoute totales vs n_interests
    - weekend_ratio vs events_attended
    - age vs score_techno (hypothèse : jeunes = plus de techno)
    - total_hours vs score_house
    """
    pairs = [
        ("total_hours",    "n_interests",      "Heures d'écoute ↔ Nombre d'intérêts"),
        ("weekend_ratio",  "events_attended",  "Ratio week-end ↔ Événements assistés"),
        ("age",            "score_techno",     "Âge ↔ Score techno"),
        ("total_hours",    "score_house",      "Heures d'écoute ↔ Score house"),
        ("age",            "total_hours",      "Âge ↔ Heures d'écoute"),
        ("score_techno",   "score_house",      "Score techno ↔ Score house"),
    ]

    results = []
    for col_a, col_b, label in pairs:
        if col_a in df.columns and col_b in df.columns:
            a = df[col_a].values.astype(float)
            b = df[col_b].values.astype(float)
            r, p = stats.pearsonr(a, b)
            results.append({
                "Paire"        : label,
                "Pearson r"    : round(r, 4),
                "p-value"      : round(p, 6),
                "Significant"  : "✓" if p < 0.05 else "✗",
                "Interprétation": _interpret_r(r),
            })

    return pd.DataFrame(results)


def _interpret_r(r: float) -> str:
    """Interprète verbalement le coefficient de Pearson."""
    abs_r = abs(r)
    direction = "positive" if r > 0 else "négative"
    if abs_r > 0.7:
        strength = "forte"
    elif abs_r > 0.4:
        strength = "modérée"
    elif abs_r > 0.2:
        strength = "faible"
    else:
        strength = "négligeable"
    return f"Corrélation {strength} {direction}"


# ─────────────────────────────────────────────
# 4. K-Means : clustering des utilisateurs
# ─────────────────────────────────────────────

def cluster_users(users: list, df: pd.DataFrame, k: int = 4) -> pd.DataFrame:
    """
    Regroupe les utilisateurs en k clusters musicaux avec scipy.cluster.vq.kmeans.

    Étapes :
    1. Construire la matrice de features (scores par genre)
    2. Normaliser (whiten) pour équilibrer les dimensions
    3. Appliquer k-means
    4. Assigner chaque utilisateur à un cluster

    Retourne le DataFrame enrichi avec la colonne 'cluster'.
    """
    genre_cols = [f"score_{g.replace(' & ', '_')}" for g in ALL_GENRES]
    features   = df[genre_cols].values.astype(float)

    # whiten : normalise chaque dimension par son écart-type
    whitened = whiten(features)

    # k-means SciPy : retourne les centroïdes et la distorsion
    centroids, distortion = kmeans(whitened, k, seed=42)

    # Assigner chaque utilisateur au centroïde le plus proche
    labels, _ = vq(whitened, centroids)

    df = df.copy()
    df["cluster"] = labels

    # Nommer les clusters selon le genre dominant dans chaque centroïde
    cluster_labels = _name_clusters(centroids, k)
    df["cluster_name"] = df["cluster"].map(cluster_labels)

    print(f"\nK-Means terminé | Distorsion : {distortion:.4f}")
    print(f"Distribution des clusters :\n{df['cluster_name'].value_counts().to_string()}")

    return df, centroids, cluster_labels


def _name_clusters(centroids: np.ndarray, k: int) -> dict:
    """Attribue un nom à chaque cluster selon son genre dominant."""
    cluster_names_pool = [
        "Underground / Techno",
        "Mainstream / Pop-Rap",
        "Jazz & Ambient",
        "House & Electronic",
        "All-Rounder",
    ]
    names = {}
    for i in range(k):
        # Le nom correspond au genre dominant du centroïde
        dominant_idx = np.argmax(centroids[i])
        pool_idx = dominant_idx % len(cluster_names_pool)
        names[i] = cluster_names_pool[pool_idx]
    return names


# ─────────────────────────────────────────────
# Point d'entrée autonome
# ─────────────────────────────────────────────

if __name__ == "__main__":
    import sys, os
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    from data.generate_data import generate_users, users_to_dataframe

    users = generate_users(50)
    df    = users_to_dataframe(users)

    print("=== 1. Chi-Square ===")
    chi = chi_square_genre_distribution(df)
    print(f"Chi2={chi['chi2_stat']}, p={chi['p_value']}")
    print(chi["conclusion"])

    print("\n=== 2. Similarité cosinus ===")
    cos_mat, euc_mat = compute_similarity_matrix(users[:10])
    pairs = most_similar_pairs(users[:10], cos_mat, top_n=3)
    for p in pairs:
        print(f"  {p['user_1']} ↔ {p['user_2']} : {p['cosine_sim']}")

    print("\n=== 3. Corrélations Pearson ===")
    pearson_df = pearson_correlations(df)
    print(pearson_df[["Paire", "Pearson r", "p-value", "Significant"]].to_string(index=False))

    print("\n=== 4. K-Means Clustering ===")
    df_c, centroids, labels = cluster_users(users, df, k=4)
