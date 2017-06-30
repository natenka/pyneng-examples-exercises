import subprocess

try:
    reply = subprocess.check_output(['ping', '-c', '3', '-n', 'a'])
except subprocess.CalledProcessError as e:
    print "Error occurred"
    print "Return code:", e.returncode
