from lib2to3.pgen2 import token
import discord
import os

TOKEN = 'OTkzNjQ3ODY1MjYxOTgxNzM2.GCtdMN.svu29m8SIONLRMH4ovptgGa2e9LJS7je4Qz8iU'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

client.run(TOKEN)