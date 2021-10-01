import pickle

docs = []
with open('predata.txt', 'rb') as f:
    docs = pickle.load(f)
print(len(docs))
for item in docs:
    print(item['local'])