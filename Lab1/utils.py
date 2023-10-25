import random


def random_array(n, a, b):
    # Создаем пустой список
    arr = []
    # Цикл for добавляет в список a случайных чисел в диапазоне от b до c
    for i in range(n):
        arr.append(random.randint(a, b))
    return arr