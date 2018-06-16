import discord
import logging
import asyncio
import time
import aiohttp
import datetime

import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix=".")

message = discord.Message

bot.remove_command('help')

@bot.event
async def on_ready():
    print("Bot connected")
    print("Sus is a gay loser")
    print(discord.__version__)

@bot.command(pass_context=True)
async def teamjerome(ctx):
    jerome = discord.utils.get(ctx.message.server.roles, name="Team Jerome")
    sus = discord.utils.get(ctx.message.server.roles, name="Team Sus")
    if sus in ctx.message.author.roles:
        await bot.remove_roles(ctx.message.author, sus)
        await bot.add_roles(ctx.message.author, jerome)
        await bot.send_message(ctx.message.channel, embed=discord.Embed(description="<@%s>, you have switched to **Team Jerome!**" % ctx.message.author.id, color=0x3498db))
    else:
        if jerome in ctx.message.author.roles:
            await bot.send_message(ctx.mess age.channel, embed=discord.Embed(description="<@%s>, you're already in **Team Jerome.**" % ctx.message.author.id, color=0xbc0012))
        else:
            await bot.add_roles(ctx.message.author, jerome)
            await bot.send_message(ctx.message.channel, embed=discord.Embed(description="<@%s>, you have joined **Team Jerome!**" % ctx.message.author.id, color=0x3498db))

@bot.command(pass_context=True)
async def teamsus(ctx):
    jerome = discord.utils.get(ctx.message.server.roles, name="Team Jerome")
    sus = discord.utils.get(ctx.message.server.roles, name="Team Sus")
    if jerome in ctx.message.author.roles:
        await bot.remove_roles(ctx.message.author, jerome)
        await bot.add_roles(ctx.message.author, sus)
        await bot.send_message(ctx.message.channel, embed=discord.Embed(description="<@%s>, you have switched to **Team Sus!**" % ctx.message.author.id, color=0xe74c3c))
    else:
        if sus in ctx.message.author.roles:
            await bot.send_message(ctx.message.channel, embed=discord.Embed(description="<@%s>, you're already in **Team Sus.**" % ctx.message.author.id, color=0xbc0012))
        else:
            await bot.add_roles(ctx.message.author, sus)
            await bot.send_message(ctx.message.channel, embed=discord.Embed(description="<@%s>, you have joined **Team Sus!**" % ctx.message.author.id, color=0xe74c3c))

@bot.command(pass_context=True)
async def countdown(ctx):
    def strfdelta(tdelta, fmt):
        d = {"days": tdelta.days}
        d["hours"], rem = divmod(tdelta.seconds, 3600)
        d["minutes"], d["seconds"] = divmod(rem, 60)
        return fmt.format(**d)

    timeleft = datetime.datetime(2018, 7, 7) + datetime.timedelta(hours=7) - datetime.datetime.utcnow()
    embed = discord.Embed(color=0x1abc9c)
    embed.set_author(name="Time left until Sus33 vs Jerome SMG2 speedrun!")
    embed.add_field(name="Countdown to July 7, 2018", value=(strfdelta(timeleft, "**{days}** days, **{hours}** hours, **{minutes}** minutes, and **{seconds}** seconds")))
    await bot.send_message(ctx.message.channel, embed=embed)

@bot.command(pass_context=True)
async def help(ctx):
    helpmsg = discord.Embed(title="SMG2", icon_url="%s" % bot.user.avatar_url, description="Usage: `.<command>`", color=0x1abc9c)
    helpmsg.add_field(name="Team Role Commands", value="`teamjerome` `teamsus`", inline=False)
    helpmsg.add_field(name="Useful Commands", value="`countdown`", inline=False)
    helpmsg.set_footer(text="© 2018 Xeno | Version 1.0")
    await bot.send_message(ctx.message.channel, embed=helpmsg)

bot.run(config.token)
