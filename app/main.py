#Movies
from backend.movies.yst_am import YstAmProvider

# Subs
from backend.subtitles.yifysubtitles import YifySubtitlesPorivder
from backend.subtitles.opensubtitles_org import OpenSubsProvider
from backend.subtitles.multiple_sources import MultipleSourcesProvider

# Bot
from bot import MoviesBot
from credentials import token

bot = MoviesBot(token, YstAmProvider(), MultipleSourcesProvider([YifySubtitlesPorivder('Hebrew'), OpenSubsProvider('heb', 'Hebrew')]))
bot.start()