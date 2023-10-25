def read_file(a):
    # Открываем файл с именем a и режимом чтения
    file = open(a + ".txt", "r")
    # Считываем данные из файла и сохраняем их в переменную data
    data = file.read()
    # Закрываем файл
    file.close()
    # Преобразуем данные из строки в список
    array = eval(data)
    return array

def write_file(a, arr):
    # Открываем файл с именем a и режимом записи
    file = open(a + ".txt", "w")
    # Преобразуем список в строку
    arr_str = str(arr)
    # Записываем строку в файл
    file.write(arr_str)
    # Закрываем файл
    file.close()
