import subprocess

reply = subprocess.check_output(['ping', '-c', '3', '-n', '8.8.8.8'])

print "Result:"
print reply
