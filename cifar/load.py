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


def writePPM(width, height, data, filename="/tmp/cifar.ppm"):
    fw = open(filename, "wb")
    quant = 255
    fw.write("P6\n%d %d\n%d\n" % (width, height, quant))
    for i in data:
        fw.write(struct.pack("B", i))
    fw.close()
if __name__ == "__main__":
    d = unpickle(conf.trainfn)
    for k, v in d.iteritems():
        print "key: ", k
        print "value: ", v
        print
    # print loadData()
