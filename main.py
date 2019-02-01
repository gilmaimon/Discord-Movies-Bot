import discord
import asyncio
from credentials import token

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

def constructMovieEmbed(name, description, thumbnail, downloads):
    embed = discord.Embed(title=name, description=description)
    embed.set_thumbnail(url=thumbnail)
    for download in downloads:
        embed.add_field(name=download['title'], value="[Download]({})".format(download['link']), inline=False)
    return embed

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

    elif message.content.startswith('!movie'):
        query = message.content[len('!movie') + 1:]
        #movie = await search_movies(query)
        await client.send_message(message.channel, 'Movies Bot', embed=constructMovieEmbed("The Patriot", """It is 1776 in colonial South Carolina. Benjamin Martin, a French-Indian war hero who is haunted by his past, now wants nothing more than to live peacefully on his small plantation, and wants no part of a war with the most powerful nation in the world, Great Britain. Meanwhile, his two eldest sons, Gabriel and Thomas, can't wait to enlist in the newly formed "Continental Army." When South Carolina decides to join the rebellion against England, Gabriel immediately signs up to fight...without his father's permission. But when Colonel William Tavington, British dragoon, infamous for his brutal tactics, comes and burns the Martin Plantation to the ground, tragedy strikes. Benjamin quickly finds himself torn between protecting his family, and seeking revenge along with being a part of the birth of a new, young, and ambitious nation.""", "https://img.yts.am/assets/images/movies/The_Patriot_Extended_Cut_2000/medium-cover.jpg", [{"title": "720p.BluRay", "link": "https://yts.am/torrent/download/99C70C844559FA7457E24E0A5C617ACAD4C610EF"}, {"title": "1080p.BluRay", "link": "https://yts.am/torrent/download/4590A23657AE7A7D51726E4FD8D5CD2D1A8765AD"}]))

client.run(token)
