import discord
import asyncio

from credentials import token
from search import search_titles

client = discord.Client()

def constructMovieEmbed(movie, also=[]):
    embed = discord.Embed(title='{} | {}'.format(movie.name, str(movie.year)), description=movie.description)
    embed.set_thumbnail(url=movie.thumbnail)
    for download in movie.downloads:
        embed.add_field(name=download['title'], value="[Download]({})".format(download['url']), inline=False)
    embed.set_footer(text="Did you mean:\n" + ', '.join([m.name for m in also]))
    return embed

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!movie'):
        query = message.content[len('!movie') + 1:]
        tmp = await client.send_message(message.channel, 'Proccessing...')
        movies = await search_titles(query)
        if len(movies) == 0:
            await client.edit_message(tmp, "Sorry, I didn't find anything.")
        elif len(movies) == 1:
            await client.edit_message(tmp, 'Got It!', embed=constructMovieEmbed(movies[0]))
        elif len(movies) > 1:
            alsoFound = movies[1:]
            await client.edit_message(tmp, 'Found some, here is the best one', embed=constructMovieEmbed(movies[0], also=alsoFound))

client.run(token)