import json
import requests
import os
import pickle
from datetime import datetime 


# 실시간  데이터 가져오는 부분 (44.346929,113.709897    28.718891,141.241635) 사이의 나라 혹은 미세먼지 데이터

# 42.500699, 115.546337
# 30.928631, 135.634177 or 30.956555, 134.380722
def json_from_api():
    r = requests.get("https://api.waqi.info/map/bounds/?latlng=40.200699,117.546337,30.956555,133.380722&token=70d8efad38844b4d5582432b51abd6e1bf419a20").json()
    return r
    
def json_from_file():
    city_uid = []
    js_data = []
    with open('BigdataPrac/project/last_data.json') as json_file:
        js = json.load(json_file)
        js_data = js["data"]

    for d in js_data:
        city_uid.append(d["uid"])
    # print(city_uid)
    print("success! read json data")
    return city_uid

def get_city_data(uid_data):
    # data = []
    dict_data = dict()
    for uid in uid_data:
        # 현재 시간의 데이터
        r = requests.post("https://api.waqi.info/feed/@{}/?token=70d8efad38844b4d5582432b51abd6e1bf419a20".format(uid)).json()
        # 과거및 미래의 데이터
        # r = requests.post("https://api.waqi.info/api/feed/@{}/aqi.json".format(uid)).json()
        # data.append(r)
        dict_data[uid] = r
        print(uid)

    # write_list(data)
    write_dict(dict_data)

def write_dict(data):
    name = "{:%Y%m%d%H%M}".format(datetime.now())

    file = open("BigdataPrac/project/res/{}_dict.txt".format(name), "w", encoding="utf-8")
    # pickle.dump(data, file)
    json.dump(data, file, ensure_ascii=False)
    file.close()
    print("good!", name)

def read_dict(name):
    file=open(name,"r") 
    content=pickle.load(file) 
    print(content )
    file.close()

def delete_data():
    file = './upload/test.txt'

    if os.path.isfile(file):
        os.remove(file)

    return 'okay'

print("=====start=====")
data = json_from_file()
get_city_data(data)
print("=====end=====")


# read_dict("20191204075340_dict.txt")
