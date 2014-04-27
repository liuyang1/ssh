import sys
import cPickle as pickle
import numpy as np

import load


if __name__ == "__main__":
    data = load.loadData("/home/liuy/obj/gist.ans.py.data.10000")
    print "loadData"
    X = np.matrix(data)
    X = X.T
    print X.shape
    mean = X.mean(1)
    X -= mean
    X2 = X * X.T

    Ml = load.loadData("/tmp/cifar.Ml")
    X2 += Ml
    print "adjust"

    print "dump var"
    print X2.shape
    load.save(X2, "/tmp/cifar.var")
    print "dump mean"
    print mean.shape
    load.save(mean, "/tmp/cifar.mean")
