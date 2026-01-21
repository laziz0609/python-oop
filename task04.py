class Movie:
    def __init__(self, title: str, genre: str, duration: str, rating: float):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating
        

m1 = Movie("qasoskorlar", "fantazy", "02:23", 9)
m2 = Movie("qasoskorlar 2", "fantazy", "02:29", 10)
m3 = Movie("trol", "fantazy", "02:33", 7.5)


movies = [m1, m2, m3]

for movie in movies:
    print(f"{movie.title}, janri - {movie.genre}, davomiyligi - {movie.duration}, ball - {movie.rating}")
