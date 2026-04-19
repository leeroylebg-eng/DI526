"""
visualization/charts.py
-----------------------
Toutes les visualisations du projet avec Matplotlib et Seaborn.

Graphiques :
1. Barres   : Top genres recommandés par cluster
2. Heatmap  : Intensité d'écoute par jour et par genre
3. Pie      : Distribution des genres dans la base
4. Line     : Évolution des écoutes sur 7 jours
5. Scatter  : Similarité cosinus entre utilisateurs
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns

sns.set_theme(style="darkgrid", palette="muted")

ALL_GENRES = ["techno", "house", "electronic", "drum & bass", "jazz", "rap", "pop", "ambient"]
DAYS       = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
COLORS     = ["#e74c3c", "#3498db", "#2ecc71", "#f39c12",
              "#9b59b6", "#1abc9c", "#e67e22", "#34495e"]


def save_and_show(fig, filename: str, output_dir: str = "."):
    """Sauvegarde et affiche un graphique."""
    import os
    path = os.path.join(output_dir, filename)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.show()
    print(f"  Saved → {path}")


# ─────────────────────────────────────────────
# 1. Top genres par cluster (barres groupées)
# ─────────────────────────────────────────────

def plot_genres_by_cluster(df: pd.DataFrame, output_dir: str = "."):
    """
    Bar chart groupé : score moyen de chaque genre par cluster.
    Montre clairement les différences de goûts entre groupes.
    """
    genre_cols = {g: f"score_{g.replace(' & ', '_')}" for g in ALL_GENRES}
    clusters   = sorted(df["cluster_name"].unique())

    # Calcul des moyennes par cluster
    means = df.groupby("cluster_name")[[c for c in genre_cols.values()]].mean()
    means.columns = list(genre_cols.keys())

    fig, ax = plt.subplots(figsize=(14, 6))
    x       = np.arange(len(ALL_GENRES))
    width   = 0.8 / len(clusters)

    for i, cluster in enumerate(clusters):
        if cluster in means.index:
            vals   = means.loc[cluster].values
            offset = (i - len(clusters) / 2) * width + width / 2
            bars   = ax.bar(x + offset, vals, width, label=cluster,
                            alpha=0.85, edgecolor="white")

    ax.set_xticks(x)
    ax.set_xticklabels(ALL_GENRES, rotation=20, ha="right", fontsize=10)
    ax.set_ylabel("Score moyen", fontsize=11)
    ax.set_ylim(0, 1.1)
    ax.set_title("Top Genres Recommandés par Cluster d'Utilisateurs", fontsize=13, fontweight="bold")
    ax.legend(title="Cluster", fontsize=9, title_fontsize=10)

    plt.tight_layout()
    save_and_show(fig, "chart1_genres_by_cluster.png", output_dir)


# ─────────────────────────────────────────────
# 2. Heatmap : intensité d'écoute jour × genre
# ─────────────────────────────────────────────

def plot_listening_heatmap(df: pd.DataFrame, output_dir: str = "."):
    """
    Heatmap Seaborn : croise les jours de la semaine (colonnes hours_*)
    et les genres (colonnes score_*) via une corrélation moyenne.

    Chaque cellule = corrélation entre les heures d'écoute d'un jour
    et le score d'un genre — révèle quand chaque genre est écouté.
    """
    day_cols   = [f"hours_{d.lower()}" for d in DAYS]
    genre_cols = [f"score_{g.replace(' & ', '_')}" for g in ALL_GENRES]

    # Matrice de corrélation jours × genres
    heat_data = np.zeros((len(DAYS), len(ALL_GENRES)))
    for i, day_col in enumerate(day_cols):
        for j, genre_col in enumerate(genre_cols):
            if day_col in df.columns and genre_col in df.columns:
                r = df[day_col].corr(df[genre_col])
                heat_data[i, j] = round(r, 3) if not np.isnan(r) else 0

    heat_df = pd.DataFrame(heat_data, index=DAYS, columns=ALL_GENRES)

    fig, ax = plt.subplots(figsize=(13, 5))
    sns.heatmap(heat_df, annot=True, fmt=".2f", cmap="RdYlGn",
                center=0, vmin=-0.5, vmax=0.5,
                linewidths=0.4, ax=ax, cbar_kws={"label": "Corrélation de Pearson"})
    ax.set_title("Intensité d'Écoute par Jour × Genre (Corrélation)", fontsize=13, fontweight="bold")
    ax.set_xlabel("Genre Musical", fontsize=11)
    ax.set_ylabel("Jour de la Semaine", fontsize=11)
    plt.xticks(rotation=20, ha="right")

    plt.tight_layout()
    save_and_show(fig, "chart2_listening_heatmap.png", output_dir)


# ─────────────────────────────────────────────
# 3. Pie chart : distribution des genres
# ─────────────────────────────────────────────

def plot_genre_distribution(df: pd.DataFrame, output_dir: str = "."):
    """
    Pie chart de la distribution du genre principal (top_genre)
    dans l'ensemble des 50 utilisateurs.
    """
    counts = df["top_genre"].value_counts()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # --- Pie chart ---
    wedge_props = {"edgecolor": "white", "linewidth": 2}
    wedges, texts, autotexts = ax1.pie(
        counts.values,
        labels=counts.index,
        autopct="%1.1f%%",
        colors=COLORS[:len(counts)],
        wedgeprops=wedge_props,
        startangle=140,
    )
    for t in autotexts:
        t.set_fontsize(9)
        t.set_fontweight("bold")
    ax1.set_title("Distribution des Genres Principaux", fontsize=12, fontweight="bold")

    # --- Bar chart complémentaire ---
    genre_score_means = {
        g: df[f"score_{g.replace(' & ', '_')}"].mean()
        for g in ALL_GENRES
        if f"score_{g.replace(' & ', '_')}" in df.columns
    }
    gs = list(genre_score_means.keys())
    vs = list(genre_score_means.values())
    bars = ax2.barh(gs, vs, color=COLORS[:len(gs)], alpha=0.8, edgecolor="white")
    ax2.set_xlabel("Score moyen", fontsize=11)
    ax2.set_title("Score Moyen par Genre (tous utilisateurs)", fontsize=12, fontweight="bold")
    ax2.set_xlim(0, 1)
    for bar, val in zip(bars, vs):
        ax2.text(val + 0.01, bar.get_y() + bar.get_height() / 2,
                 f"{val:.2f}", va="center", fontsize=9, fontweight="bold")

    plt.suptitle("Panorama Musical de la Communauté", fontsize=14, fontweight="bold")
    plt.tight_layout()
    save_and_show(fig, "chart3_genre_distribution.png", output_dir)


# ─────────────────────────────────────────────
# 4. Line plot : évolution des écoutes sur 7 jours
# ─────────────────────────────────────────────

def plot_weekly_listening(df: pd.DataFrame, output_dir: str = "."):
    """
    Line plot : compare l'évolution des heures d'écoute sur 7 jours
    entre les différents clusters. Révèle les patterns week-end/semaine.
    """
    day_cols = [f"hours_{d.lower()}" for d in DAYS]
    clusters = df["cluster_name"].unique()

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(13, 10))

    # --- Graphique 1 : par cluster ---
    for cluster, color in zip(clusters, COLORS):
        sub  = df[df["cluster_name"] == cluster]
        means = sub[day_cols].mean().values
        ax1.plot(DAYS, means, marker="o", linewidth=2.2,
                 markersize=7, label=cluster, color=color, alpha=0.9)
        ax1.fill_between(DAYS, means, alpha=0.08, color=color)

    ax1.set_title("Évolution des Écoutes sur 7 Jours par Cluster", fontsize=12, fontweight="bold")
    ax1.set_ylabel("Heures d'écoute moyennes", fontsize=11)
    ax1.legend(fontsize=9)
    ax1.axvspan(4.5, 6.5, alpha=0.07, color="gold", label="Week-end")

    # --- Graphique 2 : MusicFan vs DJFan ---
    for user_type, color in zip(["MusicFan", "DJFan"], ["#3498db", "#e74c3c"]):
        sub   = df[df["type"] == user_type]
        if len(sub) > 0:
            means = sub[day_cols].mean().values
            ax2.plot(DAYS, means, marker="s", linewidth=2.5,
                     markersize=8, label=user_type, color=color)

    ax2.set_title("Évolution des Écoutes : MusicFan vs DJFan", fontsize=12, fontweight="bold")
    ax2.set_ylabel("Heures d'écoute moyennes", fontsize=11)
    ax2.set_xlabel("Jour de la semaine", fontsize=11)
    ax2.legend(fontsize=10)
    ax2.axvspan(4.5, 6.5, alpha=0.07, color="gold")

    plt.tight_layout()
    save_and_show(fig, "chart4_weekly_listening.png", output_dir)


# ─────────────────────────────────────────────
# 5. Scatter : similarité cosinus entre utilisateurs
# ─────────────────────────────────────────────

def plot_cosine_similarity(users: list, cosine_matrix: np.ndarray,
                           df: pd.DataFrame, output_dir: str = "."):
    """
    Scatter plot : positionne chaque utilisateur dans un espace 2D
    dérivé de sa similarité cosinus moyenne avec tous les autres.
    La couleur représente le cluster, la taille les heures d'écoute.
    """
    n      = len(users)
    # Coordonnées : projection simple via PCA manuelle (2 premières composantes)
    genre_cols = [f"score_{g.replace(' & ', '_')}" for g in ALL_GENRES]
    X = df[genre_cols].values.astype(float)

    # PCA à la main avec NumPy
    X_centered = X - X.mean(axis=0)
    cov        = np.cov(X_centered.T)
    eigenvalues, eigenvectors = np.linalg.eigh(cov)
    idx        = np.argsort(eigenvalues)[::-1]
    eigenvectors = eigenvectors[:, idx]
    X_2d       = X_centered @ eigenvectors[:, :2]   # projection sur 2 axes principaux

    cluster_list = df["cluster"].values if "cluster" in df.columns else np.zeros(n)
    hours        = df["total_hours"].values

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    # --- Scatter PCA (clusters en couleur) ---
    scatter = ax1.scatter(
        X_2d[:, 0], X_2d[:, 1],
        c=cluster_list, cmap="tab10",
        s=hours * 4 + 40, alpha=0.75, edgecolors="white", linewidths=0.5
    )
    plt.colorbar(scatter, ax=ax1, label="Cluster ID")

    # Annoter quelques utilisateurs
    for i in range(min(8, n)):
        ax1.annotate(users[i].name, (X_2d[i, 0], X_2d[i, 1]),
                     fontsize=7, ha="center", va="bottom",
                     xytext=(0, 5), textcoords="offset points")

    ax1.set_title("Projection PCA des Profils Musicaux\n(taille = heures d'écoute)", fontsize=12, fontweight="bold")
    ax1.set_xlabel("Composante Principale 1", fontsize=10)
    ax1.set_ylabel("Composante Principale 2", fontsize=10)

    # --- Heatmap de la matrice cosinus (subset 20×20) ---
    sub_n   = min(20, n)
    sub_mat = cosine_matrix[:sub_n, :sub_n]
    sub_names = [u.name[:6] for u in users[:sub_n]]

    sns.heatmap(sub_mat, annot=False, cmap="YlOrRd",
                xticklabels=sub_names, yticklabels=sub_names,
                ax=ax2, cbar_kws={"label": "Similarité Cosinus"}, vmin=0, vmax=1)
    ax2.set_title(f"Matrice de Similarité Cosinus (top {sub_n} utilisateurs)", fontsize=12, fontweight="bold")
    plt.xticks(rotation=45, ha="right", fontsize=7)
    plt.yticks(fontsize=7)

    plt.tight_layout()
    save_and_show(fig, "chart5_cosine_similarity.png", output_dir)


# ─────────────────────────────────────────────
# Point d'entrée autonome
# ─────────────────────────────────────────────

if __name__ == "__main__":
    import sys, os
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    from data.generate_data import generate_users, users_to_dataframe
    from analysis.stats import compute_similarity_matrix, cluster_users

    users = generate_users(50)
    df    = users_to_dataframe(users)
    df, _, _ = cluster_users(users, df, k=4)
    cos_mat, _ = compute_similarity_matrix(users)

    plot_genres_by_cluster(df)
    plot_listening_heatmap(df)
    plot_genre_distribution(df)
    plot_weekly_listening(df)
    plot_cosine_similarity(users, cos_mat, df)
