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
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        text = ' '.join(text.splitlines())
        url="https://www.deepl.com/ja/translator"
        driver =webdriver.Chrome(options=options)
        driver.get(url)
        i=0
        while 1:
            try:
                insec="#dl_translator > div.lmt__text > div.lmt__sides_container > div.lmt__side_container.lmt__side_container--source > div.lmt__textarea_container > div.lmt__inner_textarea_container > textarea"
            except selenium.common.exceptions.NoSuchElementException as e:
                if i<10:
                    await asyncio.sleep(0.5)
                    i+=1
                else:
                    Outputtext="エラーが発生しました"
                    await message.channel.send(Outputext)
            else:
                break

        driver.find_element_by_css_selector(insec).send_keys(text)
        selector="#target-dummydiv"
        i=1
        while 1:
            Outputtext =  driver.find_element_by_css_selector(selector).get_attribute("innerHTML")
            if Outputtext != "\r\n" :
                break
            elif i>30:
                Outputtext="翻訳不可能な言語です\r\n"
                break
            await asyncio.sleep(1)
            i+=1
        driver.quit
        Outputtext=Outputtext.rstrip("\r\n")
        honyaku=unescape(Outputtext)
        await message.channel.send(honyaku)
client.run(TOKEN)