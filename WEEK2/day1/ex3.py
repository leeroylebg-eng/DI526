# Exercise 3 - Song

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics  # store lyrics as attribute

    def sing_me_a_song(self):
        for line in self.lyrics:  # print each line
            print(line)

# Create a song and call sing_me_a_song()
stairway = Song([
    "There's a lady who's sure",
    "all that glitters is gold",
    "and she's buying a stairway to heaven"
])

stairway.sing_me_a_song()