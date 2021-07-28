import deepl2
import discord
import asyncio
TOKEN = 'ODY5ODQwMzA3OTM0NjA5NDY4.YQED6g.EpgtAGZpAE_KMO6XEc5VTKzRY9Y'
client = discord.Client()
@client.event
async def on_message(message):
    author=message.author
    dm=await author.create_dm()
    if message.channel==dm:
        if __name__ == '__main__':
            honyaku = deepl2.deepl(message.content)
            await message.channel.send(honyaku)
client.run(TOKEN)