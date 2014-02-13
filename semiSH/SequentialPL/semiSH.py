import sys
import numpy as np
import cPickle as pickle

sys.path.append("../..")
from cifar import load

import logger
log = logger.get()
log.debug("---- rerun ----")
# !!! first 1000
if len(sys.argv) == 1:
    #filename = "/home/liuy/obj/gist.ans.py.data"
    filename = "/home/liuy/obj/gist_batch_1.1000.ans.py.data"
else:
    filename = sys.argv[1]
fo = open(filename)
features = pickle.load(fo)
fo.close()
log.info("load features")

meta, test, train = load.loadData()
labels = load.buildLabelMatrix(train["labels"][0:1000])
log.info("load labels")

X = np.matrix(features)
X = X.T
Xl = X
log.info("X ok")
S = np.matrix(labels)
log.info("S ok")
eta = 0.6  # TODO:

K = 32


def T_func(Sk_tidle, Sk):
    m, n = Sk.shape
    for i in xrange(m):
        for j in xrange(n):
            if Sk_tidle[i, j] * Sk[i, j] >= 0:
                Sk_tidle[i, j] = 0
    return Sk_tidle


M1 = eta * X * X.T
Sk = S
alpha = 0.1  # TODO:
for i in xrange(K):
    M = Xl * Sk * Xl.T + M1
    eigVal, eigVec = np.linalg.eig(M)
    wk = eigVec[0].T
    log.info("wk %d/%d" % (i, K))
    Sk_tidle = Xl.T * wk * wk.T * Xl
    Sk1 = Sk - alpha * T_func(Sk_tidle, Sk)
    X = X - wk * wk.T * X
    Sk = Sk1  # update
log.info("end ok")
