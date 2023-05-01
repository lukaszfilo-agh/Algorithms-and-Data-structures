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


class Heap:
    def __init__(self, sorting=None):
        if sorting is None:
            self.tab = []
            self.heap_size = 0
        else:
            self.tab = sorting
            self.heap_size = len(self.tab)
            last_parent = self.parent_idx(self.heap_size - 1)
            for i in range(last_parent, -1, -1):
                self.repair(i)

    def tab_size(self) -> int:
        return len(self.tab)

    def is_empty(self):
        if self.heap_size == 0:
            return True
        else:
            return False

    def peek(self):
        if self.heap_size != 0:
            return self.tab[0]
        else:
            return None

    def repair(self, idx):
        replace = idx
        left = self.left_child_idx(idx)
        right = self.right_child_idx(idx)
        if left is not None:
            if self.tab[left] > self.tab[replace]:
                replace = left
        if right is not None:
            if self.tab[right] > self.tab[replace]:
                replace = right

        if replace != idx:
            self.tab[replace], self.tab[idx] = self.tab[idx], self.tab[replace]
            self.repair(replace)

    def dequeue(self):
        if not self.is_empty():
            el = self.tab[0]
            # self.tab[0] = 'DELETED'
            self.heap_size -= 1
            size = self.tab_size() - self.heap_size
            self.tab[0], self.tab[-size] = self.tab[-size], self.tab[0]
            self.repair(0)
            return el
        else:
            return None

    def enqueue(self, elem: Element):
        if self.heap_size == self.tab_size():
            self.heap_size += 1
            self.tab.append(elem)
            idx = self.heap_size - 1
            parent = self.parent_idx(idx)
            while parent is not None and self.tab[parent] < self.tab[idx] and idx > 0:
                self.tab[parent], self.tab[idx] = self.tab[idx], self.tab[parent]
                idx = parent
                parent = self.parent_idx(idx)
        else:
            idx = self.tab_size() - self.heap_size
            self.tab[-idx] = elem

    def parent_idx(self, idx) -> int:
        if idx > 0:
            return (idx - 1) // 2
        else:
            return None

    def left_child_idx(self, idx) -> int:
        child_idx = 2 * idx + 1
        if child_idx < self.heap_size:
            return child_idx
        else:
            return None

    def right_child_idx(self, idx) -> int:
        child_idx = 2 * idx + 2
        if child_idx < self.heap_size:
            return child_idx
        else:
            return None

    def print_tab(self):
        print('{', end='')
        print(*self.tab[:self.heap_size], sep=', ', end='')
        print('}')

    def print_tree(self, idx, lvl):
        if idx is not None:
            if idx < self.heap_size:
                self.print_tree(self.right_child_idx(idx), lvl+1)
                print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else None)
                self.print_tree(self.left_child_idx(idx), lvl+1)


def selection_sort(tab):
    for i in range(len(tab)):
        idx = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[idx]:
                idx = j
        tab[i], tab[idx] = tab[idx], tab[i]


def main():
    elems1 = [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'),
              (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]
    elems2 = [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'),
              (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]

    numbers1 = [random.randint(0, 100) for _ in range(10000)]
    numbers2 = numbers1.copy()

    # test pierwszy heap

    t1 = []
    for i in elems1:
        t1.append(Element(i[1], i[0]))
    heap1 = Heap(t1)
    while heap1.peek() is not None:
        heap1.dequeue()
    print(t1)

    # test drugi heap
    t_start1 = time.perf_counter()
    heap2 = Heap(numbers1)
    while heap2.peek() is not None:
        heap2.dequeue()
    t_stop1 = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop1 - t_start1))

    # test pierwszy selection
    t2 = []
    for i in elems2:
        t2.append(Element(i[1], i[0]))
    selection_sort(t2)
    print(t2)

    # test drugi selection
    t_start2 = time.perf_counter()
    selection_sort(numbers2)
    t_stop2 = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop2 - t_start2))


if __name__ == '__main__':
    main()
