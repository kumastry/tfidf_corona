from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pickle

data = []
with open('data.txt', 'rb') as f:
    data = pickle.load(f)
#print(docs)

docs = []
locals = []
for  item in data:
    locals.append(item['local'])
    docs.append(item['words'])

vectorizer = TfidfVectorizer(use_idf=True)
tfidf = vectorizer.fit_transform(docs).toarray()
feature_names = np.array(vectorizer.get_feature_names())
f = vectorizer.get_feature_names()
index = tfidf.argsort(axis=1)[:,::-1]

n = int(input())
feature_words = [feature_names[doc[:n]] for doc in index]

#print(tfidf)
#print(len(feature_names))
#print(feature_words)

for i,j in zip(feature_words, locals):
    print(j)
    print(i)
    print('')