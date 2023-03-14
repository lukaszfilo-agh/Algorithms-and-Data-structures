class Record:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        print(self.data)


class Doubly_Liked_List:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        # DONE

    def __str__(self):
        s = ''
        record = self.head
        while True:
            s += '-> '
            s += str(record.data)
            if record.next is None:
                return s
            s += '\n'
            record = record.next
        # DONE

    def destroy(self) -> None:
        # TODO
        self.head = None
        self.tail = None

    def add(self, data: Record) -> None:
        data.next = self.head
        if self.head is not None:
            self.head.prev = data
        self.head = data
        if self.head.next is None:
            self.tail = data
        # DONE


    def append(self, data: Record) -> None:
        if self.is_empty():
            self.add(data)
        else:
            rec = self.head
            while rec.next is not None:
                rec = rec.next
            data.prev = rec
            rec.next = data
            self.tail = data
        # DONE

    def remove(self):
        if self.head is not None:
            self.head = self.head.next
            self.head.prev = None
        # DONE

    def remove_end(self):
        # TODO ?
        if self.head is not None:
            rec = self.head
            while rec.next.next is not None:
                rec = rec.next
            rec.next = None

    def is_empty(self) -> bool:
        if self.head is None:
            return True
        else:
            return False
        # DONE

    def lenght(self) -> int:
        x = 0
        record = self.head
        while True:
            x += 1
            if record.next is None:
                return x
            record = record.next
        # DONE

    def get(self):
        return self.head.data
        # DONE


def main():
    uni = [('AGH', 'Kraków', 1919), ('UJ', 'Kraków', 1364), ('PW', 'Warszawa', 1915),
           ('UW', 'Warszawa', 1915), ('UP', 'Poznań', 1919), ('PG', 'Gdańsk', 1945)]

    uczelnie = Doubly_Liked_List()
    uczelnie.append(Record(uni[0]))
    uczelnie.append(Record(uni[1]))
    uczelnie.append(Record(uni[2]))
    uczelnie.add(Record(uni[3]))
    uczelnie.add(Record(uni[4]))
    uczelnie.add(Record(uni[5]))

    print(uczelnie)
    print(uczelnie.lenght())
    uczelnie.remove()
    print(uczelnie.get())
    uczelnie.remove_end()
    print(uczelnie)
    # uczelnie.destroy()
    print(uczelnie.is_empty())
    # uczelnie.remove()
    # uczelnie.remove_end()

    # ucz = Doubly_Liked_List()
    # ucz.add(Record(uni[0]))
    # ucz.add(Record(uni[1]))
    # ucz.add(Record(uni[3]))
    # print(ucz, '\n')
    # ucz.remove()
    # print(ucz)
    # print('glowa:', ucz.head.data)
    # print('ogon:', ucz.tail.data)
    # print(ucz.get())


if __name__ == '__main__':
    main()
