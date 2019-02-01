import discord
import asyncio

from credentials import token
from search import search_titles

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

def constructMovieEmbed(movie):
    embed = discord.Embed(title=movie.name, description=movie.description)
    embed.set_thumbnail(url=movie.thumbnail)
    for download in movie.downloads:
        embed.add_field(name=download['title'], value="[Download]({})".format(download['link']), inline=False)
    return embed

@client.event
async def on_message(message):
    if message.content.startswith('!movie'):
        query = message.content[len('!movie') + 1:]
        tmp = await client.send_message(message.channel, 'Proccessing...')
        query_result = await search_titles(query)
        await client.edit_message(tmp, '\n'.join([str(m.url) for m in query_result.movies]))

client.run(token)
