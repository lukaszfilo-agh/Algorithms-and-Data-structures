import random
import time


class Element:
    def __init__(self, data, priority):
        self.__priority = priority
        self.__data = data

    def __lt__(self, other):
        return self.__priority < other.__priority

    def __gt__(self, other):
        return self.__priority > other.__priority

    def __repr__(self):
        return f'{self.__priority}: {self.__data}'


def selection_sort(tab):
    for i in range(len(tab)):
        idx = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[idx]:
                idx = j
        tab[i], tab[idx] = tab[idx], tab[i]


def main():
    # test pierwszy
    elems = [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'),
             (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]
    t = []
    for i in elems:
        t.append(Element(i[1], i[0]))
    selection_sort(t)
    print(t)

    # test drugi
    numbers = [random.randint(0, 100) for _ in range(10000)]

    t_start = time.perf_counter()
    selection_sort(numbers)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))


if __name__ == '__main__':
    main()
