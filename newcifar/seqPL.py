import sys
import numpy as np
import cPickle as pickle
import scipy.spatial

import Ml
import load

train = load.loadData("/home/liuy/obj/cifar-10-batches-py/data_batch_1")
labels = train["labels"]

data = load.loadData("/home/liuy/obj/gist.ans.py.data.10000")
X = np.matrix(data)
X = X.T
X -= X.mean(1)
X0 = X

eta = 0.6  # TODO:


def T_func(Sk_tidle, Sk):
    m, n = Sk.shape
    for i in xrange(m):
        for j in xrange(n):
            if Sk_tidle[i, j] * Sk[i, j] >= 0:
                Sk_tidle[i, j] = 0
    return Sk_tidle


S = Ml.buildLabelMatrix(labels)
Xlf, Slf = Ml.filterMatrix(X0, S)

print "size ", X.shape
Sk = Slf
zeros = np.zeros((X.shape[0], 1))
beta = max([scipy.spatial.distance.euclidean(i, zeros) for i in X0.T])
alpha = 1 / beta * 0.3
print alpha
W = []
K = 24
for i in xrange(K):
    print i, K
    Mc = eta * X * X.T
    print "Mc"
    print "filter Matrix"
    Mlf = Xlf * Slf * Xlf.T
    M = Mlf + Mc
    print "M"
    eigVal, eigVec = np.linalg.eig(M)
    wk = eigVec[0].T
    print "eig"
    Sk_tidle = Xlf.T * wk * wk.T * Xlf
    Sk1 = Sk - alpha * T_func(Sk_tidle, Sk)
    print "udpate S"
    X = X - wk * wk.T * X
    print "update X"
    Sk = Sk1  # update
    wk = wk.T
    W.extend(wk.tolist())
W = np.matrix(W)
load.save(W, "/tmp/cifar.splh.w")
