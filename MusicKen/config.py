import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "MOODITON")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/a2dc4c418afd06f9006fb.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "DARK_HYPERMUXIC")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "AVENGERS_PATHSHALA")
PROJECT_NAME = getenv("PROJECT_NAME", "HYPER X 𝙈𝘼𝙉")
OWNER = getenv("OWNER", "@HYPER_KING_2417")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/AKD1317/HYPER-X-0.1")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
PMPERMIT = getenv("PMPERMIT", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
KENKAN = getenv("hyperX", "https://telegra.ph/file/a2dc4c418afd06f9006fb.jpg")
