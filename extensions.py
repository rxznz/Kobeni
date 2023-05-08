import discord
import os
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

bot.load_extension('commands')
bot.load_extension('view')
bot.load_extension('read')
bot.load_extension('id')
bot.load_extension('run')
