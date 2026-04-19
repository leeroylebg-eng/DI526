"""
data/generate_data.py
---------------------
Génération de 50 profils utilisateurs synthétiques avec NumPy et Pandas.
Les données sont réalistes : distributions des genres, heures d'écoute,
âges et activités corrélés entre eux.
"""

import numpy as np
import pandas as pd
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from models.user_profile import MusicFan, DJFan

# Seed pour reproductibilité
np.random.seed(42)

# ─────────────────────────────────────────────
# Constantes
# ─────────────────────────────────────────────

FIRST_NAMES = [
    "Alex", "Jordan", "Sam", "Morgan", "Taylor", "Casey", "Riley", "Drew",
    "Avery", "Quinn", "Blake", "Skyler", "Reese", "Finley", "Sage",
    "Luca", "Mia", "Noah", "Emma", "Ethan", "Sofia", "Leo", "Zoe",
    "Max", "Lily", "Oscar", "Chloe", "Hugo", "Inès", "Théo",
    "Camille", "Nathan", "Léa", "Antoine", "Manon", "Romain", "Clara",
    "Baptiste", "Juliette", "Mathis", "Anaïs", "Enzo", "Louise",
    "Louis", "Chloé", "Tom", "Sarah", "Paul", "Nina", "Victor"
]

ALL_GENRES = ["techno", "house", "electronic", "drum & bass", "jazz", "rap", "pop", "ambient"]

# Profils archétypes : chaque archétype a des genres dominants
ARCHETYPES = {
    "underground": {"techno": 0.85, "house": 0.6, "electronic": 0.5,
                    "drum & bass": 0.3, "jazz": 0.1, "rap": 0.05, "pop": 0.0, "ambient": 0.2},
    "mainstream" : {"techno": 0.1, "house": 0.4, "electronic": 0.3,
                    "drum & bass": 0.05, "jazz": 0.1, "rap": 0.7, "pop": 0.85, "ambient": 0.05},
    "jazz_lover" : {"techno": 0.1, "house": 0.2, "electronic": 0.15,
                    "drum & bass": 0.0, "jazz": 0.9, "rap": 0.3, "pop": 0.2, "ambient": 0.5},
    "dj_fan"     : {"techno": 0.75, "house": 0.8, "electronic": 0.65,
                    "drum & bass": 0.5, "jazz": 0.05, "rap": 0.1, "pop": 0.05, "ambient": 0.15},
}

ACTIVITY_TEMPLATES = {
    "underground": [
        "listened to techno set", "attended underground rave",
        "shared Charlotte de Witte mix", "bought festival ticket",
        "liked drum & bass track", "followed DJ on Instagram"
    ],
    "mainstream": [
        "liked pop playlist", "streamed rap album",
        "shared Spotify playlist", "bought concert ticket",
        "followed artist on TikTok", "rated song 5 stars"
    ],
    "jazz_lover": [
        "attended jazz concert", "bought vinyl record",
        "listened to Miles Davis set", "shared jazz playlist",
        "joined jazz club", "rated jazz album"
    ],
    "dj_fan": [
        "listened to techno set", "liked house playlist",
        "attended DJ event", "bought festival ticket",
        "shared drum & bass track", "watched Boiler Room set",
        "followed DJ on Soundcloud", "rated set 5 stars"
    ],
}

DJ_SETS_POOL = [
    "Charlotte de Witte – KNTXT 2023",
    "Fisher – Coachella 2023",
    "Peggy Gou – Boiler Room Berlin",
    "Amelie Lens – Awakenings 2022",
    "DJ Koze – Melt Festival",
    "Four Tet – Glastonbury 2023",
    "Bicep – Printworks London",
    "Andy C – Fabric 50",
]


# ─────────────────────────────────────────────
# Fonctions de génération
# ─────────────────────────────────────────────

