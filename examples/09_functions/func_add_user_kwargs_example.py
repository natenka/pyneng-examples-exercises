def check_passwd(username, password, min_length=8, check_username=True):
    if len(password) < min_length:
        print('Пароль слишком короткий')
        return False
    elif check_username and username in password:
        print('Пароль содержит имя пользователя')
        return False
    else:
        print(f'Пароль для пользователя {username} прошел все проверки')
        return True


def add_user_to_users_file(user, users_filename='users.txt', **kwargs):
    while True:
        passwd = input(f'Введите пароль для пользователя {user}: ')
        if check_passwd(user, passwd, **kwargs):
            break
    with open(users_filename, 'a') as f:
        f.write(f'{user},{passwd}')

