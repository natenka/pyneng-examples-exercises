for username in ['nata', 'sveta', 'sergey']:
    password = input('Введите пароль для пользователя {}: '.format(username) )
    while True:
        password = input('Введите пароль еще раз: ' )
        if len(password) < 8:
            print('Пароль слишком короткий\n')
            continue
        elif username in password:
            print('Пароль содержит имя пользователя\n')
        else:
            print('Пароль для пользователя {} установлен'.format( username ))
            # завершает цикл while
            break
    print(username, password)

