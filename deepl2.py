import time
from selenium import webdriver
import chromedriver_binary
import re
def deepl(text):
    print(text)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    text=text.replace(".\r\n","あ")
    text=text.replace("\r\n"," ")
    text=text.replace("あ",".\r\n")
    print(text)
    url="https://www.deepl.com/ja/translator#en/ja/"+text
    driver =webdriver.Chrome(options=options)
    driver.get(url)
    selector="#target-dummydiv"
    while 1:
        Outputtext =  driver.find_element_by_css_selector(selector).get_attribute("innerHTML")
        if Outputtext != "\r\n" :
            break
        time.sleep(1)
    Outputtext =  driver.find_element_by_css_selector(selector).get_attribute("innerHTML")
    driver.quit
    Outputtext=Outputtext.rstrip("\r\n")
    return Outputtext

