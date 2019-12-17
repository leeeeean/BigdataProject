import json
import pandas as pd

def json_from_file():
    city_uid = []
    js_data = []
    # with open('BigdataPrac/pipe/last_data.json') as json_file:
    with open('./last_data.json') as json_file:
        js = json.load(json_file)
        js_data = js["data"]

    for d in js_data:
        city_uid.append(d["uid"])
    
    # print(city_uid)

    # file = open("./uid.txt", "w", encoding="utf-8")
    # file.write(','.join(map(str,city_uid)))
    # file.close()
    return list(map(str,city_uid))



def readFiles(loc, name):
    with open(loc + name, mode="rt", encoding='utf-8') as f:
        st = f.readline()
        jsonData = json.loads(st)

    return jsonData


def makeFrame(jsonData, idxs, name):
    di = dict()
    di["idx"]  = list()
    di["aqi"] = list()
    di["geo"] = list()
    di["name"]= list()
    di["h"] = list()
    di["pm10"]= list()
    di["pm25"]= list()
    di["w"]= list()
    di["wd"]= list()
    di["wg"]= list()
    di["time"]= list()

    for i in range(1,len(idxs)):
        di["idx"].append(idxs[i])
        di["aqi"].append(jsonData[idxs[i]]["data"]["aqi"])
        di["geo"].append(jsonData[idxs[i]]["data"]["city"]["geo"])
        di["name"].append(jsonData[idxs[i]]["data"]["city"]["name"])
        di["h"].append(jsonData[idxs[i]]["data"]["iaqi"]["h"]["v"])
        di["pm10"].append(jsonData[idxs[i]]["data"]["iaqi"]["pm10"]["v"])
        di["pm25"].append(jsonData[idxs[i]]["data"]["iaqi"]["pm25"]["v"])
        di["w"].append(jsonData[idxs[i]]["data"]["iaqi"]["w"]["v"])
        di["wd"].append(jsonData[idxs[i]]["data"]["iaqi"]["wd"]["v"])
        di["wg"].append(jsonData[idxs[i]]["data"]["iaqi"]["wg"]["v"])
        di["time"].append(name[:12])
    df = pd.DataFrame(di)
    return


idxs = json_from_file()
jsonData = readFiles("./","201912080320_dict.txt")  
makeFrame(jsonData, idxs, "201912080320_dict.txt")