import aiohttp
import asyncio
import json

class QueryResponseMovie:
    def __init__(self, title, year, img, url):
        self.title = title
        self.year = year
        self.img = img
        self.url = url

    def __str__(self):
        return "QueryResponseMovie -> {} year: {}\n\timg: {}\n\turl: {}\n".format(self.title, self.year, self.img, self.url)

    @staticmethod
    def fromJson(data):
        title = data['title']
        year = data['year']
        img = data['img']
        url = data['url']
        return QueryResponseMovie(title, year, img, url)

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
            movies = [QueryResponseMovie.fromJson(movie) for movie in data['data']]
        else:
            movies = []
        return QueryResponse(status, movies)

async def fetch_movies(session, query):
    params = {'query': query}
    async with session.get('https://yts.am/ajax/search', params=params) as response:
        body = await response.text()
        bodyJson = json.loads(body)
        return QueryResponse.fromJson(bodyJson)
            

async def search_titles(query):
    async with aiohttp.ClientSession() as session:
        return await fetch_movies(session, query)
        