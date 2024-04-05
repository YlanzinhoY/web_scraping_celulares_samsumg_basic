from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
from util import regex_money

web = webdriver.Chrome()

web.get("https://www.samsung.com/br/smartphones/all-smartphones/")
html = web.page_source
soup = BeautifulSoup(html, "html.parser")
time.sleep(4)


title = []
price = []
time.sleep(1)
title_cell = soup.find_all("p", {"class": "pd03-product-card__product-name-text"})
price_cell = soup.find_all("p", {"class": "pd03-product-card__price-main"})


for i,j in zip(title_cell, price_cell):
    title.append(i.text)
    
    price_regex = regex_money.Extract_money_value(j.get_text(strip=True))
    price.append(price_regex)


with open("celulares_preco.csv", "w+", encoding="utf-8") as f:
    for i, j in zip(title, price):
        f.write(f"{i}, R${j}\n")

web.quit()

