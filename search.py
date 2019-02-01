import aiohttp
import asyncio
import json

class MovieSnippet:
    def __init__(self, title, year, img, url):
        self.title = title
        self.year = year
        self.img = img
        self.url = url

    def __str__(self):
        return "MovieSnippet -> {} year: {}\n\timg: {}\n\turl: {}\n".format(self.title, self.year, self.img, self.url)

    @staticmethod
    def fromJson(data):
        title = data['title']
        year = data['year']
        img = data['img']
        url = data['url']
        return MovieSnippet(title, year, img, url)

class QueryResponse:
    def __init__(self, status, movies):
        self.status = status
        self.movies = movies

    def __str__(self):
        return "QueryResponse -> status: {},\nmovies: {}".format(self.status, [str(m) for m in self.movies])

    @staticmethod
    def fromJson(data):
        status = data['status']
        if status == 'ok' and 'data' in data:
            movies = [MovieSnippet.fromJson(movie) for movie in data['data']]
        else:
            movies = []
        return QueryResponse(status, movies)

async def fetch_movies(session, query):
    params = {'query': query}
    async with session.get('https://yts.am/ajax/search', params=params) as response:
        body = await response.text()
        bodyJson = json.loads(body)
        return QueryResponse.fromJson(bodyJson)

import re
from movie import Movie

async def fetch_whole_movie(session, url):
    async with session.get(url) as response:
        body = await response.text()
        title = re.findall('<h1>(.+)</h1>', body)[0]
        year, genere = re.findall('<h2>(.+)</h2>', body)[0:2]
        description = re.findall('<p class="hidden-xs">(.+)</p>', body)[0].strip()
        downloads = [res for res in filter(lambda x: 'span' not in x[1], re.findall('<a href="(.+)" rel="nofollow" title=".+">(.+)</a>', body))]
        downloads = [{'url': x[0], 'title': x[1]} for x in downloads]
        thumbnails = re.findall(r"""<div id="movie-poster".*?><img.*?src=\"(.+?)\" .*?</div>""", body.replace('\n', ''))
        print(thumbnails)
        return Movie(title, year, genere, description, thumbnails[0], downloads, url)

async def search_titles(query, snippet=False):
    async with aiohttp.ClientSession() as session:
        queryResponse = await fetch_movies(session, query)
        moviesSorted = sorted(queryResponse.movies, key = lambda x: (abs(len(x.title) - len(query)), x.title) )
        if snippet:
            return moviesSorted
        movies = []
        for movie in moviesSorted:
            movies += [await fetch_whole_movie(session, movie.url)]
        return movies