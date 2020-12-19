#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ©️ @AmineSoukara

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)
from helper_funcs.chat_base import TRChatBase
from pyrogram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from translation import Translation
from .commands import start

@pyrogram.Client.on_callback_query()
async def cb_handler(c, m):
  cb_data = m.data

  if "home" in cb_data:
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
      await c.edit_message_text(chat_id=m.message.chat.id,
                           message_id=m.message.message_id,
                           text=Translation.START_MSG.format(m.from_user.first_name),
                           reply_markup=markup)

  if "cancel" in cb_data:
      await m.message.delete()
      
  if "helpx" in cb_data:
      button = [[InlineKeyboardButton("🏠 Home", callback_data="home")]]
      markup = InlineKeyboardMarkup(button)
      await c.edit_message_text(chat_id=m.message.chat.id,
                           message_id=m.message.message_id,
                           text=Translation.HELP_USER.format(m.from_user.first_name),
                           disable_web_page_preview=True,
                           reply_markup=markup)

  if "about" in cb_data:
      button = [[InlineKeyboardButton("🏠 Home", callback_data="home")]]
      markup = InlineKeyboardMarkup(button)
      await c.edit_message_text(chat_id=m.message.chat.id,
                           message_id=m.message.message_id,
                           text=Translation.ABOUT.format(m.from_user.first_name),
                           disable_web_page_preview=True,
                           reply_markup=markup)

  if "morehelp" in cb_data:
      button = [[
                InlineKeyboardButton("🌐 Url Upload", callback_data="urldl"),
                InlineKeyboardButton("✍ Renamer", callback_data="renamerx"),
                ],
                [
                InlineKeyboardButton("🎞 YouTube DL", callback_data="ytdl"),
                InlineKeyboardButton("🤖 Feedback", url="t.me/DamienRobot")
                ],
                [InlineKeyboardButton("🏠 Home", callback_data="home")]]
      markup = InlineKeyboardMarkup(button)
      await c.edit_message_text(chat_id=m.message.chat.id,
                           message_id=m.message.message_id,
                           text=Translation.MOREHELP.format(m.from_user.first_name),
                           reply_markup=markup)
  if "ytdl" in cb_data:
      button = [[InlineKeyboardButton("🔙 Back", callback_data="morehelp"),
                InlineKeyboardButton("🏠 Home", callback_data="home")]]
      markup = InlineKeyboardMarkup(button)
      await c.edit_message_text(chat_id=m.message.chat.id,
                           message_id=m.message.message_id,
                           text=Translation.YTDL,
                           disable_web_page_preview=True,
                           reply_markup=markup)

  if "urldl" in cb_data:
      button = [[InlineKeyboardButton("🔙 Back", callback_data="morehelp"),
                InlineKeyboardButton("🏠 Home", callback_data="home")]]
      markup = InlineKeyboardMarkup(button)
      await c.edit_message_text(chat_id=m.message.chat.id,
                           message_id=m.message.message_id,
                           text=Translation.URLDL,
                           disable_web_page_preview=True,
                           reply_markup=markup)

  if "renamerx" in cb_data:
      button = [[InlineKeyboardButton("🔙 Back", callback_data="morehelp"),
                InlineKeyboardButton("🏠 Home", callback_data="home")]]
      markup = InlineKeyboardMarkup(button)
      await c.edit_message_text(chat_id=m.message.chat.id,
                           message_id=m.message.message_id,
                           text=Translation.RENAMERX,
                           disable_web_page_preview=True,
                           reply_markup=markup)
