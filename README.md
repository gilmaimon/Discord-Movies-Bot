[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
# Discord Movies Bot

A discord bot to fetch torrent downloads and subtitles for movies. In chat write `!movies NAME` and the bot will respond with torrent links and some info about the movie.

<p align="center">
  <img src ="https://github.com/gilmaimon/Discord-Movies-Bot/blob/master/screenshots/1.PNG" />
</p>

## Getting Started

These instructions will help you get an instance of MoviesBot running on your server or PC.

### Prerequisites

This project was created using Python3.6, but might work on lower version (3.5/3.4). You do need to have the following modules installed.

- [aiodns](https://github.com/saghul/aiodns) v1.2.0
- [aiohttp](https://github.com/aio-libs/aiohttp) v1.0.5
- [discord.py](https://github.com/Rapptz/discord.py) v0.16.12

*You can get all the dependencies by running:*
```
pip install -r requirements.txt
```

### Installing

create a file named `credentials.py` containing (replace with your discord bot token):
```
token = 'MY-TOKEN'
```

Thats it! Start the bot by running `main.py`.
