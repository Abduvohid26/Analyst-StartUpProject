from bs4 import BeautifulSoup
import requests
import mechanicalsoup
from selenium import webdriver
# browser = mechanicalsoup.Browser()

# url = "https://uzum.uz/uz/"
# page = browser.get(url)
# print(page)

dr = webdriver.Chrome()
dr.get("https://uzum.uz/")
bs = BeautifulSoup(dr.page_source,"html.parser")

res = bs.find_all('a', class_="subtitle-item")
# title = bs.select_one('div.subtitle')
# print(bs.prettify())
button_title = bs.find('button', class_="ui-component ui-button add-to-cart tertiary-outlined small fill")['title']

print(button_title)
