import csv
import pandas as pd
import json

data = None
with open('tfidf3.json', encoding="utf-8") as f:
    data = json.load(f)

localmap = ["北海道", "東北", "北関東・甲信", "南関東", "北陸", "東海", "近畿", "中国", "四国", "九州沖縄"]

for i in range(len(data)):
    print(localmap[i])
    local = data[i]
    cnt = 1
    for i in local['top']:
        if(i == 'ファイバ'):
            print("ファイバ " + str(cnt))
        if(i == 'ファイバー'):
            print("ファイバー " + str(cnt))
        if(i == '光ファイバー'):
            print("光ファイバー " + str(cnt))
        if(i == '光ファイバ'):
            print('光ファイバ ' + str(cnt))
        if(i == '光'):
            print("光 " + str(cnt))
          
        cnt += 1
    print("")