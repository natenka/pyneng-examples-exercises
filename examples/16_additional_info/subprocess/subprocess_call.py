import subprocess

reply = subprocess.call(['ping', '-c', '3', '-n', '8.8.8.8'])

if reply == 0:
    print "Alive"
else:
    print "Unreachable"
