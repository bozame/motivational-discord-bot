from lib2to3.pgen2 import token
from random import random
from urllib import response
import discord
import os

TOKEN = 'OTkzNjQ3ODY1MjYxOTgxNzM2.GB84Vw.ln9nxcFy3dvwndH2hOxY_am0s2n4A9_uoFBYRk'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message}({channel})')

    if message.author == client.user:
        return
    if message.channel.name == 'get-motivated':    
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
    elif user_message.lower() == '!random':
        response = "phrase"
        await message.channel.send(response)
        return

client.run(TOKEN)