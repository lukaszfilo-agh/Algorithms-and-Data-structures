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


def insertionsort(tab):
    for i in range(len(tab) - 1):
        while tab[i + 1] < tab[i] and i >= 0:
            tab[i + 1], tab[i] = tab[i], tab[i + 1]
            i -= 1


def main():
    elems1 = [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'),
              (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]
    elems2 = [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'),
              (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]

    numbers1 = [random.randint(0, 100) for _ in range(10000)]
    numbers2 = numbers1.copy()

    # test pierwszy insertion
    t1 = []
    for i in elems1:
        t1.append(Element(i[1], i[0]))
    insertionsort(t1)
    print(t1)

    # test drugi insertion
    t_start1 = time.perf_counter()
    insertionsort(numbers1)
    t_stop1 = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop1 - t_start1))


if __name__ == '__main__':
    main()
