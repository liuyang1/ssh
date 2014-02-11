import sys
import numpy as np
import cPickle as pickle

sys.path.append("../..")
from cifar import load

import logger
log = logger.get()
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
eta = 0.6 #TODO:

# M0 = Xl*S*Xl.T
M0 = Xl * S
log.info("Xl * S ok")
M0 = M0 * Xl.T
log.info("M0=Xl*S*Xl.T ok")
M1 = eta * X * X.T
log.info("M1 ok")
M = M0 + M1
log.info("M ok")

eigVal, eigVec = np.linalg.eig(M)
log.info("eig M ok")

rho = max(0, - min(eigVal)) * 1.2

Q = np.eye(M.shape[0]) + 1/rho*M
log.info("Q ok")

L = np.linalg.cholesky(Q)
log.info("cholesky decompostion L ok")
U = L.T # TODO: U = L.T ???
log.info("cholesky decompostion U ok")

k = 100
Uk = U[:,:k]

log.info('W = L U k')
W = L * Uk
log.info("W \n%s" % (W))

fw = open("/tmp/ansW", "wb")
W.dump(fw)
fw.close()
log.info("end and quit")
