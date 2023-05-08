import discord
from discord.ext import commands
from extensions import bot
import os

@bot.event 
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    print('Loaded commands:')
    for command in bot.commands:
        print(command.name)
