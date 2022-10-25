# Основной скрипт тестирования алгоритмов сортировок
import bubblesort as bs
import countsort as cs
import shakersort as sh_s
import timeuse as tu

if __name__ == '__main__':
    ns_list = [5, 3, 233, 9, 300, 1, 5, 143, 3, 27, 99, 1, 15, 5, 77, 1, 246, 11, 9, 15, 99, 194, 2, 111, 0,
               13, 298, 7, 19, 5, 6, 54, 34, 1, 62, 286, 39, 174, 15, 100, 59, 37, 82, 61, 90, 33, 64]

    print(ns_list)
    s_list = tu.time_use(bs.bubble_sort)(ns_list)
    print(s_list)

    ns_list = [5, 3, 233, 9, 300, 1, 5, 143, 3, 27, 99, 1, 15, 5, 77, 1, 246, 11, 9, 15, 99, 194, 2, 111, 0,
               13, 298, 7, 19, 5, 6, 54, 34, 1, 62, 286, 39, 174, 15, 100, 59, 37, 82, 61, 90, 33, 64]

    print(ns_list)
    s_list = tu.time_use(cs.count_sort)(ns_list)
    print(s_list)

    ns_list = [5, 3, 233, 9, 300, 1, 5, 143, 3, 27, 99, 1, 15, 5, 77, 1, 246, 11, 9, 15, 99, 194, 2, 111, 0,
               13, 298, 7, 19, 5, 6, 54, 34, 1, 62, 286, 39, 174, 15, 100, 59, 37, 82, 61, 90, 33, 64]

    print(ns_list)
    s_list = tu.time_use(sh_s.shakersort)(ns_list)
    print(s_list)
