import discord
import asyncio

class MoviesBot:
    """
        @token String -> the api token for the Discord API
        @movies_provider -> allows searching movies
    """
    def __init__(self, token, movies_provider):
        self.__token = token
        self.__provider = movies_provider
        self.__client = discord.Client()

        @self.__client.event
        async def on_ready(): await self.handle_ready()

        @self.__client.event
        async def on_message(message): await self.handle_message(message)

    @staticmethod
    def __get_embed_for_query_result(movie, also=[]):
        # Title and Description
        formatted_title = '{} | {}'.format(movie.title, str(movie.year))
        embed = discord.Embed(title=formatted_title, description=movie.description)
        
        # Thumbnail
        embed.set_thumbnail(url=movie.thumbnail)

        # Download Links
        for download in movie.downloads:
            download_link = "[Download]({})".format(download['url'])
            embed.add_field(name=download['title'], value=download_link, inline=False)
        
        # Footer (Other search options)
        if len(also) > 0:
            other_options = ', '.join(['{} ({})'.format(m.title, m.year) for m in also])
            embed.set_footer(text="Did you mean:\n" + other_options)

        return embed

    async def handle_ready(self):
        # Log
        print('Logged in as')
        print(self.__client.user.name)
        print(self.__client.user.id)
        print('------')

    @staticmethod
    def is_movies_request(message):
        content = message.content
        # Check if keyword matches
        for keyword in ['!movie', '!movies', '!moviebot', '!moviesbot']:
            # If found a match, return True
            if content.startswith(keyword + ' ') and len(content) > len(keyword + ' '):
                return True

        # Return False in case no keyword matched
        return False

    @staticmethod
    def get_query_from_command(message):
        content = message.content
        # Remove first word
        words = content.split(' ')
        return ' '.join(words[1:])

    async def handle_message(self, message):
        if self.is_movies_request(message):
            # Query movies
            query = self.get_query_from_command(message)
            tmp = await self.__client.send_message(message.channel, 'Proccessing...')
            movies = await self.__provider.search_movies(query)
            
            # If no movies were found
            if len(movies) == 0:
                # present message
                await self.__client.edit_message(tmp, "Sorry, I didn't find anything.")
            # If only found one movie, return it as single result
            elif len(movies) == 1:
                # construct message and present it
                embed = self.__get_embed_for_query_result(movies[0])
                await self.__client.edit_message(tmp, 'Got It!', embed=embed)
            # If found multiple movies, return the best one and other as hints
            elif len(movies) > 1:
                alsoFound = movies[1:]
                # construct message and present it
                embed = self.__get_embed_for_query_result(movies[0], also=alsoFound)
                await self.__client.edit_message(tmp, 'Found some, here is the best one', embed=embed)

    def start(self):
        # start the bot
        self.__client.run(self.__token)