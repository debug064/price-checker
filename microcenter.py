import datetime
import os
import sys
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchWindowException

from bs4 import BeautifulSoup

# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
# from PyQt5.QtWidgets import QApplication
# from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView

urls = {
    "https://www.microcenter.com/product/514127/latitude-e5285-123-2-in-1-laptop-computer-refurbished---black":"299.99"
    ,"https://www.microcenter.com/product/512433/latitude-5285-123-2-in-1-laptop-computer-refurbished---black":"629.99"
}


def main(args):
    options = Options()
    options.add_argument("--headless") # Runs Chrome in headless mode.
    #options.add_argument('--no-sandbox') # Bypass OS security model
    options.add_argument('--disable-gpu')  # applicable to windows os only
    # options.add_argument('start-maximized') # 
    # options.add_argument('disable-infobars')
    # options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(executable_path="chromedriver")
    try:
        print(datetime.datetime.now())
        for url, price in urls.items():
            print(url, price)
            driver.get(url)
            content = driver.page_source
            for val in parseprice(content):
                if price != val:
                    print("Price changed to:", val)
    except NoSuchWindowException as ex:
        print(ex)
    finally:
        driver.quit()


def parseprice(content):
    res = []
    soup = BeautifulSoup(content, features="html.parser")
    #for span in soup.findAll('div', attrs={'id':'options-pricing'}).findAll('span'): 
    #for div in soup.findAll('div', attrs={'id':'options-pricing'}):
        #for span in div.findChildren("span" , recursive=False):
    for span in soup.findAll('span', attrs={'id':'pricing'}):
        if __name__ == '__main__':
            print(span['content'])
            print(span.get_text()[1:])
        res.append(span['content'])
        res.append(span.get_text()[1:])
    return res


if __name__ == '__main__':
    main(sys.argv[1:])
