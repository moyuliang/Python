import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story","A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar","A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

beauty_beast = media.Movie("Beauty and the Beast (2017 film)","The film is based on Disney's 1991 animated film of the same name, itself an adaptation of Jeanne-Marie Leprince de Beaumont's eighteenth-century fairy tale.",
                          "https://upload.wikimedia.org/wikipedia/en/d/d6/Beauty_and_the_Beast_2017_poster.jpg",
                          "https://www.youtube.com/watch?v=g-DkY-drN9Q")

school_of_rock = media.Movie("Scool of Rock","Storyline",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille","Storyline",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris","Storyline",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=atLg2wQQxvU")

movies = [toy_story,avatar,beauty_beast,school_of_rock,ratatouille,midnight_in_paris]
#fresh_tomatoes.open_movies_page(movies)
print (media.Movie.VALID_RATINGS)
# print("media.Movie.__doc__ : "+media.Movie.__doc__)
# print("media.Movie.__name__ : "+media.Movie.__name__)
# print("media.Movie.__module__ : "+media.Movie.__module__)