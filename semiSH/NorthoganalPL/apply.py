import numpy as np

fo = open("/tmp/w")
W = np.load(fo)
fo.close()
print W
print W.shape
