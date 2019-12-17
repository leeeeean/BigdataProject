#!/usr/bin/env python
# coding: utf-8


import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
# 혹은 options.add_argument("--disable-gpu")

url ="http://www.weather.go.kr/weather/main.jsp"

driver = webdriver.Chrome('./chromedriver', options=options)
driver.get(url)

sleep(2)

# 화면 오픈
driver.find_element_by_id('top-menu2').click()
driver.find_element_by_id("menu2-2-1").click()
driver.find_element_by_id("data1").click()

# 이미지 가져오기
cnt = BeautifulSoup(driver.page_source, 'html.parser')
li = cnt.find("ul",{"class":"image-player-slide-images"})
img = li.find("img")
src = img.get("src")

print(src)
# 이미지 저장
img_url = "http://www.weather.go.kr"+src
img_name = src[src.find('2019'):]
if int(str(img_name)[9:12]) < 600 or int(str(img_name)[9:12]) > 608:
    urllib.request.urlretrieve(img_url, 'BigdataPrac/project/img/' + img_name)
# urllib.request.urlretrieve(img_url, './img/' + img_name)
driver.quit()

