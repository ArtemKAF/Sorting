from timeuse import time_use


@time_use
def count_sort(seq):
    """Функция сортировки последовательности методом подсчета"""
    freq = [0]*(max(seq)+1)
    for i in range(len(seq)):
        freq[seq[i]] += 1
    j = 0
    for i in range(len(freq)):
        while freq[i] > 0:
            seq[j] = i
            freq[i] -= 1
            j += 1
    return seq
