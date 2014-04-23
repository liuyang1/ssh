import numpy as np
import scipy.spatial
import sys
sys.path.append("../..")
import logger
log = logger.get()


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

if __name__ == "__main__":
    fo = open("/tmp/ansW")
    W = np.load(fo)
    fo.close()

    K = 8

    log.info("W\n%s" % (W))
    W = W[0:K, :]
    log.info("W\n%s" % (W))
    log.info("W shape %s" % (str(W.shape)))

    import semiSH
    filename = "/home/liuy/obj/gist_batch_1.1000.ans.py.data"
    X, mean = semiSH.loadX(filename)

    bk = mean2bk(mean, W)

    _, col = X.shape
    hashingArray = [hashingK(W, X[:, i]) for i in xrange(col)]
    # print hashingArray

    query = [0, 0, 0, 0, 1, 0, 0, 1]
    query = scipy.array(query)
    h = hashingArray[0]
    r = 2.0 / K
    rank = [scipy.spatial.distance.hamming(query, h) for h in hashingArray]
    print [(idx, val) for idx, val in enumerate(rank) if val < r]
