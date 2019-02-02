from backend.movies.yst_am import YstAmProvider
from backend.subtitles.yify import YifyPorivder
from credentials import token
from bot import MoviesBot

bot = MoviesBot(token, YstAmProvider(), YifyPorivder())
bot.start()