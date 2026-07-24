"""
main.py

Main file of the bot
"""

import discord
from discord.ext import commands
import os
from db import setup as setup_db

TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN: raise ValueError("Discord Bot Token was not set or found.")

intents = discord.Intents.default()

class Bot(commands.Bot):
    async def setup_hook(self):
        setup_db()
        for filename in os.listdir("cmds"):
            if filename.endswith(".py") and not filename.startswith("__"): await self.load_extension(f"cmds.{filename[:-3]}")
        try:
            synced = await self.tree.sync()
            print(f"Synced {synced} slash commands.")
        except Exception as e:
            print(f"Slash commands could not be synced: {e}")


bot = Bot(command_prefix="&&&", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

bot.run(TOKEN)
