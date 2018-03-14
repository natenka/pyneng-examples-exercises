from pprint import pprint


def filter_file_lines(filename, substring):
    result = []
    with open(filename) as f:
        for line in f:
            if substring in line:
                result.append(line)
    return result


if __name__ == "__main__":
    pprint(filter_file_lines('config_r1.txt', 'ip address'))