def _generate_listening_hours(archetype: str) -> list:
    """
    Génère 7 valeurs d'heures d'écoute (lun→dim).
    Les fans underground/dj_fan écoutent plus le week-end.
    """
    base = np.random.randint(0, 4, size=5).tolist()   # lun–ven : 0–3h
    if archetype in ("underground", "dj_fan"):
        weekend = np.random.randint(3, 8, size=2).tolist()  # week-end : 3–7h
    else:
        weekend = np.random.randint(1, 5, size=2).tolist()
    return base + weekend


def _generate_genres(archetype: str) -> dict:
    """
    Génère des scores de genres en perturbant le profil archétype
    avec du bruit gaussien pour éviter des profils identiques.
    """
    base = ARCHETYPES[archetype].copy()
    noisy = {}
    for genre, score in base.items():
        noise = np.random.normal(0, 0.08)            # bruit ±8%
        noisy[genre] = float(np.clip(score + noise, 0.0, 1.0))
    return noisy


def _generate_activity_log(archetype: str, n: int = 5) -> list:
    """Sélectionne n activités aléatoires du template de l'archétype."""
    pool = ACTIVITY_TEMPLATES[archetype]
    indices = np.random.choice(len(pool), size=min(n, len(pool)), replace=False)
    return [pool[i] for i in indices]


def generate_users(n: int = 50) -> list:
    """
    Génère n objets MusicFan / DJFan synthétiques.
    ~30% des utilisateurs sont des DJFan (archétype dj_fan ou underground).
    """
    archetype_keys = list(ARCHETYPES.keys())
    # Pondération : dj_fan et underground surreprésentés (thème DJ)
    weights = [0.30, 0.25, 0.15, 0.30]

    users = []
    for i in range(n):
        name = FIRST_NAMES[i % len(FIRST_NAMES)]
        age  = int(np.random.normal(26, 5))
        age  = int(np.clip(age, 16, 55))

        archetype = np.random.choice(archetype_keys, p=weights)
        genres    = _generate_genres(archetype)
        interests = [g for g, s in genres.items() if s > 0.5]
        hours     = _generate_listening_hours(archetype)
        activity  = _generate_activity_log(archetype)

        if archetype == "dj_fan":
            n_sets = np.random.randint(2, 6)
            fav_sets = list(np.random.choice(DJ_SETS_POOL, size=n_sets, replace=False))
            events   = int(np.random.randint(2, 20))
            user = DJFan(name, age, interests, activity, hours, genres, fav_sets, events)
        else:
            user = MusicFan(name, age, interests, activity, hours, genres)

        users.append(user)

    return users


def users_to_dataframe(users: list) -> pd.DataFrame:
    """
    Convertit la liste d'objets en DataFrame Pandas structuré.
    Chaque ligne = 1 utilisateur, chaque genre = 1 colonne de score.
    """
    rows = []
    for u in users:
        row = {
            "name"          : u.name,
            "age"           : u.age,
            "type"          : type(u).__name__,
            "total_hours"   : u.total_hours,
            "weekend_ratio" : round(u.weekend_ratio, 3),
            "top_genre"     : u.top_genre(),
            "n_interests"   : len(u.interests),
        }
        # Ajouter les scores par genre
        for genre in ALL_GENRES:
            row[f"score_{genre.replace(' & ', '_')}"] = round(
                u.favorite_genres.get(genre, 0.0), 3
            )
        # Heures par jour
        days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
        for day, h in zip(days, u.listening_hours):
            row[f"hours_{day}"] = h
        # Infos spécifiques DJFan
        if isinstance(u, DJFan):
            row["events_attended"] = u.events_attended
            row["n_fav_sets"]      = len(u.favorite_sets)
        else:
            row["events_attended"] = 0
            row["n_fav_sets"]      = 0

        rows.append(row)

    return pd.DataFrame(rows)


# ─────────────────────────────────────────────
# Point d'entrée autonome
# ─────────────────────────────────────────────

if __name__ == "__main__":
    users = generate_users(50)
    df    = users_to_dataframe(users)
    print(f"Généré {len(users)} utilisateurs\n")
    print(df[["name", "age", "type", "top_genre", "total_hours"]].to_string(index=False))
    print(f"\nTypes : {df['type'].value_counts().to_dict()}")
