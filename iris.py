#-*- coding:utf-8 -*-


import discord

import datetime
import bs4
import requests



headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}








#디스코드 
#===================================================
client= discord.Client()

#시작
@client.event
async def on_ready():
 print(f'{bot.user}에 로그인하였습니다!')

#--------------------------
#작동중
@client.event
async def on_message(message):
 s = message.content.split()
 
 if s[0] == 'Ping':
  await message.channel.send('pong')






client.run('NzUyODY0MTM5NzY4MjMzOTk0.X1d1Xg.evfkyZxrzAY9r_vgKmuWBrp4jwo')




 #if s[0]=='일정추가' and len(s) == 6":






