import pytest
from InsertSort import insertion_sort


# Проверяет, что функция insertion_sort правильно сортирует список положительных чисел [5, 2, 9, 1, 5].
def test_gnome_sort_positive_numbers():
    assert insertion_sort([5, 2, 9, 1, 5]) == [1, 2, 5, 5, 9]


# Проверяет, что функция insertion_sort правильно сортирует список отрицательных чисел [-3, -7, -2, -8, -1].
def test_gnome_sort_negative_numbers():
    assert insertion_sort([-3, -7, -2, -8, -1]) == [-8, -7, -3, -2, -1]


# Проверяет, что функция insertion_sort правильно обрабатывает пустой список [].
def test_gnome_sort_empty_list():
    assert insertion_sort([]) == []


# Проверяет, что функция insertion_sort корректно обрабатывает список с одним элементом [5].
def test_gnome_sort_single_element():
    assert insertion_sort([5]) == [5]


# Проверяет, что функция insertion_sort правильно сортирует список с повторяющимися элементами [3, 3, 3, 2, 1].
def test_gnome_sort_repeating_elements():
    assert insertion_sort([3, 3, 3, 2, 1]) == [1, 2, 3, 3, 3]


if __name__ == '__main__':
    pytest.main()