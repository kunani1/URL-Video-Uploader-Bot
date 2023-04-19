import os


class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get(
        "BOT_TOKEN", "5998213610:AAEwEcIo-zrXiEflQ1OB-hNAh1qOpAxd2B4")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", 11029886))
    API_HASH = os.environ.get("API_HASH", "4e74899bfd41879c6a4b48cf6a07f456")
    # Get these values from my.telegram.org
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 4194304000  # 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(128)
    # default thumbnail to be used in the videos
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # your telegram id
    OWNER_ID = int(os.environ.get("OWNER_ID", "1618347551"))
    SESSION_NAME = "UPLOADER-X-BOT"
    # database uri (mongodb)
    DATABASE_URL = os.environ.get(
        "DATABASE_URL", "mongodb://mongo:zYftIyb1U9FILZKKgNPW@containers-us-west-140.railway.app:5739")
    MAX_RESULTS = "50"
    PREMIUM_USER = os.environ.get("PREMIUM_USER", "True")
