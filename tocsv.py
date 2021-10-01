import csv
import pandas as pd
import json

data = None
with open('tfidf.json', encoding="utf-8") as f:
    data = json.load(f)

column = []

for item in data:
    column.append(item['local'])

table = []

for i in range(100):
    row = []
    for item in data:
        row.append(item['top'][i])
    table.append(row)
df = pd.DataFrame(table, columns=column)
df.to_csv("local.corona.csv", encoding = "shift-jis", index = False)