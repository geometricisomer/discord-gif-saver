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
DB_PATH = os.getenv("DB_PATH")
if not DB_PATH: raise ValueError("Path for data base was not set or found.")

class Bot(commands.Bot):
    async def setup_hook(self):
        return await super().setup_hook()

bot = Bot(command_prefix="&&&")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

bot.run(TOKEN)
