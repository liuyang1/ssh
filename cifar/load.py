import conf
import struct


def unpickle(filename):
    import cPickle
    fo = open(filename, 'rb')
    d = cPickle.load(fo)
    fo.close()
    return d


def loadData():
    fn = (conf.metafn, conf.testfn, conf.trainfn)
    data = map(unpickle, fn)
    return data


def buildLabelMatrix(labels):
    print "TODO: unkown labels should be ZERO"
    mat = []
    for l in labels:
        vec = [1 if i == l else -1 for i in labels]
        mat.append(vec)
    return mat


def writePPM(width, height, data, filename="/tmp/cifar.ppm"):
    fw = open(filename, "wb")
    quant = 255
    fw.write("P6\n%d %d\n%d\n" % (width, height, quant))
    for i in data:
        fw.write(struct.pack("B", i))
    fw.close()


if __name__ == "__main__":
    meta, test, train = loadData()
    labels = train["labels"]
    print labels
    for row in buildLabel(labels):
        print row
