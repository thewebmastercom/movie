import webbrowser

class Movie():

    def __init__(self, movie_title, movie_year, movie_rating, movie_time,
                 movie_director, movie_stars, movie_storyline,
                 poster_image, trailer_youtube, imdb_link):
        self.title = movie_title
        self.year = movie_year
        self.rating = movie_rating
        self.time = movie_time
        self.director = movie_director
        self.stars = movie_stars
        self.storyline =  movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.imdb_link = imdb_link

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
