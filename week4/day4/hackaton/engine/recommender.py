"""
engine/recommender.py
---------------------
Moteur de recommandation musicale.

Logique :
- Règles métier (if/elif) basées sur les préférences
- Similarité cosinus (SciPy) pour trouver les "voisins musicaux"
- Utilise lambda, map, filter, reduce pour le traitement fonctionnel
"""

import numpy as np
from functools import reduce
from scipy.spatial.distance import cosine, euclidean


# ─────────────────────────────────────────────
# Constantes : catalogue musical
# ─────────────────────────────────────────────

ALL_GENRES = ["techno", "house", "electronic", "drum & bass", "jazz", "rap", "pop", "ambient"]

RECOMMENDATIONS_DB = {
    "techno": {
        "playlists" : ["Berghain Essentials", "Dark Techno Selection", "Peak Hour Techno"],
        "artists"   : ["Charlotte de Witte", "Alignment", "Dax J", "Amelie Lens"],
        "events"    : ["Awakenings Festival", "Berghain Berlin", "Fabric London"],
    },
    "house": {
        "playlists" : ["Deep House Vibes", "House Underground", "Late Night House"],
        "artists"   : ["Fisher", "Peggy Gou", "DJ Koze", "Chris Stussy"],
        "events"    : ["ADE Amsterdam", "Sonar Barcelona", "DC-10 Ibiza"],
    },
    "electronic": {
        "playlists" : ["Electronic Explorations", "Synth Journey", "Future Electronics"],
        "artists"   : ["Bicep", "Four Tet", "Floating Points", "Jon Hopkins"],
        "events"    : ["Glastonbury Electronic", "Primavera Sound", "Melt Festival"],
    },
    "drum & bass": {
        "playlists" : ["DnB Classics", "Liquid DnB", "Neuro DnB"],
        "artists"   : ["Andy C", "Goldie", "Noisia", "Chase & Status"],
        "events"    : ["Rampage Festival", "Boomtown", "Hospitality"],
    },
    "jazz": {
        "playlists" : ["Jazz Standards", "Modern Jazz", "Jazz Fusion"],
        "artists"   : ["Miles Davis", "John Coltrane", "Kamasi Washington"],
        "events"    : ["Montreux Jazz Festival", "North Sea Jazz", "Jazz à Juan"],
    },
    "rap": {
        "playlists" : ["Hip-Hop Essentials", "French Rap", "New School Rap"],
        "artists"   : ["Kendrick Lamar", "J. Cole", "Tyler the Creator"],
        "events"    : ["Rolling Loud", "Hip-Hop Kemp"],
    },
    "pop": {
        "playlists" : ["Pop Hits 2024", "Indie Pop", "Electropop"],
        "artists"   : ["The Weeknd", "Dua Lipa", "Billie Eilish"],
        "events"    : ["Coachella", "Lollapalooza", "Glastonbury Main Stage"],
    },
    "ambient": {
        "playlists" : ["Ambient Works", "Chill Ambient", "Space Ambient"],
        "artists"   : ["Brian Eno", "Aphex Twin", "Stars of the Lid"],
        "events"    : ["Mutek Festival", "CTM Berlin"],
    },
}


# ─────────────────────────────────────────────
# Moteur de recommandation basé sur les règles
# ─────────────────────────────────────────────

def rule_based_recommendation(user) -> dict:
    """
    Génère des recommandations via des règles métier.
    Retourne un dict avec playlists, artistes et événements suggérés.
    """
    genres = user.favorite_genres

    # Règle 1 : genres actifs (score > 0.4) — via filter + lambda
    active_genres = list(filter(
        lambda g: genres.get(g, 0) > 0.4,
        ALL_GENRES
    ))

    # Règle 2 : top genre
    top = user.top_genre()

    # Règle 3 : recommander des événements si ratio week-end élevé
    suggest_events = user.weekend_ratio > 0.45

    # map : récupérer les playlists de chaque genre actif
    playlist_lists = list(map(
        lambda g: RECOMMENDATIONS_DB[g]["playlists"][:2],
        active_genres
    ))

    # reduce : fusionner toutes les playlists
    if playlist_lists:
        all_playlists = reduce(lambda a, b: a + b, playlist_lists)
    else:
        all_playlists = RECOMMENDATIONS_DB[top]["playlists"]

    # Artistes du top genre
    top_artists = RECOMMENDATIONS_DB[top]["artists"]

    # Événements si pertinent
    events = RECOMMENDATIONS_DB[top]["events"] if suggest_events else []

    return {
        "user"        : user.name,
        "top_genre"   : top,
        "active_genres": active_genres,
        "playlists"   : list(dict.fromkeys(all_playlists))[:4],  # dédupliquer
        "artists"     : top_artists[:3],
        "events"      : events,
        "suggest_events": suggest_events,
    }


