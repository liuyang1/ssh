import sys
import subprocess
import load

meta, test, train = load.loadData()

traindata = train["data"]
filenames = train["filenames"]

assert len(traindata) == len(filenames)

path = "/tmp/cifar/"
load.checkDir(path)

convert_flag = False
if sys.argv[1] == "png":
    convert_flag = True
    print "PNG format"
else:
    print "PPM format"


for i in xrange(len(traindata)):
    data = traindata[i]
    name = path + filenames[i]
    name += ".ppm"
    load.writePPM(32, 32, data, name)
    if convert_flag:
        objname = name[:-4]
        cmd = ['convert', name, objname]
        print cmd
        subprocess.call(cmd)
        cmd = ['rm', name]
        subprocess.call(cmd)
    else:
        print name
