import sys

config = sys.argv[1]

with open(config, 'r') as file:
    for (i, command) in enumerate(file, 1):
        print 'action %04d cli command "%s"' % (i, command.rstrip())
