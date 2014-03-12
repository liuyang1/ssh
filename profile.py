import subprocess
import time

cmd = ['echo', 'abc']
n = 3
dt = 0
for i in xrange(n):
    t0 = time.time()
    subprocess.call(cmd)
    t1 = time.time()
    nt = t1 - t0
    dt += (nt - dt) / (i + 1)
    print nt
print dt
