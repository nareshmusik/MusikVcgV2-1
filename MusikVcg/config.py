# DAISYXMUSIC- Telegram bot project
# Copyright (C) 2021  Roj Serbest
# Copyright (C) 2021  Inuka Asith
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Modified by Inukaasith

import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQAO_kZdAxU9YECYdhhMpR6ROMP4nFVcwWDtFTS19KbBE7HXqLoZMH9fkySOX0R2PSTxvNb1OetH0fka0m491Hm2dcd-ec7zDTqkJp6Lv6syCssXyTme1EDRU38fx9ALyUoK0ZQjxJ4n1go9YTf0YgEqkO-NEkSAOniBmHgubHxE4ndts10K-TjyoGuSyWCsxog12XBp1DVIlSBvCkO_VcRnZHSOSx8GAtJfV7zI1bPXOqmwVj53FiCvof6QRhtQJ3wJr1Jq3yJsoL-jHqdvGKXKj2nxHIAjnMM55S8U0PLy4-r1anMKOvGDiVxNBrD7t5PXaSBAFsnRkaeOhA33uqrTdZu9tAA")
BOT_TOKEN = getenv("BOT_TOKEN", "2006768713:AAEbbpfwMjj38t0L1I4ISUymhQeWHotyvgI") 
BOT_NAME = getenv("BOT_NAME", " naresh private") 
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "urfavresh")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/e5d9523a3175991bdba12.png")
admins = {}
API_ID = int(getenv("API_ID", "7101691")
API_HASH = getenv("API_HASH", "c63ca59280c5dceaf1171e46e436cd17") 
BOT_USERNAME = getenv("BOT_USERNAME", "NprivateBOT") 
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "MusikVcg")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "mutuualanaja)
PROJECT_NAME = getenv("PROJECT_NAME", "MusikVcg")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/CollinFowel/MusikVcgV2")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "180"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
