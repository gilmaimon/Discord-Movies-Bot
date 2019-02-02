"""
    Entity to represent a subtitles for a specific movie in some language 
    
    @movie_title String -> the target movie title
    @imdb_id String -> imdb id of the target movie
    @language String -> the language of the subtitles (free text)
    @download_url String -> a url from which the subtitles can be downloaded (directly, url)
"""
class Subtitles:
    def __init__(self, movie_title, imdb_id, language, download_url):
        self.movie_title = movie_title
        self.imdb_id = imdb_id
        self.language = language
        self.download_url = download_url