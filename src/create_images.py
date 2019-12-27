import urllib.request
from bs4 import BeautifulSoup
import csv
from time import sleep
import pandas as pd
import json
import urllib.request
import os
from PIL import Image

result = {}

with open('data/data_all.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # ヘッダーを読み飛ばしたい時

    for row in reader:

        # print(row)

        title1 = row[0]
        id1 = row[1]

        if id1 not in result:
            # result[title1] = {}
            result[id1] = {
                "title": title1,
                "children": {}
            }

        tmp = result[id1]["children"]

        title2 = row[2]
        id2 = row[3]

        if id2 not in tmp:
            tmp[id2] = {
                "title": title2,
                "children": {}
            }

        tmp = tmp[id2]["children"]

        no = row[4]
        desc = row[5]

        if no not in tmp:
            tmp[no] = {
                "desc": desc,
                "images": []
            }

        tmp = tmp[no]

        img = row[6]

        tmp["images"].append(img)

data = []
data.append(["ID", "Media Url"])

for id1 in result:
    obj1 = result[id1]["children"]
    title1 = result[id1]["title"]

    for id2 in obj1:
        print("**"+id2)
        obj2 = obj1[id2]["children"]
        title2 = obj1[id2]["title"]

        for no in obj2:
            obj3 = obj2[no]

            id = id1+"-"+id2+"-"+str(no).zfill(4)
            
            for i in range(len(obj3["images"])):
                img_url = obj3["images"][i]


                row = [id, img_url]
                data.append(row)

df = pd.DataFrame(data)

writer = pd.ExcelWriter('data2/images.xlsx', options={'strings_to_urls': False})
df.to_excel(writer, index=False, header=False)
writer.close()
