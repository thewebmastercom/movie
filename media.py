import webbrowser


class Movie():

    '''Creates a class containing movie information.'''

    def __init__(self, movie_title, movie_year, movie_rating, movie_time,
                 movie_director, movie_stars, movie_storyline,
                 poster_image, trailer_youtube, imdb_link):

        '''
        Args:
            movie_title (str): Title of movie.
            movie_year (int): Year movie released.
            movie_rating (int): Rating of movie from 1 to 5.
            movie_time (int): Time of movie in minutes.
            movie_director (str): Director(s) of the movie. Add multiple with
                                  commas.
            movie_stars (str): Star(s) of the movie. Add multiple with commas.
            movie_storyline (str): Summary of the movie. Keep to < 130 chars.
            poster_image (str): The URL of the poster image.
            trailer_youtube (str):YouTube URL to trailer.
            imdb_link (str): URL to Movie IMDB page.
        '''

        self.title = movie_title
        self.year = movie_year
        self.rating = movie_rating
        self.time = movie_time
        self.director = movie_director
        self.stars = movie_stars
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.imdb_link = imdb_link

    def show_trailer(self):

        '''Opens the Youtube trailer URL in a web browser.'''

        webbrowser.open(self.trailer_youtube_url)
