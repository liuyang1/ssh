import conf


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


if __name__ == "__main__":
    print unpickle(conf.metafn)
    #print loadData()
