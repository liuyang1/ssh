import subprocess
import sys
sys.path.append("..")
from cifar import load

meta, test, train = load.loadData()

traindata = train["data"]

gist = "lear_gist-1.2/compute_gist"
# using lear gist implemention
gistcmd = [gist, "/tmp/cifar.ppm"]

cnt = 0
allans = []
for data in traindata:
    load.writePPM(32,32,data)
    ans = subprocess.check_output(gistcmd)
    ans = [float(i) for i in ans.split()]
    allans.append(ans)
    cnt += 1
    print cnt

import cPickle as pickle

fw = open("/tmp/gist.ans.py.data","wo")
pickle.dump(allans, fw)
fw.close()
