import numpy as np
import sys


mat = [[1, 0], [0, 1], [1,1]]
mat = np.matrix(mat)

def matrix2raw(mat, fn):
    height, width = mat.shape
    fn.write("%s %s\r\n" % (height, width))
    for i in xrange(height):
        for j in xrange(width):
            fn.write("%s " % mat[i,j])
        fn.write("\r\n")


if __name__ == "__main__":
    matrix2raw(mat, sys.__stdout__)
