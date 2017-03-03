import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta property="og:title" content="Top 30 Movies For Programmers">
    <meta property="og:url" content="https://bestof.thewebmaster.com/top_30_movies_for_programmers.html">
    <meta property="og:type" content="website">
    <meta property="og:description" content="Take a look at our top 30 movies for programmers, along with basic film information and trailers.">
    <meta property="og:image" content="https://bestof.thewebmaster.com/assets/top-100-movies-for-programmers.jpg">
    <meta name="twitter:card" content="summary_large_image"/>
    <meta name="twitter:description" content="Take a look at our top 30 movies for programmers, along with basic film information and trailers."/>
    <meta name="twitter:title" content="Top 30 Movies For Programmers"/>
    <meta name="twitter:site" content="@thewebmastercom"/>
    <meta name="twitter:image" content="https://bestof.thewebmaster.com/assets/top-100-movies-for-programmers.jpg"/>
    <meta name="twitter:creator" content="@thewebmastercom"/>
    <title>Top 30 Movies For Programmers</title>
    <meta name="description" content="Take a look at our top 30 movies for programmers, along with basic film information and trailers.">
    <meta name="robots" content="INDEX, FOLLOW, ARCHIVE">
    <meta name="google-site-verification" content="4hP9BbkZgnQSEf2hWN7kvjjnjc2AU5ktn3LoROVbWZs" />
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="
    https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css
    ">
    <link rel="stylesheet" href="
    https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css
    ">
    <link href="
    https://fonts.googleapis.com/css?family=Francois+One" rel="stylesheet">
    <link href="
    https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js">
    </script>
    <script src="
    https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js">
    </script>
    <script>
      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
      })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

      ga('create', 'UA-92963729-1', 'auto');
      ga('send', 'pageview');

    </script>
    <script type="application/ld+json">

    {
      "@context": "http://schema.org",
      "@type": "WebPage",
      "description": "Top 30 Movies For Programmers",

    }

    </script>
    <style type="text/css">

        header {
            text-align: center;
            background-color:#1c262f;
            padding:20px 0 20px 0;
            font-family: 'Francois One', sans-serif;
        }

        header h1.center-block {
            font-size: 40px;
            color:#37c8b9;
            padding-bottom:10px;
            font-family: 'Francois One', sans-serif;
        }

        header .glyphicon {
            font-size: 30px;
            padding:5px;
        }

        body {
        background-color:#1c262f;
        font-size:14px;
        font-family: 'Open Sans', sans-serif;
        color:#37c8b9;
        }

        body .small-text {
            font-size:12px;
        }

        body .large-text {
            font-size:18px;
        }

        .movie-tile h2{
            margin-top:0px;
            font-family: 'Francois One', sans-serif;
        }

        .movie-tile h2.small_h2 {
        font-size: 25px;
        }

        .director {
        padding-top:5px;
        }

        .left_column {
        padding-bottom: 25px;
        }

        a:hover, a:focus {
            color: #1c262f;
        }

        a {
            color: #37c8b9;
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
            padding-bottom: 30px;
            padding-top: 30px;
            margin-bottom: 20px;
        }

        .movie-tile:hover {
            background-color: #37c8b9;
            cursor: pointer;
            color:#1c262f;
        }

        .movie-tile:hover a{
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

        @media only screen and (min-width : 480px) {

            header h1.center-block {
                font-size: 60px;
                padding-bottom:15px;
            }

            header .glyphicon {
                font-size: 40px;
            }

        header {
                padding:40px 0 40px 0;
            }

        }

        @media only screen and (min-width : 768px) {

            header h1.center-block {
                font-size: 80px;
                padding-bottom:20px;
            }

             header .glyphicon {
                font-size: 50px;
             }

            header {
                padding:40px 0 40px 0;
            }

            .left_column {
                padding-bottom: 0px;
            }

        }

        @media only screen and (min-width : 992px) {

            header h1.center-block {
                font-size: 100px;
                padding-bottom:25px;
            }

            header .glyphicon {
                font-size: 60px;
            }

            header {
                padding:50px 0 50px 0;
            }

        }

        @media only screen and (min-width : 1200px) {

            header h1.center-block {
                font-size: 120px;
                padding-bottom:30px;
            }

            header .glyphicon {
                font-size: 70px;
            }

            header {
                padding:60px 0 60px 0;
            }

        }

</style>


    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal',
        function (event) {
            // Remove the src so the player itself gets removed, as this
            // is the only reliable way to ensure the video
            //  stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.open', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'https://www.youtube.com/embed/' +
            trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>",
            {
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
                <h1 class="center-block">Top 30 Movies For Programmers</h1>
                <span class="glyphicon glyphicon-star" aria-hidden="true">
                </span>
                <span class="glyphicon glyphicon-star" aria-hidden="true">
                </span>
                <span class="glyphicon glyphicon-star" aria-hidden="true">
                </span>
                <span class="glyphicon glyphicon-star" aria-hidden="true">
                </span>
                <span class="glyphicon glyphicon-star" aria-hidden="true">
                </span>
            </div>
        </div>
    </div>
</header>

  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal"
          aria-hidden="true">
            <img src="
            https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24
            "/>
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

<div class="col-sm-12 col-md-6 col-lg-6 movie-tile text-center">
    <div class="row">
        <div class="col-sm-6 col-md-6 col-lg-6 text-center open left_column"
        data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal"
        data-target="#trailer">
            <img src="{poster_image_url}" width="220" height="342">
        </div>

        <div class="col-sm-6 col-md-6 col-lg-6 text-center">
            <div class="row open"
            data-trailer-youtube-id="{trailer_youtube_id}"
            data-toggle="modal" data-target="#trailer">
                <div class="col-md-12 col-lg-12 text-center">
                    {movie_title}
                    <p class="small-text">({movie_year}), {movie_time} mins</p>
                    <p class="large-text">{movie_rating}</p>
                    <p>{movie_storyline}</p>
                    <div class="director">
                        <p class="small-text">Director: {movie_director}</p>
                        <p class="small-text">Stars: {movie_stars}</p>
                    </div>
                </div>
            </div>
            <div class="row" >
                <div class="col-md-12 col-lg-12 text-center">
                    <a href="{movie_imdb_link}"
                    class="btn-lg btn-block">Read more at IMDB</a>
                </div>
            </div>
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

        '''Create film number to display in tile'''
        film_number += 1

        '''This is a fix for long file names. Where length of movie title is \
        greater than 27 we insert a class which we can then style to make \
        font smaller'''
        size = len(movie.title)
        if size > 27:
            title_class = "small_h2"
        else:
            title_class = "normal_h2"
        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title='''<h2 class="''' + title_class + '''"><span>''' +
            str(film_number) + ".</span>" + " " + movie.title + "</h2>",
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_storyline=movie.storyline,
            movie_year=movie.year,
            movie_rating=movie.rating * '''<span class="glyphicon'''
            ''' glyphicon-star" aria-hidden="true"></span>''',
            movie_time=movie.time,
            movie_director=movie.director,
            movie_stars=movie.stars,
            movie_imdb_link=movie.imdb_link
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('../top_30_movies_for_programmers.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
