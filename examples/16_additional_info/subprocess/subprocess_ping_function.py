import subprocess
from tempfile import TemporaryFile


def ping_ip(ip_address):
    """
    Ping IP address and return tuple:
    On success:
        * return code = 0
        * command output
    On failure:
        * return code
        * error output (stderr)
    """
    with TemporaryFile() as temp:
        try:
            output = subprocess.check_output(['ping', '-c', '3', '-n', ip_address],
                                             stderr=temp)
            return 0, output
        except subprocess.CalledProcessError as e:
            temp.seek(0)
            return e.returncode, temp.read()

print ping_ip('8.8.8.8')
print ping_ip('a')
