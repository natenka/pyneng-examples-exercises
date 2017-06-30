import subprocess
import os

DNULL = open(os.devnull, 'w')

reply = subprocess.call(['ping', '-c', '3', '-n', '8.8.8.8'], stdout=DNULL)

if reply == 0:
    print "Alive"
else:
    print "Unreachable"
