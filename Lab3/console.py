import math


def function(x):
    if x <= 0:
        return "Функция не существует при данном аргументе"
    else:
        return math.log(x)


def main():
    try:
        a = float(input("Введите начало диапазона a\n"))
    except:
        print("Ошибка: a должно быть числом")
        return
    try:
        b = float(input("Введите конец диапазона b\n"))
    except:
        print("Ошибка: b должно быть числом")
        return
    try:
        h = float(input("Введите шаг h\n"))
    except:
        print("Ошибка: h должно быть числом")
        return

    print("#\tx\tf(x)")

    x = a + h
    i = 0
    while x <= b:
        print(f"{i}\t{x}\t{function(x)}")
        i += 1
        x += h


if __name__ == '__main__':
    main()
