"""
       D i s c o r d  C o u n t d o w n

             Made by @znotdeev

"""

# Imports

import discord, datetime
from discord.ext import commands as cmds
from discord.ext import tasks

# Configuration

conf = {
    "token": "TOKEN_BOT",
    "prefix": "!",
    "channel": 9999999999999999999,
    "objective": 1686402822,
}

# Functions

def time_rest(arg):
    now = datetime.datetime.now()
    arg = datetime.datetime.fromtimestamp(arg)

    if arg < now:
        return "Right now"

    rest = arg - now
    days = rest.days
    seconds = rest.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60

    output = ""
    if days > 0:
        output += f"{days}d"
    if hours > 0:
        output += f", {hours}h"
    if minutes > 0:
        output += f", {minutes}m"
    if remaining_seconds > 0:
        if days > 0 and hours > 0 and minutes > 0:
            output += f", {remaining_seconds}s"
        else:
            output += f"{remaining_seconds}s"

    return output

# Variables

bot = cmds.Bot(command_prefix=conf["prefix"], intents=discord.Intents.all())

# Bot Events

@bot.event
async def on_ready():
    print('Bot ready.')
    update_channel_name.start()

@tasks.loop(seconds=600) # 10 minutes is the minimun because discord likes to ratelimit.
async def update_channel_name():
    channel = bot.get_channel(conf["channel"])
    await channel.edit(name=f"↪ {time_rest(conf['objective'])}")

# Bot Commands

@bot.command(name="countdown")
async def countdown(ctx):
    return await ctx.send(time_rest(conf["objective"]))

# Init bot

bot.run(conf["token"])