# ─────────────────────────────────────────────
# Similarité entre utilisateurs (SciPy)
# ─────────────────────────────────────────────

def user_to_vector(user) -> np.ndarray:
    """
    Convertit le profil d'un utilisateur en vecteur NumPy.
    Chaque dimension = score d'un genre musical.
    Ce vecteur est utilisé pour calculer les distances.
    """
    return np.array([user.favorite_genres.get(g, 0.0) for g in ALL_GENRES])


def cosine_similarity(u1, u2) -> float:
    """
    Similarité cosinus entre deux utilisateurs.
    Cosine distance → similarité = 1 - distance.
    Valeur proche de 1 = profils similaires.
    """
    v1 = user_to_vector(u1)
    v2 = user_to_vector(u2)
    dist = cosine(v1, v2)
    return round(1 - dist, 4)


def euclidean_distance(u1, u2) -> float:
    """
    Distance euclidienne entre deux profils.
    Valeur proche de 0 = profils similaires.
    """
    v1 = user_to_vector(u1)
    v2 = user_to_vector(u2)
    return round(euclidean(v1, v2), 4)


def find_neighbors(target_user, all_users: list, n: int = 5, method: str = "cosine") -> list:
    """
    Trouve les n utilisateurs les plus similaires à target_user.

    Paramètres :
        target_user : objet MusicFan/DJFan de référence
        all_users   : liste de tous les utilisateurs
        n           : nombre de voisins à retourner
        method      : "cosine" (similarité) ou "euclidean" (distance)

    Retourne :
        Liste de tuples (user, score) triés par similarité décroissante.
    """
    others = [u for u in all_users if u.name != target_user.name]

    if method == "cosine":
        # Plus le score est élevé, plus ils sont similaires
        scores = list(map(lambda u: (u, cosine_similarity(target_user, u)), others))
        scores.sort(key=lambda x: x[1], reverse=True)
    else:
        # Plus la distance est faible, plus ils sont similaires
        scores = list(map(lambda u: (u, euclidean_distance(target_user, u)), others))
        scores.sort(key=lambda x: x[1])

    return scores[:n]


def collaborative_recommendation(target_user, all_users: list, n_neighbors: int = 3) -> dict:
    """
    Recommandation collaborative : basée sur les voisins musicaux.
    Agrège les préférences des n voisins les plus proches pour
    recommander des genres que l'utilisateur cible n'écoute pas encore.
    """
    neighbors = find_neighbors(target_user, all_users, n=n_neighbors)
    target_genres = set(g for g, s in target_user.favorite_genres.items() if s > 0.5)

    # Collecter les genres favoris des voisins (score > 0.6) — via map + filter
    neighbor_genres = list(map(
        lambda pair: [g for g, s in pair[0].favorite_genres.items() if s > 0.6],
        neighbors
    ))

    # Aplatir et compter les occurrences
    if neighbor_genres:
        all_neighbor_genres = reduce(lambda a, b: a + b, neighbor_genres)
    else:
        all_neighbor_genres = []

    # Genres populaires chez les voisins mais pas encore chez la cible
    discovery_genres = list(filter(
        lambda g: g not in target_genres,
        dict.fromkeys(all_neighbor_genres)   # préserver l'ordre, dédupliquer
    ))

    neighbor_names = [pair[0].name for pair in neighbors]
    discovery_recs = [RECOMMENDATIONS_DB[g]["playlists"][0] for g in discovery_genres[:3]
                      if g in RECOMMENDATIONS_DB]

    return {
        "user"             : target_user.name,
        "neighbors"        : neighbor_names,
        "discovery_genres" : discovery_genres[:3],
        "discovery_playlists": discovery_recs,
    }


# ─────────────────────────────────────────────
# Point d'entrée autonome
# ─────────────────────────────────────────────

if __name__ == "__main__":
    import sys, os
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    from data.generate_data import generate_users

    users = generate_users(10)
    target = users[0]

    print("=== Recommandation basée sur les règles ===")
    rec = rule_based_recommendation(target)
    print(f"Utilisateur : {rec['user']}")
    print(f"Genre principal : {rec['top_genre']}")
    print(f"Playlists : {rec['playlists']}")
    print(f"Artistes  : {rec['artists']}")

    print("\n=== Recommandation collaborative ===")
    collab = collaborative_recommendation(target, users)
    print(f"Voisins : {collab['neighbors']}")
    print(f"Genres à découvrir : {collab['discovery_genres']}")
    print(f"Playlists découverte : {collab['discovery_playlists']}")
