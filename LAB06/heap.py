class Element:
    def __init__(self, data, priority):
        __priority = priority
        __data = data

    def __lt__(self, other):
        return self.__priority < other.__priority

    def __gt__(self, other):
        return self.__priority > other.__priority


class Heap:
    def __init__(self):
        self.tab = []
        self.heap_size = 0

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

    def parent_idx(self, idx) -> int:
        if idx > 0:
            return idx - 1 // 2
        else:
            return None

    def left_child_idx(self, idx) -> int:
        parent_idx = parent_idx(self, idx)
        child_idx = 2 * parent_idx + 1
        if child_idx < self.heap_size:
            return child_idx
        else:
            return None

    def right_child_idx(self, idx) -> int:
        parent_idx = parent_idx(self, idx)
        child_idx = 2 * parent_idx + 2
        if child_idx < self.heap_size:
            return child_idx
        else:
            return None


def main():
    print('Hello')


if __name__ == '__main__':
    main()
