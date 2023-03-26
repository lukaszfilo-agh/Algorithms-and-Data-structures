class NoSpace(Exception):
    pass


class NoData(Exception):
    pass


def hash(key, size):
    if isinstance(key, str):
        s = 0
        for i in key:
            s += ord(i)
        return s % size
    return key % size


class Element:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value

    def __str__(self):
        s = '{'
        s += f'{self.key} : {self.value}'
        s += '}'
        return s


class hash_list:
    def __init__(self, size, c1=1, c2=0) -> None:
        self.tab = [None for i in range(size)]
        self.size = size
        self.c1 = c1
        self.c2 = c2

    def search(self, key):
        # JAK SA KOLIZJE TO SIE PIERDOLI
        hashed_key = hash(key, self.size)

        if isinstance(self.tab[hashed_key], Element):
            if self.tab[hashed_key].key == key:
                return self.tab[hashed_key]

        for i in range(self.size):
            new_key = (hashed_key + self.c1 * i +
                       self.c2 * (i ** 2)) % self.size
            if isinstance(self.tab[new_key], Element):
                if self.tab[new_key].key == key:
                    return self.tab[new_key]
        return None

    def insert(self, key, value):
        hashed_key = hash(key, self.size)
        if self.tab[hashed_key] is None or self.tab[hashed_key] == 'ERASED':
            self.tab[hashed_key] = Element(key, value)
        else:
            if self.tab[hashed_key].key == key:
                self.tab[hashed_key] = Element(key, value)
            else:
                for i in range(self.size):
                    new_key = (hashed_key + self.c1 * i +
                               self.c2 * (i ** 2)) % self.size
                    if self.tab[new_key] is None or self.tab[new_key] == 'ERASED':
                        self.tab[new_key] = Element(key, value)
                        return
                    if self.tab[hashed_key].key == key:
                        self.tab[hashed_key] = Element(key, value)
                        return
                raise NoSpace

    def remove(self, key):
        # JAK SA KOLIZJE TO SIE PIERDOLI
        hashed_key = hash(key, self.size)
        if isinstance(self.tab[hashed_key], Element):
            if self.tab[hashed_key].key == key:
                self.tab[hashed_key] = 'ERASED'
        else:
            for i in range(self.size):
                new_key = (hashed_key + self.c1 * i +
                           self.c2 * (i ** 2)) % self.size
                if self.tab[new_key] == 'ERASED':
                    continue
                if self.tab[new_key].key == key:
                    self.tab[new_key] = 'ERASED'
                    return
            raise NoData

    def __str__(self):
        s = '['
        for i in range(self.size):
            if self.tab[i] is None or self.tab[i] == 'ERASED':
                s += 'None'
            else:
                s += str(self.tab[i])
            if i != self.size - 1:
                s += ', '
        s += ']'
        return s


def test_1(c1=1, c2=0):
    print('====TEST_1====')
    print(f'==== c1 = {c1}, c2 = {c2} ====')
    hashed_list = hash_list(13, c1, c2)
    print(hashed_list)
    values = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
              'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    for i in range(1, 16):
        try:
            if i == 6:
                hashed_list.insert(18, values[i - 1])
            elif i == 7:
                hashed_list.insert(31, values[i - 1])
            else:
                hashed_list.insert(i, values[i - 1])
        except NoSpace:
            print(f'Not enough space for {Element(i, values[i - 1])}')
    print(hashed_list)
    print(hashed_list.search(5))
    print(hashed_list.search(14))
    hashed_list.insert(5, 'Z')
    print(hashed_list.search(5))
    hashed_list.remove(5)
    print(hashed_list)
    print(hashed_list.search(31))
    hashed_list.insert('test', 'W')
    print(hashed_list)
    print('====END====')


def test_2(c1=1, c2=0):
    print('====TEST_2====')
    print(f'==== c1 = {c1}, c2 = {c2} ====')
    hashed_list = hash_list(13, c1, c2)
    values = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
              'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    for i in range(1, 16):
        try:
            hashed_list.insert(13 * i, values[i - 1])
        except NoSpace:
            print(f'Not enough space for {Element(13 * i, values[i - 1])}')
    print(hashed_list)
    print('====END====')


def main():
    test_1()
    test_2()
    test_2(0, 1)
    test_1(0, 1)


if __name__ == '__main__':
    main()
