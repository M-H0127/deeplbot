import time
from selenium import webdriver
import chromedriver_binary
import re
def deepl(text):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    text=text.replace(".\r","あ")
    text=text.replace(".\n","あ")
    text=text.replace("\n"," ")
    text=text.replace("\r"," ")
    text=text.replace("あ",".\r")
    url="https://www.deepl.com/ja/translator#en/ja/"+text
    driver =webdriver.Chrome(options=options)
    driver.get(url)
    selector="#target-dummydiv"
    while 1:
        Outputtext =  driver.find_element_by_css_selector(selector).get_attribute("innerHTML")
        if Outputtext != "\r\n" :
            break
        time.sleep(1)
    driver.quit
    return Outputtext

