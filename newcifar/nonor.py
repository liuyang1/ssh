import load
import numpy as np
import sys

if __name__ == "__main__":
    M = load.loadData("/tmp/cifar.adjustVar")
    print M.shape
    eigVal, _ = np.linalg.eig(M)
    print min(eigVal)
    rho = max(0, - min(eigVal))
    print rho
    rho *= 1.2
    if rho == 0:
        print "rho setting 0.1"
        rho = 0.1

    Q = np.eye(M.shape[0]) + 1/rho *M

    L = np.linalg.cholesky(Q)
    U = L.T

    load.save(L, "/tmp/cifar.nonor.L")
    load.save(L, "/tmp/cifar.nonor.U")

