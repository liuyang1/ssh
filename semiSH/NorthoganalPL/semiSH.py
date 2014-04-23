import sys
import numpy as np
import cPickle as pickle

sys.path.append("../..")
from cifar import load

import logger
log = logger.get()

def loadX(filename):
    fo = open(filename)
    features = pickle.load(fo)
    fo.close()
    log.info("load features")
    X = np.matrix(features)
    X = X.T
    mean = X.mean(1)
    X -= mean
    log.info("X zero mean")
    return X, mean

if __name__ == "__main__":
    if len(sys.argv) == 1:
        filename = "/home/liuy/obj/gist_batch_1.1000.ans.py.data"
        # filename = "/home/liuy/obj/gist.ans.py.data"
    else:
        filename = sys.argv[1]

    X, _ = loadX(filename)
    Xl = X
    log.info("X ok")

    meta, test, train = load.loadData()
    labels = load.buildLabelMatrix(train["labels"][0:1000])
#labels = load.buildLabelMatrix(train["labels"])
    log.info("load labels")


    S = np.matrix(labels)
    log.info("S ok")
    eta = 0.6

# M0 = Xl*S*Xl.T
    M0 = Xl * S
    log.info("Xl * S ok")
    M0 = M0 * Xl.T
    log.info("M0=Xl*S*Xl.T ok")
    M1 = eta * X * X.T
    log.info("M1 ok")
    M = M0 + M1
    log.info("M ok")

    log.info("M size %s" % (str(M.shape)))
    V, W = np.linalg.eig(M)
    log.info("W\n%s" % (W))
    log.info("V\n%s" % (V))

# ft = open("eig", "w")
# for i in V:
#     print i
#     ft.write("%s\r\n" % (i))
# ft.close()
# log.info("write V txt file ok")

    fw = open("/tmp/ansW", "wb")
    W.dump(fw)
    fw.close()
    log.info("end and quit")
