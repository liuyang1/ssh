import load
import numpy as np
import sys

if __name__ == "__main__":
    M = load.loadData("/tmp/cifar.adjustVar")
    print M.shape
    V, W = np.linalg.eigh(M)
    print V
    print W
    load.save(W, "/tmp/cifar.north.w")

