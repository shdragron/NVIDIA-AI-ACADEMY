import numpy as np

a = [
    [1,2,3],
    [3,2,1]
]

b = np.array(a)

c = np.argmax(b,axis=0)
d = np.argmax(b,axis=1)
print(b.shape)
print(b)
print(c)
print(d)