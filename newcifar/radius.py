import conf
import numpy as np
import random
import load
import scipy.spatial
import hashing


def query(q, hashingArray):
    rank = [scipy.spatial.distance.hamming(q, h) for h in hashingArray]
    K = len(q)
    r = 2.0 / len(q)
    return [idx for idx, val in enumerate(rank) if val <= r]


if __name__ == "__main__":
    K = conf.K
    W = hashing.buildSeqLHW()

    hashingArray = load.loadData("/tmp/cifar.hashingArray")

    data = load.loadData("/home/liuy/obj/gist.ans.py.data.10000")
    X = np.matrix(data)
    X = X.T
    X -= X.mean(1)

    train = load.loadData("/home/liuy/obj/cifar-10-batches-py/data_batch_1")
    label = train["labels"]

    precisionLst, recallLst = [], []
    idxLst = range(0, len(data))
    random.shuffle(idxLst)
    idxLst = idxLst[0:200]
    for idx in idxLst:
        x = X[:, idx]
        objlabel = label[idx]

        q = hashing.hashingK(W, x)
        ret = query(q, hashingArray)
        cnt = len([i for i in ret if label[i] == objlabel]) - 1
        try:
            precision = (cnt + 0.0) / (len(ret) - 1)
        except ZeroDivisionError:
            precision = 0
        try:
            recall = (cnt + 0.0) / (len([i for i in label if i == objlabel]) - 1)
        except ZeroDivisionError:
            recall = 0
        precisionLst.append(precision)
        recallLst.append(recall)
    print sum(precisionLst) / len(precisionLst)
    print sum(recallLst) / len(recallLst)
