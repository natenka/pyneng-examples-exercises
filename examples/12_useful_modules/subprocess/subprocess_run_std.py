import subprocess

reply = subprocess.run(
    ['ping', '-c', '3', '-n', '8.8.8.8'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    encoding='utf-8')

if reply.returncode == 0:
    print("Alive")
    result = reply.stdout
else:
    print("Unreachable")
    result = reply.stderr

print('Result:\n', result)
