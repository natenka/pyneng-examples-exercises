import subprocess
from tempfile import TemporaryFile

import argparse


def ping_ip(ip_address, count=3):
    """
    Ping IP address and return tuple:
    On success: (return code = 0, command output)
    On failure: (return code, error output (stderr))
    """
    with TemporaryFile() as temp:
        try:
            output = subprocess.check_output(['ping', '-c', str(count), '-n', ip_address],
                                             stderr=temp)
            return 0, output
        except subprocess.CalledProcessError as e:
            temp.seek(0)
            return e.returncode, temp.read()


parser = argparse.ArgumentParser(description='Ping script')

parser.add_argument('host', action="store", help="IP or name to ping")
parser.add_argument('-c', action="store", dest="count", default=2, type=int,
                    help="Number of packets")

args = parser.parse_args()
print args

rc, message = ping_ip( args.host, args.count )
print message
