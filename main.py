# Основной скрипт тестирования алгоритмов сортировок
import time
from datetime import timedelta
import bubblesort as bs

if __name__ == '__main__':
    ns_list = [5, 3, 233, 9, 300, 1, 5, 143, 3, 27, 99, 1, 15, 5, 77, 1, 246, 11, 9, 15, 99, 194, 2, 111, 0,
               13, 298, 7, 19, -5, 6, 54, 34, -1, 62, 286, 39, 174, -15, -100, 59, 37, 82, 61, 90, -33, -64]
    s_time = time.monotonic()
    s_list = bs.bubblesort(ns_list)
    e_time = time.monotonic()
    print(s_list)
    print(f"Время сортировки массива сортировкой пузырьком: {timedelta(e_time - s_time)}")
