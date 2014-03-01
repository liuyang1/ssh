import numpy as np
import cPickle as pickle
import sys
sys.path.append("../..")
import logger
log = logger.get()

import time

filename = "/home/liuy/obj/gist_batch_1.1000.ans.py.data"
fo = open(filename)
features = pickle.load(fo)
fo.close()
log.info("load features")

X = np.matrix(features)
X = X.T
log.info("X ok")

t1 = time.time()
q, r = np.linalg.qr(X)
log.info("qr ok")

r2 = r * r.T
# x2 = q * r * r.T * q.T
r2 = q * r2 * q.T
t2 = time.time()
log.info("elapsed %s seconds" % (t2 - t1))


x2 = X * X.T
t3 = time.time()
log.info("elapsed %s seconds" % (t3 - t2))

print x2 - r2
