import glob
import csv

files = glob.glob('../docs/**/*.json', recursive=True)

f = open('data/manifest_list.csv', 'w')

writer = csv.writer(f, lineterminator='\n')
writer.writerow(["manifest_uri"])

for file in files:
    if "collection.json" not in file:
        url = file.replace("../docs", "https://nakamura196.github.io/hi")
        writer.writerow([url])

f.close()
