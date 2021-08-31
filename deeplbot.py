import discord
import asyncio
import time
from selenium import webdriver
import chromedriver_binary
from xml.sax.saxutils import unescape
TOKEN = 'ODY5ODQwMzA3OTM0NjA5NDY4.YQED6g.Itpfh-oSeP989MH9UiaFLA6hSzc'

client = discord.Client()
mode=[]
def split(text):
    text.replace(".\r\n","あ")
    text = ' '.join(text.splitlines())
    text.replace("あ",".\r\n")
    return text
def deepl(text,driver):
    text = split(text)
    i=0
    while 1:
        try:
            insec="#dl_translator > div.lmt__text > div.lmt__sides_container > div.lmt__side_container.lmt__side_container--source > div.lmt__textarea_container > div.lmt__inner_textarea_container > textarea"
        except selenium.common.exceptions.NoSuchElementException as e:
            if i<10:
                time.sleep(0.5)
                i+=1
            else:
                outputtext="エラーが発生しました"
                return outputtext
        else:
            break
    driver.find_element_by_css_selector(insec).send_keys(text)
    selector="#dl_translator > div.lmt__text > div.lmt__sides_container > div.lmt__side_container.lmt__side_container--target > div.lmt__textarea_container > div.lmt__inner_textarea_container > textarea"
    i=1
    while 1:
        outputtext =  driver.find_element_by_css_selector(selector).get_attribute("value")
        time.sleep(5)
        if outputtext != "":
            break
        elif i>30:
            outputtext="翻訳不可能な言語です\r\n"
            break
        time.sleep(1)
        i+=1
    outputtext =  driver.find_element_by_css_selector(selector).get_attribute("value")
    outputtext=unescape(outputtext)
    driver.find_element_by_css_selector(insec).clear()
    return outputtext

@client.event
async def on_message(message):
    global mode
    if message.content=="hello" and message.author not in mode:
        mode.append(message.author)
        channel=message.channel
        author=message.author
        dm=await author.create_dm()
        await channel.send("起動中")

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        url="https://www.deepl.com/ja/translator"
        driver =webdriver.Chrome(options=options)
        driver.get(url)
        await asyncio.sleep(0.5)
        m="翻訳文を入力"
        def check(m):
            return m.content!=""
        i=1
        while i:
            await channel.send(m)
            def check(m):
                return m.content!="" and m.author!=client.user
            try:
                msg=await client.wait_for('message',timeout=300,check=check)
            except asyncio.TimeoutError:
                await channel.send("操作が見られなかったため中断します")
                break
            await channel.send("翻訳を開始します")
            async for mes in channel.history(limit=1):
                mes = mes
            text=msg.content
            if msg.channel==dm:
                outputtext = deepl(text,driver)
                await mes.edit(content=outputtext+"\r\n//")
            await channel.send("続けますか？\r\n(続けるならy、終えるならnを入力)")
            def check(m):
                return m.author!=client.user and m.content=="y" or m.content=="n"
            try:
                msg=await client.wait_for('message',timeout=3600,check=check)
            except asyncio.TimeoutError:
                await channel.send("操作が見られなかったため中断します")
                break
            if msg.content=="n":
                i=0
        await channel.send("お疲れさまでした")
        driver.quit()
        mode.remove(author)
client.run(TOKEN)
