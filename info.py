import re
from os import environ, getenv
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '24579842'))
API_HASH = environ.get('API_HASH', 'ec6105bf1a02c98f837300546dc341d1')
BOT_TOKEN = environ.get('BOT_TOKEN', "6596630313:AAHYsHgQzWs5atcOF1AIdODVCtldfQ0MbdU")
TIMEZONE = environ.get("TIMEZONE", "Asia/Kolkata")
# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 150))
USE_CAPTION_FILTER = is_enabled((environ.get('USE_CAPTION_FILTER', 'True')), True)

PICS = (environ.get('PICS', 'https://graph.org/file/6092ad90bdc8b12dbf4b2.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/6092ad90bdc8b12dbf4b2.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://graph.org/file/030bd90333f090dafe064.jpg")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/6092ad90bdc8b12dbf4b2.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1991522624').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001867538832').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID')
reqst_channel = environ.get('REQST_CHANNEL', '-1002023614254')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = is_enabled((environ.get("NO_RESULTS_MSG", 'True')), False)

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://thhbot:happyhour@cluster0.4kenaya.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "MINATO")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

premium = environ.get('PREMIUM_LOGS', '-1002114337101')
PREMIUM_LOGS = int(premium) if premium and id_pattern.search(premium) else None

IMPORT_JK_SITE = environ.get('IMPORT_JK_SITE', 'riplinker.in')
IMPORT_JK_API = environ.get('IMPORT_JK_API', 'edaa2a506f920af47a82e5f41ba3b30510df335d')
SHORT_MODE = is_enabled((environ.get("SHORT_MODE","False")), False)

# Others
IS_VERIFY = is_enabled((environ.get('IS_VERIFY', 'True')), False)
HOW_TO_VERIFY = environ.get('HOW_TO_VERIFY', "https://youtube.com/shorts/b-vzSXDlviM?si=w8AXzSJpc6oh_hPi")
VERIFY2_URL = environ.get('VERIFY2_URL', "aslink.in")
VERIFY2_API = environ.get('VERIFY2_API', "d4bb1d041de18cd42c31a72a63aff1c727cbbc0a")
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'aslink.in')
SHORTLINK_API = environ.get('SHORTLINK_API', 'd4bb1d041de18cd42c31a72a63aff1c727cbbc0a')
IS_SHORTLINK = is_enabled((environ.get('IS_SHORTLINK', 'False')), False)
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-1001966591245').split()]
MAX_B_TN = environ.get("MAX_B_TN", "7")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/Happy_Hour_Friends')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/The_Happy_Hours')
MSG_ALRT = environ.get('MSG_ALRT', 'Wʜᴀᴛ Aʀᴇ Yᴏᴜ Lᴏᴏᴋɪɴɢ Aᴛ ?')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1002139657732))
LAZY_GROUP_LOGS = int(environ.get('LAZY_GROUP_LOGS', -1002049370768))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Happy_Hour_Friends')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", f"{script.CAPTION}")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

# Streaming
BIN_CHANNEL = environ.get("BIN_CHANNEL", "-1001992201683")
if len(BIN_CHANNEL) == 0:
    logging.error('BIN_CHANNEL is missing, exiting now')
    exit()
else:
    BIN_CHANNEL = int(BIN_CHANNEL)

PORT = int(environ.get('PORT', 8080))
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
    "https://{}:{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'LusiBot'))
MULTI_CLIENT = False
name = str(environ.get('name', 'Lusifilms'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))

else:
    ON_HEROKU = False
HAS_SSL=bool(getenv('HAS_SSL',False))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "https://{}/".format(FQDN)
REPO_OWNER = "JKDeveloperr"

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"