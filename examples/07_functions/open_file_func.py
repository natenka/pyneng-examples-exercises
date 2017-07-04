

def open_file(filename):
    """
    filename - имя файла (строка)
    """
    with open(filename) as f:
        file_as_str =  f.read()
        f.seek(0)
        file_as_list = f.readlines()
        return file_as_str, file_as_list

file_str, file_list = open_file('r1.txt'))

print(file_str, file_list)
