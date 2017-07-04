
def correct_ip(ipaddress):
    check_int = [ int(octet) for octet in ipaddress.split('.') if octet.isdigit()]
    correct = [ o for o in check_int if 0 <= o <= 255 ]
    if len(correct) == 4:
        return True
    else:
        return False

print('10.1.1.1', correct_ip('10.1.1.1'))
print('10.1.1.', correct_ip('10.1.1.'))
print('a.1.1.1', correct_ip('a.1.1.1'))


# Эту функцию можно использовать так:
ip = input("Введите IP-адрес: ")

while not correct_ip(ip):
    ip = input('Введите IP-адрес: ')


