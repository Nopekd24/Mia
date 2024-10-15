class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 26950231
    API_HASH = "2111ec3bde28f2c4190c490eb5526238"

    CASH_API_KEY = ""  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://koyeb-adm:aj2JdlE4ubks@ep-winter-wildflower-a2qa55in.eu-central-1.pg.koyeb.app/koyebdb"  # A sql database url from https://aiven.io/ Create As Database postgresql

    EVENT_LOGS = ()  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://Aanandkd:24112908@cluster01.mry06.mongodb.net/"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://envs.sh/TqG.jpg"

    SUPPORT_CHAT = "back2home1"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "8190445173:AAHAcLjvF6Vvlk--xlIKpcNjJJidvbqVWFE"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = ""  # Get this value from https://timezonedb.com/api

    OWNER_ID = 7229313541  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
