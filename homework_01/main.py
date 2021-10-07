"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """

    return [result**2 for result in args]



# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    if num == 1:
        return False
    i = 2
    while i * i <= num and num % i != 0:
        i += 1
    return i * i > num


def filter_numbers(lst, param):
    """
        функция, которая на вход принимает список из целых чисел,
        и возвращает только чётные/нечётные/простые числа
        (выбор производится передачей дополнительного аргумента)
        >>> filter_numbers([1, 2, 3], ODD)
        <<< [1, 3]
        >>> filter_numbers([2, 3, 4, 5], EVEN)
        <<< [2, 4]
        """
    if param == ODD:
        return list(filter(lambda x: x % 2 != 0, lst))
    if param == EVEN:
        return list(filter(lambda x: x % 2 == 0, lst))
    if param == PRIME:
        return list(filter(is_prime, lst))

