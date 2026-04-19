"""
models/user_profile.py
----------------------
Définition des classes OOP pour les profils utilisateurs.

Hiérarchie :
    User (base)
    └── MusicFan(User)
        └── DJFan(MusicFan)

Principes OOP appliqués :
- Encapsulation  : attributs privés + getters/setters
- Héritage       : chaque classe étend la précédente
- Polymorphisme  : get_recommendation() redéfinie à chaque niveau
"""

from functools import reduce


# ─────────────────────────────────────────────
# Classe de base : User
# ─────────────────────────────────────────────

class User:
    """Représente un utilisateur générique avec nom et âge."""

    def __init__(self, name: str, age: int):
        self._name = name          # attribut privé
        self._age = age

    # --- Getters / Setters ---
    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int):
        if value < 0 or value > 120:
            raise ValueError(f"Âge invalide : {value}")
        self._age = value

    def get_recommendation(self) -> str:
        """Polymorphisme : version de base, sans contexte musical."""
        return f"Bonjour {self._name}, découvrez notre catalogue général."

    def __repr__(self) -> str:
        return f"User(name={self._name!r}, age={self._age})"


# ─────────────────────────────────────────────
# Classe héritée : MusicFan
# ─────────────────────────────────────────────

class MusicFan(User):
    """
    Fan de musique avec des intérêts, un journal d'activité
    et des préférences de genres pondérées.
    """

    # Playlists disponibles par genre (utilisées dans les recommandations)
    GENRE_PLAYLISTS = {
        "techno"       : ["Charlotte de Witte – KNTXT", "Alignment Festival Set", "Dax J – Fabric"],
        "house"        : ["Peggy Gou – Set 2023", "Fisher – Losing It", "DJ Koze – Knock Knock"],
        "electronic"   : ["Aphex Twin – Selected", "Bicep – Isles Live", "Four Tet – Fabric 59"],
        "drum & bass"  : ["Andy C – Ram Records", "Goldie – Timeless", "Noisia – Impact"],
        "jazz"         : ["Miles Davis – Kind of Blue", "Coltrane – A Love Supreme"],
        "rap"          : ["Kendrick Lamar – DAMN", "J. Cole – 2014 FHD"],
        "pop"          : ["The Weeknd – Blinding Lights", "Dua Lipa – Future Nostalgia"],
        "ambient"      : ["Brian Eno – Ambient 1", "Floating Points – Promises"],
    }

    def __init__(self, name: str, age: int, interests: list,
                 activity_log: list, listening_hours: list,
                 favorite_genres: dict):
        super().__init__(name, age)
        self._interests = interests
        self._activity_log = activity_log
        self._listening_hours = listening_hours   # liste de 7 valeurs (lun→dim)
        self._favorite_genres = favorite_genres   # {"techno": 0.8, ...}

    # --- Getters / Setters ---
    @property
    def interests(self) -> list:
        return self._interests

    @property
    def favorite_genres(self) -> dict:
        return self._favorite_genres

    @favorite_genres.setter
    def favorite_genres(self, genres: dict):
        """Valide que les scores sont entre 0 et 1."""
        if any(v < 0 or v > 1 for v in genres.values()):
            raise ValueError("Les scores de genres doivent être entre 0 et 1.")
        self._favorite_genres = genres

    @property
    def listening_hours(self) -> list:
        return self._listening_hours

    @property
    def total_hours(self) -> float:
        """Total des heures d'écoute sur la semaine."""
        return sum(self._listening_hours)

    @property
    def weekend_ratio(self) -> float:
        """Ratio écoute week-end / total (sam=5, dim=6)."""
        if self.total_hours == 0:
            return 0.0
        weekend = self._listening_hours[5] + self._listening_hours[6]
        return weekend / self.total_hours

    def top_genre(self) -> str:
        """Retourne le genre le plus écouté via max() + lambda."""
        if not self._favorite_genres:
            return "unknown"
        return max(self._favorite_genres, key=lambda g: self._favorite_genres[g])

    def get_recommendation(self) -> str:
        """
        Polymorphisme : recommandation basée sur les genres préférés.
        Utilise map + filter + reduce pour construire la playlist.
        """
        top = self.top_genre()

        # filter : garder les genres avec score > 0.4
        active_genres = list(filter(
            lambda g: self._favorite_genres[g] > 0.4,
            self._favorite_genres
        ))

        # map : récupérer jusqu'à 2 tracks par genre actif
        track_lists = list(map(
            lambda g: self.GENRE_PLAYLISTS.get(g, [])[:2],
            active_genres
        ))

        # reduce : fusionner toutes les listes en une seule
        if track_lists:
            all_tracks = reduce(lambda a, b: a + b, track_lists)
        else:
            all_tracks = self.GENRE_PLAYLISTS.get(top, ["Aucune track trouvée"])

        # Recommandation week-end si ratio élevé
        event_msg = ""
        if self.weekend_ratio > 0.5:
            event_msg = "\n  🎉 Ton activité explose le week-end → Check les événements DJ près de toi !"

        tracks_str = "\n    • " + "\n    • ".join(all_tracks[:5])
        return (
            f"🎵 {self._name}, basé sur ton amour du {top} :\n"
            f"  Playlist du soir :{tracks_str}"
            f"{event_msg}"
        )

    def __repr__(self) -> str:
        return (f"MusicFan(name={self._name!r}, age={self._age}, "
                f"top_genre={self.top_genre()!r})")


