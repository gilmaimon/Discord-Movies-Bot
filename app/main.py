from backend.yst_am import YstAmProvider
from credentials import token
from bot import MoviesBot

bot = MoviesBot(token, YstAmProvider())
bot.start()