import cPickle as pickle
import numpy

def save(data, filename):
    fo = open(filename, "wb")
    pickle.dump(data, fo, pickle.HIGHEST_PROTOCOL)
    fo.close()

def loadData(filename):
    return pickle.load(open(filename, "rb"))


if __name__ == "__main__":
    data = pickle.load(open("/home/liuy/obj/gist.ans.py.data.10000", "rb"))
