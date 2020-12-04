#-*- coding:utf-8 -*-


import discord

client= discord.Client()






#디스코드 
#===================================================
#시작
@client.event
async def on_ready():
 print(f'{bot.user}에 로그인하였습니다!')

#--------------------------
#작동중
@client.event
async def on_message(message):
 s = message.content.split()
 
 if s[0] == 'ping':
  await message.channel.send('pong')


client.run('NzUyODY0MTM5NzY4MjMzOTk0.X1d1Xg.evfkyZxrzAY9r_vgKmuWBrp4jwo')

 #if s[0]=='일정추가' and len(s) == 6":






