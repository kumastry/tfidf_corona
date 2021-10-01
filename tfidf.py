from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pickle
import json

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)

data = []
with open('data.txt', 'rb') as f:
    data = pickle.load(f)
#print(docs)

docs = []
locals = []
for  item in data:
    locals.append(item['local'])
    docs.append(item['words'])

vectorizer = TfidfVectorizer(sublinear_tf=True)
tfidf = vectorizer.fit_transform(docs).toarray()
feature_names = np.array(vectorizer.get_feature_names())
f = vectorizer.get_feature_names()
index = tfidf.argsort(axis=1)[:,::-1]

n = int(input())
feature_words = [feature_names[doc[:n]] for doc in index]

#print(tfidf)
#print(len(feature_names))
#print(feature_words)

json_data = []

for i,j in zip(feature_words, locals):
    print(j)
    print(i)
    print('')

    json_data.append({"local":j, "top":i})


with open('tfidf.json',  mode='wt', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, cls = MyEncoder,indent=2)
