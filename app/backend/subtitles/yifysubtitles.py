import aiohttp
import asyncio
import re
import socket

from .subtitles import Subtitles

async def get_all_subtitles(title, imdb_id, session):
    url = 'https://www.yifysubtitles.com/movie-imdb/{}/'.format(imdb_id)
    async with session.get(url) as response:
        body = await response.text()

        html_regex = r"""<tr.*?>.*?<span class="sub-lang">(.+?)</span>.*?<a href="/subtitles/(.+?)">.*?</tr>"""
        all_subs_raw = re.findall(html_regex, body)

        all_subs = []
        for lanuage, yify_subs_id in all_subs_raw:
            all_subs.append(Subtitles(
                title, 
                imdb_id,
                lanuage,
                'https://www.yifysubtitles.com/subtitle/{}.zip'.format(yify_subs_id)
            ))
        return all_subs

class YifySubtitlesPorivder:
    def __init__(self, language):
        self.language = language
        pass

    async def search_subtitles(self, movie):
        conn = aiohttp.TCPConnector(family=socket.AF_INET)
        async with aiohttp.ClientSession(connector=conn) as session:
            all_subs = await get_all_subtitles(movie.title, movie.imdb_id, session)
            await session.close()
            for subs in all_subs:
                if subs.language == self.language:
                    return subs
            return None