
import sys
import cPickle as pickle

# !!! first 1000
if len(sys.argv) == 1:
    filename = "/home/liuy/obj/gist_batch_1.1000.ans.py.data"
else:
    filename = sys.argv[1]
fo = open(filename)
features = pickle.load(fo)
fo.close()

sys.path.append("..")
from cifar import load
meta, test, train = load.loadData()
labels = load.buildLabelMatrix(train["labels"][0:1000])

import numpy as np
X = np.matrix(features)
X = X.T
Xl = X
S = np.matrix(labels)
eta = 0.6

M0 = Xl*S*Xl.T
M1 = eta * X * X.T
M = M0 + M1
print "M ok"

W, V = np.linalg.eig(M)
print W
print V
