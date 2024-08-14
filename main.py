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
button_prices = [price.text.strip() for price in bs.find_all('span', class_="currency product-card-price slightly medium")]
button_feedback = [feedback.text.strip() for feedback in bs.find_all('span', class_="orders__feedback-amount")]
button_titles = [button['title'] for button in bs.find_all('button', class_="ui-component ui-button add-to-cart tertiary-outlined small fill")]

for title, price, feedback in zip(button_titles, button_prices, button_feedback):
    print(f"Nom: {title}\nNarxi: {price}\nFeedbacks: {feedback}\n")
