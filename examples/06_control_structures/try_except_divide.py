# Вариант с try/except
while True:
    a = input("Введите число: ")
    b = input("Введите второе число: ")
    try:
        result = int(a) / int(b)
    except ValueError:
        print("Поддерживаются только числа")
    except ZeroDivisionError:
        print("На ноль делить нельзя")
    else:
        print(result)
        break

# Аналогичное решение без try/except
while True:
    a = input("Введите число: ")
    b = input("Введите второе число: ")
    if a.isdigit() and b.isdigit():
        if int(b) == 0:
            print("На ноль делить нельзя")
        else:
            print(int(a) / int(b))
            break
    else:
        print("Поддерживаются только числа")
