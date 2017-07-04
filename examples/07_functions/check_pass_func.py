
def check_username_password(username, password):
    while True:
        if len(password) < 8:
            print('Пароль слишком короткий\n')
            password = input('Введите пароль еще раз: ')
        elif username in password:
            print('Пароль содержит имя пользователя\n')
            password = input('Введите пароль еще раз: ')
        else:
            print('Пароль для пользователя {} установлен'.format( username ))
            return [username, password]

print(check_username_password('nata', 'test'))

