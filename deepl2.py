import time
from selenium import webdriver
import chromedriver_binary
from xml.sax.saxutils import unescape
def deepl(text):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    text = ' '.join(text.splitlines())
    url="https://www.deepl.com/ja/translator"
    driver =webdriver.Chrome(options=options)
    driver.get(url)
    insec="#dl_translator > div.lmt__text > div.lmt__sides_container > div.lmt__side_container.lmt__side_container--source > div.lmt__textarea_container > div.lmt__inner_textarea_container > textarea"
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
        time.sleep(1)
        i+=1
    driver.quit
    Outputtext=Outputtext.rstrip("\r\n")
    Outputtext=unescape(Outputtext)
    return Outputtext

