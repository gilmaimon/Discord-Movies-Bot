import aiohttp
import asyncio
import re
import socket

from .subtitles import Subtitles

async def get_subtitles_for_langid(title, imdb_id, language, session):
    url = 'https://www.opensubtitles.org/en/search/sublanguageid-{}/imdbid-{}'.format(language['opensubs_id'], imdb_id[2:])
    async with session.get(url) as response:
        body = await response.text()
        body = body.replace('\n', '')

        html_regex = r""".*?href="/en/subtitles/(.+?)/(.+?)".*"""
        all_subs_raw = re.findall(html_regex, body)

        all_subs = []
        for opensubtitles_identifier, _ in all_subs_raw:
            all_subs.append(Subtitles(
                title, 
                imdb_id,
                language['lang'],
                'https://www.opensubtitles.org/en/subtitleserve/sub/{}'.format(opensubtitles_identifier),
            ))
        return all_subs

class OpenSubsProvider:
    def __init__(self, opensubs_sublanguageid, lanuage):
        self.lanauage = {
            'opensubs_id': opensubs_sublanguageid,
            'lang': lanuage
        }
        pass

    async def search_subtitles(self, movie):
        conn = aiohttp.TCPConnector(family=socket.AF_INET)
        async with aiohttp.ClientSession(connector=conn) as session:
            all_subs = await get_subtitles_for_langid(movie.title, movie.imdb_id, self.lanauage, session)
            await session.close()
            if len(all_subs) > 0: return all_subs[0]
            else: return None