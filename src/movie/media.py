import webbrowser
import os

class Vedio():
    def __init__(self, title):
        self.title = title

class Movie(Vedio):
    #VALID_RATINGS = ["G","PG","PG-13","R"]
    """This class provides a way to store movie related information"""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        Vedio.__init__(movie_title)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class TvShow(Vedio):
    def __init__(self, tv_title, tv_season, tv_episode, tv_station):
        Vedio.__init__(tv_title)
        self.season = tv_season
        self.episode = tv_episode
        self.station = tv_station

    def get_local_listing(self):
        os.open(self.station,'r')