import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that came to life",
                        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc" )

avatar = media.Movie("Avatar",
                     "A marine on an aliean planet",
                     "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                     "https://youtu.be/d1_JBMrrYw8?t=15")

fury = media.Movie("Fury",
                     "portrays US tank crews in Nazi Germany during the final days of World War II.",
                     "https://en.wikipedia.org/wiki/Fury_(2014_film)#/media/File:Fury_2014_poster.jpg",
                     "https://youtu.be/-OGvZoIrXpg?t=7")
fury.show_trailer()
