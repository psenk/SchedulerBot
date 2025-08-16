#
# IMPORTS
#

# discord.py library
import discord
# bot commands framework library
from discord.ext import commands
# python logging library
import logging
# python operating system interface library
import os
# python uuid library
import uuid
# python datetime library
from datetime import datetime
# environment variable interfacing library
from dotenv import load_dotenv


#
# CONSTANTS
#

## AUTH

# load .env file
load_dotenv(override=True)
# get DISCORD_TOKEN key from .env file
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

#
# VARIABLES
#

## BOT

# creating an intent (discord permissions for bot) object with all intents enabled
intents = discord.Intents.all()
# explicitly enabling intents
intents.message_content = True
intents.members = True
# creating bot object
bot = commands.Bot(intents=intents)

## LOGGING

# getting logger or create if unmade
bot_logger = logging.getLogger(__name__)
# add specific handler to logger
bot_logger.addHandler(logging.FileHandler(filename='logs/bot.log', encoding='utf-8', mode='w'))
# set logging level
bot_logger.setLevel(logging.DEBUG)

#
# BOT COMMANDS
# 

"""
User command for scheduling content to learn.

Arguments:
- interaction - Discord interaction object

Return:
- None
"""
@bot.tree.command(name='schedule', description='Command to schedule a time to learn content with a certified trainer.')
async def schedule(interaction: discord.Interaction) -> None:
    pass

#
# DISCORD API CODE
#

"""
Bot event, runs whenever the bot starts up.

Arguments:
- None

Return:
- None
"""
@bot.event
async def on_ready() -> None:
    print('Scheduling bot online.')
    bot_logger.info('Scheduling bot online.')

# final command to run the bot
# requires token and log handler with level specified
if DISCORD_TOKEN:
    bot.run(DISCORD_TOKEN, log_handler=logging.FileHandler(filename='logs/discord.log', encoding='utf-8', mode='w'), log_level=logging.DEBUG)