# ─────────────────────────────────────────────
# Classe héritée : DJFan
# ─────────────────────────────────────────────

class DJFan(MusicFan):
    """
    Fan hardcore de DJs : suit des sets spécifiques et assiste à des events.
    Hérite de MusicFan et surcharge get_recommendation() avec une logique
    orientée performance live.
    """

    # Base de sets DJ par genre
    DJ_SETS = {
        "techno"      : ["Charlotte de Witte @ Awakenings", "Amelie Lens @ Fabric",
                         "Dax J @ Berghain", "Alignment @ Fabric Live"],
        "house"       : ["Fisher @ Coachella", "Peggy Gou @ Boiler Room",
                         "DJ Koze @ Melt Festival", "Chris Stussy @ ADE"],
        "electronic"  : ["Bicep @ Printworks", "Four Tet @ Glastonbury",
                         "Floating Points @ Barbican"],
        "drum & bass" : ["Andy C @ Fabric", "Goldie @ Wembley", "Noisia @ Warehouse"],
        "ambient"     : ["Brian Eno @ Royal Festival Hall"],
    }

    UPCOMING_EVENTS = [
        "⚡ Festival Awakenings – Amsterdam (juin)",
        "⚡ Boiler Room Paris – (juillet)",
        "⚡ Fabric London – Every Friday",
        "⚡ Dour Festival – Belgique (juillet)",
        "⚡ Printworks London – (août)",
    ]

    def __init__(self, name: str, age: int, interests: list,
                 activity_log: list, listening_hours: list,
                 favorite_genres: dict, favorite_sets: list,
                 events_attended: int):
        super().__init__(name, age, interests, activity_log,
                         listening_hours, favorite_genres)
        self._favorite_sets = favorite_sets
        self._events_attended = events_attended

    @property
    def events_attended(self) -> int:
        return self._events_attended

    @events_attended.setter
    def events_attended(self, value: int):
        if value < 0:
            raise ValueError("Le nombre d'événements ne peut pas être négatif.")
        self._events_attended = value

    @property
    def favorite_sets(self) -> list:
        return self._favorite_sets

    def get_recommendation(self) -> str:
        """
        Polymorphisme : recommandation DJ spécifique.
        Priorise les sets live et les événements à venir.
        """
        top = self.top_genre()
        sets = self.DJ_SETS.get(top, ["Sets à découvrir"])

        # filter : événements pour les fans très actifs (> 3 events)
        events = list(filter(
            lambda e: self._events_attended > 3 or "Boiler Room" in e,
            self.UPCOMING_EVENTS[:3]
        ))

        sets_str = "\n    • " + "\n    • ".join(sets[:3])
        events_str = "\n    → " + "\n    → ".join(events) if events else ""

        return (
            f"🎧 {self._name} [DJ Fan | {self._events_attended} events] :\n"
            f"  Top sets {top} :{sets_str}\n"
            f"  Prochains events :{events_str if events_str else ' Consulte Resident Advisor !'}"
        )

    def __repr__(self) -> str:
        return (f"DJFan(name={self._name!r}, age={self._age}, "
                f"top_genre={self.top_genre()!r}, "
                f"events={self._events_attended})")
