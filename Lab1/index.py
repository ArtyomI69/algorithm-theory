import time

from InsertSort import insertion_sort
from FileSystem import write_file, read_file
from utils import random_array

# alist = input('Введите числа массива: ').split()
# alist = [int(x) for x in alist]
# insertion_sort(alist)
# print('Отсортированный массив: ', end='')
# print(alist)
# write_file("sortResult", alist)
# read_file("sortResult")

# n = 25000
# arr = random_array(n, 1, 999)
# start = time.time()
# insertion_sort(arr)
# end = time.time()
# time = end - start
# print(n, "элементов. Время выполнения:", time, "секунд")

for i in range(1000, 30000, 1000):
    arr = random_array(i, 1, 999)
    start = time.time()
    insertion_sort(arr)
    end = time.time()
    result = end - start
    print(i, result)
