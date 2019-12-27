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
                "title" : title1,
                "children" : {}
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
                "desc" : desc,
                "images" : []
            }

        tmp = tmp[no]

        img = row[6]

        tmp["images"].append(img)

data = []
data.append(["ID", "Title", "Description"])

for id1 in result:
    obj1 = result[id1]["children"]
    title1 = result[id1]["title"]

    for id2 in obj1:
        print("**"+id2)
        obj2 = obj1[id2]["children"]
        title2 = obj1[id2]["title"]

        for no in obj2:
            obj3 = obj2[no]

            dir1 = "../docs/data/"+id1+"/"+id2

            file = dir1+"/" + str(no).zfill(4) + ".json"

            id = id1+"-"+id2+"-"+str(no).zfill(4)
            title = title1+"・"+title2+"・"+no
            desc = obj3["desc"]

            row = [id, title, desc]
            data.append(row)

df = pd.DataFrame(data)

df.to_excel("data2/metadata.xlsx", index=False, header=False)

'''
f = open('data/temp.json', 'r')
json_dict = json.load(f)

count = 0

for id1 in result:
    print("*"+id1)

    obj1 = result[id1]["children"]
    title1 = result[id1]["title"]

    for id2 in obj1:
        print("**"+id2)
        obj2 = obj1[id2]["children"]
        title2 = obj1[id2]["title"]

        for no in obj2:
            obj3 = obj2[no]

            dir1 = "../docs/data/"+id1+"/"+id2
            os.makedirs(dir1, exist_ok=True)

            file = dir1+"/" + str(no).zfill(4) + ".json"

            count += 1

            if os.path.exists(file):
                continue

            # obj = json_dict.copy()

            obj = {
                "@context": "http://iiif.io/api/presentation/2/context.json",
                "@type": "sc:Manifest",
                "license": "http://creativecommons.org/licenses/by-nc-sa/4.0/",
                "attribution": "Historiographical Institute The University of Tokyo 東京大学史料編纂所",
                "logo": "http://www.hi.u-tokyo.ac.jp/favicon.ico",
                "within": "http://www.hi.u-tokyo.ac.jp/publication/dip/index.html",
                "sequences": [
                    {
                        "@type": "sc:Sequence",
                        "label": "Current Page Order",
                        "viewingHint": "non-paged",
                        "canvases": []
                    }
                ],
                "viewingDirection": "right-to-left"
            }

            obj["label"] = title1+"・"+title2+"・"+no
            obj["description"] = obj3["desc"]
            obj["@id"] = "https://nakamura196.github.io/hi/"+file.replace("../docs/", "")

            obj["sequences"][0]["@id"] = obj["@id"]+"/sequence/normal"
            
            canvases = obj["sequences"][0]["canvases"]

            width = -1
            height = -1


            for i in range(len(obj3["images"])):
                img_url = obj3["images"][i]
                tmp = {
                  "@type": "sc:Canvas",
                  "thumbnail": {},
                  "images": [
                    {
                      "@type": "oa:Annotation",
                      "motivation": "sc:painting",
                      "resource": {
                        "@type": "dctypes:Image",
                        "format": "image/jpeg",
                      }
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

print(count)

'''


