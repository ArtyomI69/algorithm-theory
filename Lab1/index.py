from InsertSort import insertion_sort
from FileSystem import write_file, read_file

alist = input('Введите числа массива: ').split()
alist = [int(x) for x in alist]
insertion_sort(alist)
print('Отсортированный массив: ', end='')
print(alist)
write_file("sortResult", alist)
read_file("sortResult")