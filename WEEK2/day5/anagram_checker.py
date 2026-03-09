class AnagramChecker:

    def __init__(self, filepath="sowpods.txt"):
        """Charge la liste de mots depuis le fichier texte."""
        self.word_list = set()
        with open(filepath, "r") as f:
            for line in f:
                word = line.strip().lower()
                if word:
                    self.word_list.add(word)

    def is_valid_word(self, word):
        """Vérifie si le mot existe dans la liste de mots."""
        return word.lower() in self.word_list

    def is_anagram(self, word1, word2):
        """Retourne True si word1 et word2 sont des anagrammes l'un de l'autre."""
        return sorted(word1.lower()) == sorted(word2.lower())

    def get_anagrams(self, word):
        """Retourne la liste de tous les anagrammes du mot donné."""
        anagrams = []
        for w in self.word_list:
            if w.lower() != word.lower() and self.is_anagram(w, word):
                anagrams.append(w)
        return anagrams
