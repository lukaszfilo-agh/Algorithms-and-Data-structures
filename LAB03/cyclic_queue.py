class queue:
    def __init__(self, size=5) -> None:
        self.tab = [None for i in range(size)]
        self.size = size
        self.read = 0
        self.write = 0

    def is_empty(self) -> bool:
        if self.read == self.write:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab[self.read]

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            elem = self.tab[self.read]
            self.tab[self.read] = None
            if self.read == self.size - 1:
                self.read = 0
            else:
                self.read += 1
        return elem

    def enqueue(self, data):
        self.tab[self.write] = data
        if self.write == self.size - 1:
            self.write = 0
        else:
            self.write += 1

        if self.read == self.write:
            self.realloc_n()

    def __str__(self):
        d = self.read
        s = '['
        while self.tab[d] is not None:
            s += str(self.tab[d])
            # if d != self.write - 1:
            #     s += ', '
            if d == self.size - 1:
                d = 0
            else:
                d += 1
            if self.tab[d] is not None:
                s += ', '
        s += ']'
        return s

    def realloc_n(self):
        new_size = 2 * self.size
        new_tab = [None for i in range(new_size)]
        new_tab[0:self.write] = self.tab[0:self.write]
        new_tab[-(self.size-self.write):] = self.tab[self.write:]
        self.read += self.size
        self.tab = new_tab
        self.size = new_size


def main():
    test2()
    test3()
    # tablica = queue()
    # tablica.enqueue(1)
    # tablica.enqueue(2)
    # tablica.enqueue(3)
    # tablica.enqueue(4)
    # print(tablica.dequeue())
    # print(tablica.peek())
    # print(tablica)
    # tablica.enqueue(5)
    # tablica.enqueue(6)
    # tablica.enqueue(7)
    # tablica.enqueue(8)
    # print(tablica)

    # while tablica.peek() is not None:
    #     print(tablica.dequeue())
    # print(tablica)


def test2():
    tab = queue()
    for i in range(6):
        tab.enqueue(i)

    print(tab)

    for i in range(2):
        print(tab.dequeue())

    print(tab)

    for i in range(6, 15):
        tab.enqueue(i)

    while tab.peek() is not None:
        print(tab.dequeue())

    print(tab)


def test3():
    q = queue()
    q.dequeue()
    q.enqueue(3)
    q.enqueue(5)
    q.enqueue(7)
    print(q)
    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q)
    q.enqueue(9)
    print(q)
    q.enqueue(11)
    print(q)


if __name__ == '__main__':
    main()
