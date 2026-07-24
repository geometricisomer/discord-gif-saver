import discord
from random import choice

c = discord.Color
em = discord.Embed

def wait():
    """
    Creates Embed with temporary message.

    Returns:
        discord.Embed: Embed with message to wait.
    """
    return em(
        color=c.blue(),
        title=choice(["Hold on...", "Wait...", "Thinking...", "Uhh..."])
    )
