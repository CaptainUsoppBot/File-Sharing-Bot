#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6569543312:AAHJ0HLBgkn-iMG2fJprJQlY2ivwn9mu0Tw")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "26254064"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "72541d6610ae7730e6135af9423b319c")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002010070803"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5296584067"))

#Port
PORT = os.environ.get("PORT", "8000")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://inanstcompany:SJUDMA5sleyVNKPY@cluster0.trsvbyw.mongodb.net/")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002125561929"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first} I'm a bot who can store files and share it via spacial links")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5296584067").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Claim your File After Joining my Channal")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(5296584067)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
