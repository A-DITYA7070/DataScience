import numpy as np

ar = np.array([1,2,3,34,45,224,2,1,2,3,34,45,343])

ar2 = np.unique(ar)

print(ar2)

print(np.concatenate(ar,ar2))