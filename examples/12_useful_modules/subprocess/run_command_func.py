import subprocess


def run_command(command):
    result = subprocess.run(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding='utf-8')
    if result.returncode == 0:
        return True, result.stdout
    else:
        return False, result.stderr


success, func_result = run_command('ping -c 3 8.8.8.8')
if success:
    print('Команда выполнилась успешно')
else:
    print('Возникла ошибка')

print(func_result)

success2, func_result2 = run_command('ping -c 3 a')
if success2:
    print('Команда выполнилась успешно')
else:
    print('Возникла ошибка')

print(func_result2)
