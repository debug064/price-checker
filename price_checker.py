import microcenter
import random
import time
import sys

while True:
    microcenter.main(sys.argv[1:])
    secs = random.randrange(1200, 4000, 10)
    print("Sleep for %s seconds" % secs)
    time.sleep(secs)