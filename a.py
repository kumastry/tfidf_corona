
import numpy as np


a_2d = np.array([[20, 3, 100], [1, 200, 30], [300, 10, 2]])
index = a_2d.argsort(axis=1)[:,::-1]
i = a_2d.argsort(axis=1)
print(a_2d)

print(index)


for doc in index:
    print(doc[:2])