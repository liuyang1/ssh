import load

meta, test, train = load.loadData()

print train
traindata = train["data"]
filenames = train["filenames"]

assert len(traindata) == len(filenames)

path = "/tmp/cifar/"
load.checkDir(path)

for i in xrange(len(traindata)):
    data = traindata[i]
    name = path + filenames[i]
    load.writePPM(32, 32, data, name)
