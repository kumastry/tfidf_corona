import pickle
import json
import spacy
from collections import defaultdict

def pref2local(prefecture):
    local = ''
    if(prefecture == '北海道'):
        local = '北海道'
    elif(prefecture in ["青森県","岩手県","宮城県","秋田県","山形県","福島県"]):
        local = '東北'
    elif(prefecture in ["埼玉県","千葉県","東京都","神奈川県"]):
        local = '南関東'
    elif(prefecture in ["茨城県","栃木県","群馬県","山梨県","長野県"]):
        local = "北関東・甲信"
    elif(prefecture in ["新潟県","富山県","石川県","福井県"]):
        local = "北陸"
    elif(prefecture in ["岐阜県","静岡県","愛知県","三重県"]):
        local = "東海"
    elif(prefecture in ["滋賀県","京都府","大阪府","兵庫県","奈良県","和歌山県"]):
        local = "近畿"
    elif(prefecture in ["鳥取県","島根県","岡山県","広島県","山口県"]):
        local =  "中国"
    elif(prefecture in ["徳島県","香川県","愛媛県","高知県"]):
        local = "四国"
    else:
        local = "九州"
    return local


nlp = spacy.load("ja_ginza")
documents = []
sentents_word = []

tfidf_list = []
local_documents = defaultdict(list)


cnt = 0
for row in open("corona-2nd.ndjson", encoding="utf-8_sig"):
    obj = json.loads(row.strip())
    print(cnt)
    cnt += 1
    word = []
    local = pref2local(prefecture=obj['prefecture'])

    for key in ['name', 'objective']:
        if obj[key]:
            doc = nlp(obj[key])
            for sent in doc.sents:
                for t in sent:
                    if(t.pos_ in ['NOUN', 'PRON', 'PROPN ']):
                        local_documents[local].append(t.text)
#print(local_documents)

docs = []
for key in local_documents.keys():
    print(key)

for key,doc in local_documents.items():
    docs.append({"local":key,"words":",".join(doc)})
#print(docs)

with open('data.txt', 'wb') as f:
    pickle.dump(docs, f)
