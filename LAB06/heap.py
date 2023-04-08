class Element:
    def __init__(self, data, priority):
        self.__priority = priority
        self.__data = data

    def __lt__(self, other):
        return self.__priority < other.__priority

    def __gt__(self, other):
        return self.__priority > other.__priority
    
    def __str__(self):
        return f'{self.__priority} : {self.__data}'


class Heap:
    def __init__(self):
        self.tab = []

    def heap_size(self) -> int:
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

    def dequeue(self):
        pass

    def enqueue(self, elem: Element):
        self.tab.append(elem)
        idx = self.heap_size() - 1
        parent = self.parent_idx(idx)
        while parent is not None and self.tab[parent] < self.tab[idx] and idx > 0:
            self.tab[parent], self.tab[idx] = self.tab[idx], self.tab[parent]
            idx = parent
            parent = self.parent_idx(idx)

    def parent_idx(self, idx) -> int:
        if idx > 0:
            return (idx - 1) // 2
        else:
            return None

    def left_child_idx(self, idx) -> int:
        child_idx = 2 * idx + 1
        if child_idx < self.heap_size():
            return child_idx
        else:
            return None

    def right_child_idx(self, idx) -> int:
        child_idx = 2 * idx + 2
        if child_idx < self.heap_size():
            return child_idx
        else:
            return None

    def print_tab(self):
        print('{', end=' ')
        print(*self.tab[:self.heap_size()], sep=', ', end=' ')
        print('}')

    def print_tree(self, idx, lvl):
        if idx is not None:
            if idx < self.heap_size():
                self.print_tree(self.right_child_idx(idx), lvl+1)
                print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else None)
                self.print_tree(self.left_child_idx(idx), lvl+1)


def main():
    p = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    d = 'GRYMOTYLA'

    heap = Heap()

    for i in range(len(p)):
        heap.enqueue(Element(d[i], p[i]))

    heap.print_tree(0, 0)
    heap.print_tab()
    el = heap.dequeue()
    print(heap.peek())
    # heap.print_tab()
    print(el)

    # while heap.peek() is not None:
    #     print(heap.dequeue())
    # heap.print_tab()


if __name__ == '__main__':
    main()
