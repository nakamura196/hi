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


temp = {
    "@context": "http://iiif.io/api/presentation/2/context.json",
    "@id": "https://nakamura196.github.io/iiif/data/collection/collection.json",
    "@type": "sc:Collection"
}

collection = temp.copy()
collection["@id"] = "https://nakamura196.github.io/hi/data/collection.json"
collections = []
collection["collections"] = collections


for id1 in result:

    obj1 = result[id1]["children"]
    title1 = result[id1]["title"]

    collection1 = temp.copy()
    collection1["label"] = title1
    collection1["@id"] = "https://nakamura196.github.io/hi/data/"+id1+"/collection.json"
    collections.append(collection1)
    collections1 = []
    collection1["collections"] = collections1


    for id2 in obj1:
        obj2 = obj1[id2]["children"]
        title2 = obj1[id2]["title"]

        collection2 = temp.copy()
        collection2["label"] = title1+"・"+title2
        collection2["@id"] = "https://nakamura196.github.io/hi/data/"+id1+"/"+id2+"/collection.json"
        collections1.append(collection2)

        manifests = []
        collection2["manifests"] = manifests

        for no in obj2:
            obj3 = obj2[no]

            dir1 = "../docs/data/"+id1+"/"+id2

            file = dir1+"/" + str(no).zfill(4) + ".json"

            manifest = "https://nakamura196.github.io/hi/"+file.replace("../docs/", "")

            m = temp.copy()
            m["@id"] = manifest
            m["@type"] = "sc:Manifest"
            m["label"] = title1+"・"+title2+"・"+no
            manifests.append(m)

            '''

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

            # f2 = open(file, 'w')
            # json.dump(obj, f2, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))


            '''


f2 = open("../docs/data/collection.json", 'w')
json.dump(collection, f2, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
