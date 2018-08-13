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
    await bot.send_message(discord.Object('457633597764141076'), "I am online now, version 1.0.5 Jerome will WIN and Sus will LOSE.\n\n<http://www.multitwitch.tv/sus333/actuallyimjerome>")

@bot.command(pass_context=True)
async def shutdown(ctx):
    if ctx.message.author.id == '220383768966463489':
        await bot.send_message(ctx.message.channel, 'Bye bye :wave:')
        await bot.logout()
    else:
        await bot.send_message(channel, embed=discord.Embed(description="You have no permission to shut down the bot.", color=0xbc0012))

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
            await bot.send_message(ctx.message.channel, embed=discord.Embed(description="<@%s>, you're already in **Team Jerome.**" % ctx.message.author.id, color=0xbc0012))
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

    timeleft = datetime.datetime(2018, 8, 13) + datetime.timedelta(hours=12, minutes=30) - datetime.datetime.utcnow()
    embed = discord.Embed(color=0x1abc9c)
    embed.set_author(name="Time left until Sus333 vs Jerome SMG2 speedrun!")
    embed.add_field(name="Countdown to August 13, 2018", value="NOW!!!!!!!!!!!\n\n<http://www.multitwitch.tv/sus333/actuallyimjerome>")
    await bot.send_message(ctx.message.channel, embed=embed)

@bot.command(pass_context=True)
async def jerome(ctx):
    await bot.send_message(ctx.message.channel, "<https://www.twitch.tv/actuallyimjerome>")

@bot.command(pass_context=True)
async def sus(ctx):
    await bot.send_message(ctx.message.channel, "<https://www.twitch.tv/sus333>")

@bot.command(pass_context=True)
async def help(ctx):
    helpmsg = discord.Embed(description="Usage: `.<command>`", color=0x1abc9c)
    helpmsg.set_author(name="JEROME AND SUS RACE BOT", icon_url=bot.user.avatar_url)
    helpmsg.add_field(name="Team Role Commands", value="`teamjerome` `teamsus`", inline=False)
    helpmsg.add_field(name="Useful Commands", value="`countdown`", inline=False)
    helpmsg.add_field(name="Livestream Links", value="`jerome` `sus`")
    helpmsg.set_footer(text="© 2018 Xeno | Version 1.0.5")
    await bot.send_message(ctx.message.channel, embed=helpmsg)

bot.run(config.token)
