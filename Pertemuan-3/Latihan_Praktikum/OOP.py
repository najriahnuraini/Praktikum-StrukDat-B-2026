class Music:
    def __init__(self, title, genre, singer) :
         self.title = title
         self.genre = genre
         self.singer = singer

    def judul_lagu(self) :
         print("about you")

    def genre_lagu(self) :
         print("pop")

    def ubah_judul(self, titleBaru) :
         self.title = titleBaru

m1 = Music("about you", "pop", "the 1975")
m2 = Music("manchild", "pop", "sabrina carpenter")
m3 = Music("mejikuhibiniu", "hiphop", "naykila")

m1.judul_lagu()
m2.genre_lagu()
m3.ubah_judul("cinta satu malam")

print(m1.title, m1.genre, m1.singer)
print(m2.title, m2.genre, m2.singer)
print(m3.title, m3.genre, m3.singer)