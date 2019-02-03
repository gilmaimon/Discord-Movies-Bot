"""
    Entity to represent a fully known and fetched movie.
    
    @title String -> the movie title
    @year int -> the movie release year
    @genere String -> the generes of the movie (free text)
    @description String -> a resonably long description (free text)
    @thumbnail String -> link to a thumbnail (image url)
    @downloads [{title, url}] -> download links as an array of dictionaries
    @original_url String -> an original url for the site the downloads are from (url)
    @imdb_id String -> imdb id to uniquely identify the movie 
"""
class Movie(object):
    def __init__(self, title, year, genere, description, thumbnail, downloads, original_url, imdb_id):
        self.title = title
        self.year = int(year)
        self.genere = genere
        self.description = description
        self.thumbnail = thumbnail
        self.downloads = downloads
        self.original_url = original_url
        self.imdb_id = imdb_id

    @staticmethod
    def minimal(title, year):
        return Movie(title, year, None, None, None, None, None, None)

    def __str__(self):
        return "Movie: {} ({}). imdb_id: {}".format(self.title, self.year, self.imdb_id)