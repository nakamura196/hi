import urllib.request
from bs4 import BeautifulSoup
import csv
from time import sleep
import pandas as pd
import json
import urllib.request

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
