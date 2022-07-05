from lib2to3.pgen2 import token
import random
from urllib import response
import discord
import os

TOKEN = 'OTkzNjQ3ODY1MjYxOTgxNzM2.GTmQx0.WErc0u-GCigWuoW82TZO0gd1HLu_l5Gk-54yNo'

client = discord.Client()

phrases = ['you can do it!',
'keep going, i believe in you!',
"You learn more from failure than from success. Don't let it stop you. Failure builds character.",
"Don’t let yesterday take up too much of today.",
"Setting goals is the first step in turning the invisible into the visible.",
"Well done is better than well said."
]

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
            await message.channel.send(random.choice(phrases))
            return

client.run(TOKEN)