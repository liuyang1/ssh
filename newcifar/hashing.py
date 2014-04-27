import sys
import conf
import numpy as np
import scipy
import load


def hashing(w, x):
    ret = w * x
    ret = ret[0, 0]
    ret = int((1 + np.sign(ret)) / 2)
    return ret


def hashingK(W, x):
    code = [hashing(w, x) for w in W]
    return hashing2bit(code)


def hashing2bit(x):
    return scipy.array(x)
    # return np.packbits(x)[0]


def mean2bk(mean, W):
    return W * mean


def hashingKout(W, x, bk):
    return hashingK(W, x - bk)


def buildNonorW():
    L = load.loadData("/tmp/cifar.nonor.L")
    U = load.loadData("/tmp/cifar.nonor.U")
    Uk = U[:, 0:conf.K]
    W = L * Uk
    return W.T

def buildOrthW():
    W = load.loadData("/tmp/cifar.north.w")
    return W[0:conf.K, :]


def buildSeqLHW():
    W = load.loadData("/tmp/cifar.splh.w")
    W = np.matrix(W)
    return W[0:conf.K, :]


if __name__ == "__main__":
    K = conf.K
    W = buildSeqLHW()

    data = load.loadData("/home/liuy/obj/gist.ans.py.data.10000")
    X = np.matrix(data)
    X = X.T
    X -= X.mean(1)

    _, col = X.shape
    hashingArray = [hashingK(W, X[:, i]) for i in xrange(col)]
    load.save(hashingArray, "/tmp/cifar.hashingArray")
