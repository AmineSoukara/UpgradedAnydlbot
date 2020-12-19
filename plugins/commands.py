#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.chat_base import TRChatBase

def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "Source Cloned User", "1970.01.01.12.00.00")
    return expires_at


@pyrogram.Client.on_message(pyrogram.Filters.command(["help", "about"]))
def help_user(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/help")
    bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode=pyrogram.ParseMode.HTML,
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@pyrogram.Client.on_message(pyrogram.Filters.command(["me"]))
def get_me_info(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/me")
    chat_id = str(update.from_user.id)
    chat_id, plan_type, expires_at = GetExpiryDate(chat_id)
    bot.send_message(
        chat_id=update.chat.id,
        text=Translation.CURENT_PLAN_DETAILS.format(chat_id, plan_type, expires_at),
        parse_mode=pyrogram.ParseMode.HTML,
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )

@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def start(c, m):
      button = [[
                InlineKeyboardButton("💬 Updates Channel", url="t.me/DamienSoukara"),
                InlineKeyboardButton("🗣 Support Group", url="t.me/damienhelp"),
                ],
                [
                InlineKeyboardButton("ℹ About", callback_data="about"),
                InlineKeyboardButton("🤔 Help", callback_data="morehelp")
                ],
                [InlineKeyboardButton("🤴 Developer 🤴", url="t.me/AmineSoukara")]]
      markup = InlineKeyboardMarkup(button)
      await c.send_message(chat_id=m.chat.id,
                           text=Translation.START_TEXT.format(m.from_user.first_name),
                           reply_to_message_id=m.message_id,
                           reply_markup=markup)


@pyrogram.Client.on_message(pyrogram.Filters.command(["upgrade"]))
def upgrade(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/upgrade")
    bot.send_message(
        chat_id=update.chat.id,
        text=Translation.UPGRADE_TEXT,
        parse_mode=pyrogram.ParseMode.HTML,
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )
