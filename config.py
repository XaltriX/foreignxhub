import logging
from logging.handlers import RotatingFileHandler

# Bot Configuration
LOG_FILE_NAME = "bot.log"
PORT = '5010'
OWNER_ID = 5706788169

MSG_EFFECT = 5046509860389126442

SHORT_URL = "earnlinks.in" # shortner url 
SHORT_API = "7bd8bb008b14e25c629b12456233dcc4da3a474f" 
SHORT_TUT = "https://t.me/HTODLINKZ/7"

# Bot Configuration
SESSION = "yato"
TOKEN = "642712"
API_ID = "24955235"
API_HASH = "f317b3f7bbe390346d8b46868cff0de8"
WORKERS = 5

DB_URI = "mongodb+srv://rs92573993688:pVf4EeDuRi2o92ex@cluster0.9u29q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "yato"

FSUBS = [[-1001980994910, True, 10]] # Force Subscription Channels [channel_id, request_enabled, timer_in_minutes]
# Database Channel (Primary)
DB_CHANNEL = -1003526493094   # just put channel id dont add ""
# Multiple Database Channels (can be set via bot settings)
# DB_CHANNELS = {
#     "-1002595092736": {"name": "Primary DB", "is_primary": True, "is_active": True},
#     "-1001234567890": {"name": "Secondary DB", "is_primary": False, "is_active": True}
# }
# Auto Delete Timer (seconds)
AUTO_DEL = 600
# Admin IDs
ADMINS = [5706788169]
# Bot Settings
DISABLE_BTN = True
PROTECT = False

# Messages Configuration
MESSAGES = {
    "START": "<b>›› ʜᴇʏ!!, {first} ✨<blockquote>🌍 ᴅᴀɪʟʏ ᴠɪᴅᴇꜱʜɪ ᴀᴅᴜʟᴛ ᴠɪᴅᴇᴏꜱ<br>🎥 ᴅɪʀᴇᴄᴛ ᴠɪᴅᴇᴏ • ɴᴏ ʟɪɴᴋꜱ<br>⚡ ꜰᴀꜱᴛ & ꜱᴍᴏᴏᴛʜ ᴜᴘᴅᴀᴛᴇꜱ<br><br>📲 ꜰᴏʀ ᴍᴏʀᴇ ᴠɪᴅᴇᴏꜱ ᴊᴏɪɴ:<br>https://t.me/+eCphRNJtWLU5NmU9</blockquote></b>",
    "FSUB": "<b><blockquote>›› ʜᴇʏ {first} ✨</blockquote>\n📁 ʏᴏᴜʀ ꜰɪʟᴇ ɪꜱ ʀᴇᴀᴅʏ ‼️\n\n🔔 ɪᴛ ʟᴏᴏᴋꜱ ʟɪᴋᴇ ʏᴏᴜ ʜᴀᴠᴇɴ’ᴛ ᴊᴏɪɴᴇᴅ ᴏᴜʀ ᴄʜᴀɴɴᴇʟꜱ ʏᴇᴛ.\n\n👉 ᴊᴏɪɴ ɴᴏᴡ ᴛᴏ ᴜɴʟᴏᴄᴋ ʏᴏᴜʀ ꜰɪʟᴇꜱ\n⚡ ꜰᴀꜱᴛ • ꜱᴍᴏᴏᴛʜ • ᴘʀᴇᴍɪᴜᴍ</b>",
    "ABOUT": "<b>›› ғᴏʀ ᴍᴏʀᴇ: @Linkz_Wallah \n <blockquote expandable>›› ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/NeonGhost_Network'>Cʟɪᴄᴋ ʜᴇʀᴇ</a> \n›› ᴏᴡɴᴇʀ: @NeonGhost\n›› ʟᴀɴɢᴜᴀɢᴇ: <a href='https://docs.python.org/3/'>Pʏᴛʜᴏɴ 3</a> \n›› ʟɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ ᴠ2</a> \n›› ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>Mᴏɴɢᴏ ᴅʙ</a> \n›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @NeonGhost</b></blockquote>",
    "REPLY": "<b>For More Join - @Hanime_Arena</b>",
    "SHORT_MSG": "<b>📊 ʜᴇʏ {first}, \n\n‼️ ɢᴇᴛ ᴀʟʟ ꜰɪʟᴇꜱ ɪɴ ᴀ ꜱɪɴɢʟᴇ ʟɪɴᴋ ‼️\n\n ⌯ ʏᴏᴜʀ ʟɪɴᴋ ɪꜱ ʀᴇᴀᴅʏ, ᴋɪɴᴅʟʏ ᴄʟɪᴄᴋ ᴏɴ ᴏᴘᴇɴ ʟɪɴᴋ ʙᴜᴛᴛᴏɴ..</b>",
    "START_PHOTO": "https://graph.org/file/510affa3d4b6c911c12e3.jpg",
    "FSUB_PHOTO": "https://telegra.ph/file/7a16ef7abae23bd238c82-b8fbdcb05422d71974.jpg",
    "SHORT_PIC": "https://telegra.ph/file/7a16ef7abae23bd238c82-b8fbdcb05422d71974.jpg",
    "SHORT": "https://telegra.ph/file/8aaf4df8c138c6685dcee-05d3b183d4978ec347.jpg"
}

def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
