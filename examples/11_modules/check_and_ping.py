from check_ip_functions import check_ip
from ping_function import ping_ip


def return_correct_ip(ip_addresses):
    correct = []
    for ip in ip_addresses:
        if check_ip(ip):
            correct.append(ip)
    return correct


ip_list = ['10.1.1.1', '8.8.8.8', '2.2.2']

for ip in return_correct_ip(ip_list):
    print(ip, ping_ip(ip))
