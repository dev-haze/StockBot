import discord
from discord.ext import commands, tasks

@bot.event
async def on_ready():
 print('------------')
 print('접속성공. 봇 이리스, 대기중입니다.')
 print(bot.user.name)
 print(bot.user.id)
 print('------------')


@bot.command()
async def ping(ctx):
 await ctx.send('pong')

@bot.command(



