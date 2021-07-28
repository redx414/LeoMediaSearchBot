import os
import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'test4')
USER_SESSION = environ.get('USER_SESSION', 'test5')
APP_ID = int(environ('APP_ID', 6657305))
API_HASH = environ('API_HASH', '10ca9a965d788b977b45226e82dd4174')
BOT_TOKEN = environ('BOT_TOKEN', '1933475915:AAFKb67RXRgtGsquv7xCvvXFhuIucTD6Wf8')
USERBOT_STRING_SESSION = environ.get('USERBOT_STRING_SESSION', 'test4')
BOT_OWNER = int(os.environ.get("BOT_OWNER", 1859164817))
BOT_USERNAME = os.environ.get("BOT_USERNAME", "Test_414_bot")

# Bot settings
MAX_RESULTS = int(environ.get('MAX_RESULTS', 10))
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS', 1859164817].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS', -1001572776649].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001175433925))

# MongoDB information
DATABASE_URI = environ['DATABASE_URI', 'mongodb+srv://test4:rUq!657yAGYBa_S@cluster0.rgpna.mongodb.net/myFirstDatabase?retryWrites=true&w=majority']
DATABASE_NAME = environ['DATABASE_NAME', 'test4']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

#for broadcast and force sub
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", -1001404671682)

#ban/unban
BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))

#for broadcast and user stts db
MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://test5:rUq!657yAGYBa_S@cluster0.lmciz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
SESSION_NAME = os.environ.get("SESSION_NAME", "test5")

# Messages
default_start_massege = """
**Hello {} 

✦You Must Join Our Channel to Search a Movie😇 

✧(Movie Search කිරීමට නම් ඔයා අපේ Channel එකට Join වෙලා තිබීම අත්‍යවශ්‍ය වේ😇) 

✦You Will Recieve a Message Saying '❌Unsupported Message type.'😒 Just Ignore It😌 

✧(ඔයාලට '❌Unsupported Message type.' කියල Error එකක් පෙන්නයි😒 ඒක එච්චර ගනන් ගන්න එපා😌) 

✦Click the Search Button Below to Find the Movie You Want😊 

✧(ඔයාට අවශ්‍ය Movie එක ලබා ගැනීමට Search Button එක Click කරන්න😊)**
"""

default_share_button_text = """
**🇱🇰 RED X Bot 🇱🇰** 

'You Can Get Movies, TV Series & Games By Using This Bot😊' 

Bot : {username}😍 
Update Channel : @redx414news 
Developer : @RedX14
"""

START_MSG = environ.get('START_MSG', default_start_massege)

SHARE_BUTTON_TEXT = environ.get('SHARE_BUTTON_TEXT', default_share_button_text)

INVITE_MSG = environ.get('INVITE_MSG', 'Please join @.... to use this bot')
