import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from datetime import datetime 


# 이미지 저장
date = 201912071500
# date = 201912010000

while (date != 201912071502) :
# while (date != 201912021600) :
    if str(date)[-2:] == '60':
        date += 40
        if str(date)[8:-2] == '24':
            date += 10000
            date -= 2400
    # 시간 변동 때문인지 6:00 부터 6:08 까지는 데이터가 없다
    if int(str(date)[9:]) >= 600 and int(str(date)[9:]) <= 608:
        date += 2
        continue
    img_url = "http://www.weather.go.kr/repositary/image/sat/gk2a/KO/gk2a_ami_le1b_ir105_ko020lc_{0}.thn.png"
    img_name = str(date)+".png"
#     urllib.request.urlretrieve(img_url.format(date), 'BigdataPrac/project/img/' + img_name)
    urllib.request.urlretrieve(img_url.format(date), './im2/' + img_name)
    date += 2

