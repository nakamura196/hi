import urllib.request
import bs4
import csv
from time import sleep
import pandas as pd
import json
import urllib.request
import os
from PIL import Image
import hashlib

result = {}

with open('data/data_all.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # ヘッダーを読み飛ばしたい時

    for row in reader:

       title1 = row[0]
       id1 = row[1]

       title2 = row[2]
       id2 = row[3]

       no = row[4]
       desc = row[5]

       manifest = "https://nakamura196.github.io/hi/data/" + \
           str(id1)+"/"+str(id2)+"/"+str(no).zfill(4) + ".json"

       title = title1+"・"+title2+"・"+no

       with open("data/template.html") as inf:
           txt = inf.read()
           soup = bs4.BeautifulSoup(txt, "lxml")
           
       soup.find(id="head").string = title
       # soup.find(id="image")["data-uri"] = manifest
       soup.find(id="image")["src"] = "https://universalviewer.io/examples/uv/uv.html#?manifest="+manifest

       dl = soup.new_tag("dl", attrs={"class": "row"})
       soup.find(id="metadata").append(dl)

       dt = soup.new_tag("dt", attrs={"class": "col-sm-3"})
       dl.append(dt)
       dt.string = str("Description")

       dd = soup.new_tag("dd", attrs={"class": "col-sm-9"})
       dl.append(dd)
       dd.string = str(desc)

       html = str(soup)
       html = html.replace("<html><body><p>", "")
       html = html.replace("</body></html>", "")
       html = html.replace("</p>", "")
       

       with open("../docs/item/"+hashlib.md5(manifest.encode("utf-8")).hexdigest()+".html", "w") as outf:
            outf.write(html)

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



print(count)
