import deepl2
import discord
import asyncio
import time
from selenium import webdriver
import chromedriver_binary
from xml.sax.saxutils import unescape
TOKEN = 'ODY5ODQwMzA3OTM0NjA5NDY4.YQED6g.Itpfh-oSeP989MH9UiaFLA6hSzc'
client = discord.Client()
@client.event
async def on_message(message):
    author=message.author
    dm=await author.create_dm()
    text=message.content
    if message.channel==dm:
        honyaku = deepl2.deepl(text)
        await message.channel.send(honyaku)
client.run(TOKEN)