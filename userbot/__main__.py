# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# Copyright (C) 2021 TeamUltroid for autobot
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
#
""" Userbot start point """

import sys
from importlib import import_module

import requests
from pytgcalls import idle

from userbot import BOT_TOKEN, BOT_VER, DEVS, LOGS, bot
from userbot.modules import ALL_MODULES
from userbot.utils import autobot, checking
from userbot.client import man_userbot_on, multiman

try:
    client = multiman()
    user = bot.get_me()
    blacklistman = requests.get(
        "https://raw.githubusercontent.com/mrismanaziz/Reforestation/master/manblacklist.json"
    ).json()
    if user.id in blacklistman:
        LOGS.warning(
            "MAKANYA GA USAH BERTINGKAH GOBLOK, USERBOTnya GUA MATIIN NAJIS BANGET DIPAKE JAMET KEK LU.\nCredits: @mrismanaziz"
        )
        sys.exit(1)
    if 844432220 not in DEVS:
        LOGS.warning(
            f"EOL\nMan-UserBot v{BOT_VER}, Copyright © 2021-2022 ʀɪsᴍᴀɴ• <https://github.com/mrismanaziz>"
        )
        sys.exit(1)
except Exception as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info(
    f"Jika {user.first_name} Membutuhkan Bantuan, Silahkan Tanyakan di Grup https://t.me/SharingUserbot"
)

LOGS.info(f"Man-Userbot ⚙️ V{BOT_VER} [🔥 BERHASIL DIAKTIFKAN! 🔥]")


bot.loop.run_until_complete(checking())
bot.loop.run_until_complete(man_userbot_on())
if not BOT_TOKEN:
    bot.loop.run_until_complete(autobot())
idle()
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
