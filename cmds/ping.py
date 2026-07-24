import discord
from discord import app_commands
from discord.ext import commands
from things import wait

class ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Returns latency of the bot.")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(embed=wait(), ephemeral=True)

        latency = round(self.bot.latency * 1000)
        embed = discord.Embed(
            title="Pong!",
            description=f"Latency: {latency}ms.")
        await interaction.edit_original_response(embed=embed)
