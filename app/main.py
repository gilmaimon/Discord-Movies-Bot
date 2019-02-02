from backend.movies.yst_am import YstAmProvider
from backend.subtitles.yifysubtitles import YifySubtitlesPorivder
from credentials import token
from bot import MoviesBot

bot = MoviesBot(token, YstAmProvider(), YifySubtitlesPorivder('Hebrew'))
bot.start()