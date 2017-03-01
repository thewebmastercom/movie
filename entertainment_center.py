import fresh_tomatoes
import media

'''
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

the_matrix = media.Movie(
    "The Matrix",
    "1999",
    4,
    136,
    "The Wachowski Brothers",
    "Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving",
    "A computer hacker learns from mysterious rebels about the true nature of \
    his reality and his role in the war against its controllers.",
    "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
    "https://www.youtube.com/watch?v=a94b1yZOBes",
    "http://www.imdb.com/title/tt0133093/")

ghost_in_the_shell = media.Movie(
    "Ghost in the Shell",
    "1995",
    4,
    83,
    "Mamoru Oshii",
    "Atsuko Tanaka, Iemasa Kayumi, Akio Otsuka, Koichi Yamadera",
    "A cyborg policewoman and her partner hunt a mysterious and powerful \
    hacker called the Puppet Master.",
    "https://upload.wikimedia.org/wikipedia/en/1/11/"
    "Ghost_in_the_Shell_%282017_film%29.png",
    "https://www.youtube.com/watch?v=SvBVDibOrgs",
    "http://www.imdb.com/title/tt0113568/")

the_girl_with_the_dragon_tatoo = media.Movie(
    "The Girl with the Dragon Tattoo",
    "2009",
    4,
    152,
    "Niels Arden Oplev",
    "Michael Nyqvist, Noomi Rapace, Ewa Froling, Lena Endre",
    "A journalist is aided in his search for a woman who has been missing -- \
    or dead -- for forty years by a young female hacker.",
    "https://upload.wikimedia.org/wikipedia/en/8/80/"
    "The_Girl_with_the_Dragon_Tattoo_Poster.jpg",
    "https://www.youtube.com/watch?v=RL8LI-h2WFc",
    "http://www.imdb.com/title/tt1132620/"
    )

minority_report = media.Movie(
    "Minority Report",
    "2002",
    4,
    145,
    "Steven Spielberg",
    "Tom Cruise, Colin Farrell, Samantha Morton, Max von Sydow",
    "An officer from a special unit who arrests murderers before they commit \
    their crimes, is himself accused of a future murder.",
    "https://upload.wikimedia.org/wikipedia/en/4/44/"
    "Minority_Report_Poster.jpg",
    "https://www.youtube.com/watch?v=jdl6eAIx2K4",
    "http://www.imdb.com/title/tt0181689/"
    )

snowden = media.Movie(
    "Snowden",
    "2016",
    5,
    134,
    "Oliver Stone",
    "Joseph Gordon-Levitt, Shailene Woodley, Melissa Leo",
    "The NSA's illegal surveillance techniques are leaked to the public by one \
    of the agency's employees, Edward Snowden.",
    "https://upload.wikimedia.org/wikipedia/en/c/ca/Snowden_film_poster.jpg",
    "https://www.youtube.com/watch?v=QlSAiI3xMh4",
    "http://www.imdb.com/title/tt3774114/"
    )

the_internship = media.Movie(
    "The Internship",
    "2013",
    3,
    119,
    "Shawn Levy",
    "Vince Vaughn, Owen Wilson, Rose Byrne",
    "Two salesmen whose careers have been torpedoed by the digital age find \
    their way into a coveted internship at Google.",
    "https://upload.wikimedia.org/wikipedia/en/e/ed/The-internship-poster.jpg",
    "https://www.youtube.com/watch?v=cdnoqCViqUo",
    "http://www.imdb.com/title/tt2234155/"
    )

twenty_three = media.Movie(
    "23",
    "1998",
    3,
    136,
    "Hans-Christian Schmid",
    "August Diehl, Fabian Busch, Dieter Landuris, Jan-Gregor Kremp",
    "The movie's plot is based on the true story of a group of young computer \
    hackers from Hannover, Germany.",
    "https://upload.wikimedia.org/wikipedia/en/4/4e/23MovieFrenchDVDCover.jpg",
    "https://www.youtube.com/watch?v=be_uVIM8tyM",
    "http://www.imdb.com/title/tt0126765/"
    )

sneakers = media.Movie(
    "Sneakers",
    "1992",
    3,
    126,
    "Phil Alden Robinson",
    "Robert Redford, Dan Aykroyd, Sidney Poitier, Jo Marr",
    "A security pro's past comes back to haunt him, when he is tasked with \
    retrieving a particularly important item.",
    "https://upload.wikimedia.org/wikipedia/en/a/aa/Sneakersmovie.jpg",
    "https://www.youtube.com/watch?v=rbJpx_6fYgE",
    "http://www.imdb.com/title/tt0105435/"
    )

wargames = media.Movie(
    "WarGames",
    "1983",
    4,
    114,
    "John Badham",
    "Matthew Broderick, Ally Sheedy, John Wood, Dabney Coleman",
    "A young man finds a back door into a military central computer in which \
    reality is confused with game-playing, possibly starting World War III. ",
    "https://upload.wikimedia.org/wikipedia/en/2/29/Wargames.jpg",
    "https://www.youtube.com/watch?v=tAcEzhQ7oqA",
    "http://www.imdb.com/title/tt0086567/"
    )

the_thirteenth_floor = media.Movie(
    "The Thirteenth Floor",
    "1999",
    3,
    100,
    "Josef Rusnak",
    "Craig Bierko, Gretchen Mol, Armin Mueller-Stahl, Vincent D'Onofrio",
    "Computer scientist Hannon Fuller has discovered something important. \
    He's about to tell his colleague...",
    "https://upload.wikimedia.org/wikipedia/en/0/02/"
    "The_Thirteenth_Floor_poster.jpg",
    "https://www.youtube.com/watch?v=dtYdZkPmFoU",
    "http://www.imdb.com/title/tt0139809/"
    )

existenz = media.Movie(
    "eXistenZ",
    "1999",
    3,
    97,
    "David Cronenberg",
    "Jude Law, Jennifer Jason Leigh, Ian Holm, Willem Dafoe",
    "A game designer on the run from assassins plays her latest virtual \
    reality creation to determine if the game has been damaged.",
    "https://upload.wikimedia.org/wikipedia/en/7/76/EXISTENZ.jpg",
    "https://www.youtube.com/watch?v=HAdbdUt_h9M",
    "http://www.imdb.com/title/tt0120907/"
    )

tron = media.Movie(
    "TRON",
    "1982",
    4,
    96,
    "Steven Lisberger",
    "Jeff Bridges, Bruce Boxleitner, David Warner, Cindy Morgan",
    "computer hacker is abducted into the digital world and forced to \
    participate in gladiatorial games with the help of a security program",
    "https://upload.wikimedia.org/wikipedia/en/1/17/Tron_poster.jpg",
    "https://www.youtube.com/watch?v=3efV2wqEjEY",
    "http://www.imdb.com/title/tt0084827/"
    )

underground = media.Movie(
    "Underground: The Julian Assange Story",
    "2012",
    3,
    94,
    "Robert Connolly",
    "Rachel Griffiths, Anthony LaPaglia, Alex Williams, Laura Wheelwright",
    "A look at the early career of Wikileaks founder, Julian Assange.",
    "https://www.thewebmaster.com/media/uploads/files/underground.jpg",
    "https://www.youtube.com/watch?v=1ujDD2LpSRg",
    "http://www.imdb.com/title/tt2357453/"
    )

wierd_science = media.Movie(
    "Weird Science",
    "1985",
    5,
    94,
    "John Hughes",
    "Anthony Michael Hall, Ilan Mitchell-Smith, Kelly LeBrock, Bill Paxton",
    "Two high school nerds attempt to create the perfect woman, but she turns \
    out to be more than that.",
    "https://upload.wikimedia.org/wikipedia/en/d/d6/"
    "Movie_poster_for_Weird_Science_%281985%29.jpg",
    "https://www.youtube.com/watch?v=25q3hxlgvw4",
    "http://www.imdb.com/title/tt0090305/"
    )

eagle_eye = media.Movie(
    "Eagle Eye",
    "2008",
    3,
    118,
    "D.J. Caruso",
    "Shia LaBeouf, Michelle Monaghan, Rosario Dawson, Michael Chiklis",
    "Jerry and Rachel are two strangers thrown together by a mysterious \
    phone call from a woman they have never met. ",
    "https://upload.wikimedia.org/wikipedia/en/1/15/Eagle_eye_poster.jpg",
    "https://www.youtube.com/watch?v=_wkqo_Rd3_Q",
    "http://www.imdb.com/title/tt1059786/"
    )

swordfish = media.Movie(
    "Swordfish",
    "2001",
    3,
    99,
    "Dominic Sena",
    "John Travolta, Hugh Jackman, Halle Berry, Don Cheadle",
    "Gabriel brings in convicted hacker Stanley Jobson to help him to unlock \
    money to help fight terrorism.",
    "https://upload.wikimedia.org/wikipedia/en/e/e8/Swordfish_movie.jpg",
    "https://www.youtube.com/watch?v=mfLizCqjz18",
    "http://www.imdb.com/title/tt0244244/"
    )

takedown = media.Movie(
    "Takedown",
    "2000",
    2,
    96,
    "Joe Chappelle",
    "Skeet Ulrich, Russell Wong, Angela Featherstone, Donal Logue",
    "This film is based on the story of the capture of computer hacker \
    Kevin Mitnick.",
    "https://upload.wikimedia.org/wikipedia/en/e/e5/Takedown_2000.jpg",
    "https://www.youtube.com/watch?v=NbgDMYy9mzM",
    "http://www.imdb.com/title/tt0159784/"
    )

hackers = media.Movie(
    "Hackers",
    "1995",
    3,
    107,
    "Iain Softley",
    "TJonny Lee Miller, Angelina Jolie, Jesse Bradford, Matthew Lillard",
    "Dade Murphy was a hacker even as a kid in Seattle. He got arrested for \
    the computer virus that he planted",
    "https://upload.wikimedia.org/wikipedia/en/6/67/Hackersposter.jpg",
    "https://www.youtube.com/watch?v=Rn2cf_wJ4f4",
    "http://www.imdb.com/title/tt0113243/"
    )

the_fifth_estate = media.Movie(
    "The Fifth Estate",
    "2013",
    4,
    128,
    "Bill Condon",
    "Benedict Cumberbatch, Daniel Bruhl, Carice van Houten",
    "The story behind Wikileaks, one of the 21st century's most \
    fiercely debated organizations.",
    "https://upload.wikimedia.org/wikipedia/en/0/0a/"
    "The_Fifth_Estate_poster.jpg",
    "https://www.youtube.com/watch?v=ZT1wb8_tcYU",
    "http://www.imdb.com/title/tt1837703/"
    )

onepoint0 = media.Movie(
    "One Point O",
    "2002",
    3,
    92,
    "Jeff Renfroe, Marteinn Thorsson",
    "Richard Rees, Jeremy Sisto, Udo Kier, Deborah Kara Unger",
    "After receiving mysterious empty packages inside his apartment, a young \
    computer-programmer investigates.",
    "https://upload.wikimedia.org/wikipedia/en/1/11/"
    "Paranoia_1point0_poster.jpg",
    "https://www.youtube.com/watch?v=rw3V_VnRoaA",
    "http://www.imdb.com/title/tt0317042/"
    )

antitrust = media.Movie(
    "Antitrust",
    "2001",
    3,
    109,
    "Peter Howitt",
    "Ryan Phillippe, Tim Robbins, Rachael Leigh Cook, Claire Forlani",
    "A programmer discovers his boss has a secret and ruthless means of \
    dispatching anti-trust problems.",
    "https://upload.wikimedia.org/wikipedia/en/2/2a/Antitrust_poster.jpg",
    "https://www.youtube.com/watch?v=EMHF5LjY9EI",
    "http://www.imdb.com/title/tt0218817/"
    )

the_computer_wore_tennis_shoes = media.Movie(
    "The Computer Wore Tennis Shoes",
    "1969",
    5,
    91,
    "Robert Butler",
    "Kurt Russell, Cesar Romero, Joe Flynn, William Schallert",
    "College students persuade the town's big businessman to \
    donate a computer to their college.",
    "https://upload.wikimedia.org/wikipedia/en/7/73/"
    "Computer_wore_tennis_shoes_ver1.jpg",
    "https://www.youtube.com/watch?v=DtCTKMQSCOo",
    "http://www.imdb.com/title/tt0065566/"
    )

the_net = media.Movie(
    "The Net",
    "1995",
    2,
    114,
    "Irwin Winkler",
    "Sandra Bullock, Jeremy Northam, Dennis Miller, Diane Baker",
    "A computer programmer stumbles upon a conspiracy, putting her life \
    in great danger.",
    "https://upload.wikimedia.org/wikipedia/en/0/0d/Netposter1995.jpg",
    "https://www.youtube.com/watch?v=46qKHq7REI4",
    "http://www.imdb.com/title/tt0113957/"
    )

gamer = media.Movie(
    "Gamer",
    "2009",
    3,
    95,
    "Neveldine, Taylor",
    "Gerard Butler, Michael C. Hall, Ludacris, Amber Valletta",
    "In a future mind-controlling game, death row convicts battle in a \
    Doom-type environment to win freedom.",
    "https://upload.wikimedia.org/wikipedia/en/f/fa/Gamermovie.jpg",
    "https://www.youtube.com/watch?v=P2g94xQmtHw",
    "http://www.imdb.com/title/tt1034032/"
    )

firewall = media.Movie(
    "Firewall",
    "2006",
    3,
    105,
    "Richard Loncraine",
    "Harrison Ford, Virginia Madsen, Paul Bettany, Carly Schroeder",
    "A security specialist is forced to rob the bank that he's \
    protecting to pay his family's ransom.",
    "https://upload.wikimedia.org/wikipedia/en/a/a9/Firewall_2.jpg",
    "https://www.youtube.com/watch?v=aLtVpOUEwnI",
    "http://www.imdb.com/title/tt0408345/"
    )

virtuosity = media.Movie(
    "Virtuosity",
    "1995",
    2,
    106,
    "Brett Leonard",
    "Denzel Washington, Russell Crowe, Kelly Lynch, Stephen Spinella",
    "A virtual reality sim created using the personalities of serial killers \
    escapes into the real world",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Virtuosity_ver2.jpg",
    "https://www.youtube.com/watch?v=8Qj4h_BZYIY",
    "http://www.imdb.com/title/tt0114857/"
    )

algorithm = media.Movie(
    "Algorithm",
    "2014",
    1,
    91,
    "Jonathan Schiefer",
    "Raphael Barker, Keith Barletta, Julie Ceballos, Joey Devine",
    "A hacker discovers a mysterious government computer program. \
    He breaks in and is thrust into a revolution.",
    "https://www.thewebmaster.com/media/uploads/files/algorithm_mPCiDFk.jpg",
    "https://www.youtube.com/watch?v=tyTUVovCp5s",
    "http://www.imdb.com/title/tt0181689/"
    )

the_social_network = media.Movie(
    "The Social Network",
    "2010",
    5,
    120,
    "David Fincher",
    "Jesse Eisenberg, Andrew Garfield, Justin Timberlake",
    "Harvard student Mark Zuckerberg creates the social networking site \
    Facebook",
    "https://upload.wikimedia.org/wikipedia/en/7/7a/"
    "Social_network_film_poster.jpg",
    "https://www.youtube.com/watch?v=lB95KLmpLR4",
    "http://www.imdb.com/title/tt1285016/"
    )

middle_men = media.Movie(
    "Middle Men",
    "2002",
    4,
    105,
    "George Gallo",
    "George Gallo, Andy Weiss",
    "Chronicles Jack Harris, one of the pioneers of internet commerce, \
    as he wrestles with his morals.",
    "https://upload.wikimedia.org/wikipedia/en/7/7a/Middle_men_poster.jpg",
    "https://www.youtube.com/watch?v=m3gcb_9Q10E",
    "http://www.imdb.com/title/tt1251757/"
    )

pirates_of_silicon_valley = media.Movie(
    "Pirates of Silicon Valley",
    "1999",
    3,
    95,
    "Martyn Burke",
    "Anthony Michael Hall, Noah Wyle, Joey Slotnick",
    "This is a biographical film about the men behind Apple and Microsoft.",
    "https://upload.wikimedia.org/wikipedia/en/3/30/Movieposterposv.jpg",
    "https://www.youtube.com/watch?v=lEyrivrjAuU",
    "http://www.imdb.com/title/tt0168122/"
    )

movies = [
    the_matrix, ghost_in_the_shell, the_girl_with_the_dragon_tatoo,
    minority_report, snowden, the_internship, twenty_three, sneakers,
    wargames, the_thirteenth_floor, existenz, tron, underground,
    wierd_science, eagle_eye, swordfish, takedown, hackers, the_fifth_estate,
    onepoint0, antitrust, the_computer_wore_tennis_shoes, the_net, gamer,
    firewall, virtuosity, algorithm, the_social_network, middle_men,
    pirates_of_silicon_valley
    ]

fresh_tomatoes.open_movies_page(movies)
