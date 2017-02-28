import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Top 100 Movies For Developer Geeks</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link href="https://fonts.googleapis.com/css?family=Francois+One" rel="stylesheet">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>

    <style type="text/css" media="screen">


        header {
            text-align: center;
            background-color:#1c262f;
            padding:80px 0 60px 0;
            font-family: 'Francois One', sans-serif;
        }
        header h1.center-block {
            font-size: 120px;
            color:#37c8b9;
            padding-bottom:30px;
        }
        header .glyphicon {
            font-size: 70px;
            padding:5px;
        }
        body {
        background-color:#1c262f;
        color: white;
        font-family: 'Francois One', sans-serif;
        color:#37c8b9;
        }

        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #37c8b9;
            cursor: pointer;
            color:#1c262f;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''

    <header>
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <h1 class="center-block">Top 100 Movies For Developer Geeks</h1>
                    <span class="glyphicon glyphicon-star" aria-hidden="true"></span><span class="glyphicon glyphicon-star" aria-hidden="true"></span><span class="glyphicon glyphicon-star" aria-hidden="true"></span><span class="glyphicon glyphicon-star" aria-hidden="true"></span><span class="glyphicon glyphicon-star" aria-hidden="true"></span>
                </div>
            </div>
        </div>
    </header>

  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->





    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-6 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
<div class="row">
<div class="col-md-6 col-lg-6 text-center">
    <img src="{poster_image_url}" width="220" height="342">
</div>
<div class="col-md-6 col-lg-6 text-center">
    <h2>{movie_title}</h2>
    <p>{movie_rating}</p>
    <p>({movie_year}), {movie_time} mins</p>
    <p>{movie_storyline}</p>

    <p>{movie_director}</p>
    <p>{movie_stars}</p>
    <p><a href="{movie_imdb_link}">Read more at IMDB</a></p>
</div>
</div>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    film_number = 0
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # create film number to display in tile
        film_number += 1

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title = "<span>" + str(film_number)+ ".</span>" + " " + movie.title,
            poster_image_url = movie.poster_image_url,
            trailer_youtube_id = trailer_youtube_id,
            movie_storyline = movie.storyline,
            movie_year = movie.year,
            movie_rating = movie.rating * '''<span class="glyphicon glyphicon-star" aria-hidden="true"></span>''',
            movie_time = movie.time,
            movie_director = movie.director,
            movie_stars = movie.stars,
            movie_imdb_link = movie.imdb_link
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
