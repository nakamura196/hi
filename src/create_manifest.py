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

with open('data/data.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # ヘッダーを読み飛ばしたい時

    for row in reader:

        print(row)

        title1 = row[0]

        if title1 not in result:
            result[title1] = {}

        tmp = result[title1]

        title2 = row[1]

        if title2 not in tmp:
            tmp[title2] = {}

        tmp = tmp[title2]

        no = row[2]
        desc = row[3]

        if no not in tmp:
            tmp[no] = {
                "desc" : desc,
                "images" : []
            }

        tmp = tmp[no]

        img = row[4]

        tmp["images"].append(img)


f = open('data/temp.json', 'r')
json_dict = json.load(f)

for title1 in result:

    obj1 = result[title1]

    for title2 in obj1:
        obj2 = obj1[title2]

        for no in obj2:
            obj3 = obj2[no]

            dir1 = "../docs/data/"+title1+"/"+title2
            os.makedirs(dir1, exist_ok=True)

            file = dir1+"/" + str(no).zfill(4) + ".json"

            obj = json_dict.copy()
            obj["label"] = title1+"・"+title2+"・"+no
            obj["description"] = obj3["desc"]
            obj["@id"] = "https://nakamura196.github.io/hi/"+file.replace("../docs/", "")

            canvases = obj["sequences"][0]["canvases"]

            width = -1
            height = -1


            for i in range(len(obj3["images"])):
                img_url = obj3["images"][i]
                tmp = {
                  "@id": "https://uta.u-tokyo.ac.jp/uta/iiif/12358/canvas/p1",
                  "@type": "sc:Canvas",
                  "label": "[1]",
                  "thumbnail": {
                    "@id": "https://uta.u-tokyo.ac.jp/uta/files/medium/b0860287cd6c5ccdebdd7b0ba0eb4367db17cf89.jpg"
                  },
                  "width": 1631,
                  "height": 1224,
                  "images": [
                    {
                      "@id": "https://uta.u-tokyo.ac.jp/uta/iiif/12358/annotation/p0001-image",
                      "@type": "oa:Annotation",
                      "motivation": "sc:painting",
                      "resource": {
                        "@id": "https://uta.u-tokyo.ac.jp/uta/files/original/b0860287cd6c5ccdebdd7b0ba0eb4367db17cf89.jpg",
                        "@type": "dctypes:Image",
                        "format": "image/jpeg",
                        "width": 1631,
                        "height": 1224
                      },
                      "on": "https://uta.u-tokyo.ac.jp/uta/iiif/12358/canvas/p1"
                    }
                  ]
                }
                tmp["@id"] = obj["@id"]+"/canvas/p"+str(i+1)
                tmp["label"] = "["+str(i+1)+"]"

                tmp["thumbnail"]["@id"] =img_url.replace(".jpg", "_r25.jpg")

                if i == 0:
                    obj["thumbnail"] = tmp["thumbnail"]["@id"]

                    img = Image.open(urllib.request.urlopen(img_url))
                    width, height = img.size

                tmp["images"][0]["resource"]["width"] = width
                tmp["images"][0]["resource"]["height"] = height

                tmp["width"] = width
                tmp["height"] = height

                tmp["images"][0]["@id"] = obj["@id"]+"/annotation/p"+str(i+1)+"-image"

                tmp["images"][0]["resource"]["@id"] = img_url

                tmp["images"][0]["on"] = tmp["@id"]

                canvases.append(tmp)

            f2 = open(file, 'w')
            json.dump(obj, f2, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))


'''
result = []
result.append(["title1", "title2", "no", "desc", "img_url"])

url = 'http://www.hi.u-tokyo.ac.jp/publication/dip/data/series.json'
res = urllib.request.urlopen(url)
# json_loads() でPythonオブジェクトに変換
data = json.loads(res.read())

dd = []

for obj in data:
    title1 = obj["title"]
    id1=obj["id"]

    print("*"+str(id1))

    url1 = 'http://www.hi.u-tokyo.ac.jp/publication/dip/data/'+id1+'.json'

    sleep(1)

    res1 = urllib.request.urlopen(url1)
    # json_loads() でPythonオブジェクトに変換
    data1 = json.loads(res1.read())

    for obj1 in data1:
        title2 = obj1["title"]
        id2 = obj1["id"]

        print("**"+str(id1))

        url2 = 'http://www.hi.u-tokyo.ac.jp/publication/dip/data/'+id1+"-"+id2+'.json'

        sleep(1)

        res2 = urllib.request.urlopen(url2)
        # json_loads() でPythonオブジェクトに変換
        data2 = json.loads(res2.read())

        for obj2 in data2:
            url3 = obj2["url"]
            no = obj2["no"]
            desc = obj2["description"]

            url3 = url3 + "?m=all&n=100&p="

            print("***"+str(no))

            loop_flg = True
            page = 1

            while loop_flg:
                url4 = url3 + str(page)
                print("****"+str(url4))

                page += 1

                sleep(1)

                html4 = urllib.request.urlopen(url4)
                soup4 = BeautifulSoup(html4, "lxml")
                arr = soup4.find_all(class_="thumbnail-image")

                if len(arr) > 0:
                    for a in arr:
                        img_url = a.get("style").split("'")[1].replace("_r25.jpg", ".jpg")

                        if img_url in dd:
                            loop_flg = False
                            break
                        else:
                            dd.append(img_url)

                            row = [title1, title2, no, desc, img_url]
                            result.append(row)

                else:
                    loop_flg = False


print(result)

f = open("data.csv", 'w')

writer = csv.writer(f, lineterminator='\n')

writer.writerows(result)


f.close()
'''
