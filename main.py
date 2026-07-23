"""
main.py

Main file of bot
"""

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN: raise ValueError("Discord Bot Token was not set or found.")

