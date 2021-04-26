import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from mystic_bot.discord_cog import DiscordCog

load_dotenv()

bot = commands.Bot(command_prefix='$', help_command=None)
bot.add_cog(DiscordCog(bot))
bot.run(os.environ['TOKEN'])
