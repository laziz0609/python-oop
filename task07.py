class Movie:
    def __init__(self, title: str, genre: str, duration: str, rating: float):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating
        
    def show_summary(self):
        print(f"{self.title} — {self.genre} janridagi film. Reyting: {self.rating}/10.")
        

m1 = Movie("qasoskorlar", "fantazy", "02:23", 9)
m2 = Movie("qasoskorlar 2", "fantazy", "02:29", 10)
m3 = Movie("trol", "fantazy", "02:33", 7.5)
