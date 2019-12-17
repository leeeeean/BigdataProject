import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from datetime import datetime 


date = int("{:%Y%m%d%H%M}".format(datetime.utcnow()))
print("=====start : {}=====".format(date))
# 20분 전부터 10분간의 데이터를 가져옴
if date%2 != 0:
    date -= 1
date -= 18
if int(str(date)[8:10]) == 99:
    date -= 7600
if int(str(date)[-2:]) >= 60:
    date -= 40
for _ in range(5) :
    if int(str(date)[-2:]) == 60:
        date -= 60 # 1760 일떄 ERR >> 1800 으로 바꿔준다
        date += 100
    if int(str(date)[-4:]) == 2400: # 2400 일떄 err >> 0000 으로 바꿔준다
        date -= 2400
        date += 10000
    # 시간 변동 때문인지 6:00 부터 6:08 까지는 데이터가 없다
    if int(str(date)[8:]) >= 600 and int(str(date)[8:]) <= 608:
        date += 2
        continue
    img_url = "http://www.weather.go.kr/repositary/image/sat/gk2a/KO/gk2a_ami_le1b_ir105_ko020lc_{0}.thn.png"
    img_name = str(date)+".png"
    try:
        urllib.request.urlretrieve(img_url.format(date), 'BigdataPrac/project2/im2/' + img_name)
        # urllib.request.urlretrieve(img_url.format(date), './im2/' + img_name)
    except urllib.error.HTTPError:
        print("hppt error!!!!!!!!", img_url.format(date))
    date += 2

print("=====end : {}=====".format(date))