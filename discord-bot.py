import random
import discord
import os

TOKEN = "" #add your own token here

client = discord.Client()

phrases = ['you can do it!',
'keep going, i believe in you!',
"You learn more from failure than from success. Don't let it stop you. Failure builds character.",
"Don’t let yesterday take up too much of today.",
"Setting goals is the first step in turning the invisible into the visible.",
"Well done is better than well said.",
"If you can dream it, you can do it.",
"Aim for the moon. If you miss, you may hit a star.",
"The past cannot be changed. The future is yet in your power.",
"It always seems impossible until it's done."
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
    if user_message.lower() == 'hello':
        await message.channel.send(f'Hello {username}!')
        return
    elif user_message.lower() == '!random':
        await message.channel.send(random.choice(phrases))
        return

client.run(TOKEN)
