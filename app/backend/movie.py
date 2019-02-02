"""
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