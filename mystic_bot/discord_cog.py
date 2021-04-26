import asyncio
import discord
#import sqlite3
import os
import random
#from datetime import datetime
#from pomobot.timer import Timer, TimerStatus
from mystic_bot.timer import Timer, TimerStat
from dotenv import load_dotenv
from discord.ext import commands
from discord import Embed

green = 0x33c633
red = 0xc33333

class DiscordCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.timer = Timer(10)

    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as {}'.format(self.bot.user))

    @commands.command()
    async def start(self, ctx):
        if self.timer.get_status() == TimerStat.RUNNING:
            await self.show_message(ctx, "MYSTIC Bot is already Online!!! ^_^ ^_^", green)
            return    
        title="MYSTIC bot is Online:)"
        await self.show_message(ctx, title, green)
        self.timer.start()
        while self.timer.get_status() == TimerStat.RUNNING:
            await asyncio.sleep(1)
            self.timer.tick()
        if self.timer.get_status() == TimerStat.EXPIRED:
            await self.show_message(ctx, "MYSTIC is going offline :( ", red)
    
    async def show_message(self, ctx, title, color):
        msg = Embed(title=title, color=color)
        await ctx.send(embed=msg)

    async def show_msg(self, ctx, title, description, color):
        msg = Embed(title=title, description=description, color=color)
        await ctx.send(embed=msg)

    @commands.command()
    async def time(self, ctx):
        title = "Current status"
        status = title + " is " + str(self.timer.get_status())
        tim = "Current time"
        tim_n = tim + " is " + str(self.timer.get_ticks())
        await self.show_msg(ctx, title, status, green)
        await self.show_msg(ctx, tim, tim_n, green)
        self.timer.stop()

    @commands.command()
    async def help(self, ctx):
        help_commands = dict()
        for command in commands.commands:
            help_commands[command.name] = command.help
        title="MYSTIC bot official"
        description="Bot commands are : {}".format(help_commands)
        await self.show_msg(ctx, title, description, green)

    @commands.command()
    async def lineups(self, ctx):
        aplha = "MYSTIC ALPHA"
        lineup = "MYT々Ghozt, MYT々NytKing, MYT々dibi, GR AGON"
        await self.show_msg(ctx, alpha, lineup, 0xc66335)

    @commands.command()
    async def aboutme(self, ctx):
        about = "This bot is fully owned by Mystic Esports Official. More deatils will be Updated soon..!"
        await self.show_msg(ctx, "About Me", about, 0xc66335)

    @commands.command()
    async def stop(self, ctx):
        if self.timer.get_status() != TimerStat.RUNNING:
            await self.show_message(ctx, "MYSTIC Bot is already Offline!!! :( ", red)
            return
        diag = "MYSTIC bot is Offline now :( "
        await show_msg(ctx, diag, red)
        self.timer.stop()

#    commands.run(os.getenv('TOKEN'))