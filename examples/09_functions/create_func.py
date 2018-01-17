# First version - without return operator


def open_file(filename):
    '''Documentation string'''
    with open(filename) as f:
        print(f.read())


print(open_file('r1.txt'))
print(open_file('ospf.txt'))

# Second version - with return operator


def open_file(filename):
    '''Documentation string'''
    with open(filename) as f:
        return f.read()


result = open_file('r1.txt')
print(result)

# Third version - after return


def open_file(filename):
    print('Reading file', filename)
    with open(filename) as f:
        return f.read()
        print('Done')


result = open_file('r1.txt')
