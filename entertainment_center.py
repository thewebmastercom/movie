import fresh_tomatoes
import media

the_matrix = media.Movie("The Matrix",
                         "1999",
                         4,
                         136,
                         "The Wachowski Brothers",
                         "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving",
                         "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                         "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                         "https://www.youtube.com/watch?v=a94b1yZOBes",
                         "http://www.imdb.com/title/tt0133093/"
                         )


movies = [the_matrix]
fresh_tomatoes.open_movies_page(movies)
