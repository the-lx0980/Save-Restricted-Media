from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH")
      API_ID = int(getenv("API_ID", 0))
      BOT_TOKEN = getenv("BOT_TOKEN", "")
