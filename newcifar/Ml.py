import conf
import random
import load
import sys
import cPickle as pickle
import numpy as np

pairNum = 1000


def buildLabelMatrix(labels):
    size = len(labels)
    mat = np.zeros((size, size))
    cnt = 0
    while 1:
        p0, p1 = random.randint(0, size - 1), random.randint(0, size - 1)
        if mat[p0, p1] != 0:
            continue
        v = 1 if labels[p0] == labels[p1] else -1
        mat[p0, p1] = v
        mat[p1, p0] = v
        cnt += 1
        if cnt == pairNum:
            break
    return mat


def filterMatrix(X, Sl):
    idxlst = [idx for idx, val in enumerate(Sl) if any(val)]
    Xl = X[:, idxlst]
    Sl = np.matrix(Sl)
    Sl = Sl[idxlst, :][:, idxlst]
    return Xl, Sl

if __name__ == "__main__":
    data = load.loadData("/home/liuy/obj/gist.ans.py.data.10000")
    X = np.matrix(data)
    X = X.T
    mean = X.mean(1)
    X -= mean
    print "load X"

    train = load.loadData("/home/liuy/obj/cifar-10-batches-py/data_batch_1")
    labels = train["labels"]
    print "load Label"

    Sl = buildLabelMatrix(labels)
    print "buildLabelMatrix"
    Xl, Sl = filterMatrix(X, Sl)
    print "filterMatrix"
    print Xl.shape
    print Sl.shape

    Ml = Xl * Sl
    Ml = Ml * Xl.T
    print Ml.shape

    var = load.loadData("/tmp/cifar.var")
    adjustVar = var + Ml * conf.eta
    print "adjust", adjustVar.shape
    load.save(adjustVar, "/tmp/cifar.adjustVar")
