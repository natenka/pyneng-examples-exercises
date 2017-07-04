for username in ['nata', 'sveta', 'sergey']:
    #Пропустить пользователя nata
    if username == 'nata':
        continue
        # эта строка не отобразится:
        print('nata')

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
            break
    print(username, password)

