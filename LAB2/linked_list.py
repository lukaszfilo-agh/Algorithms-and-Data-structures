class Record:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __str__(self):
        print(self.data)


class Liked_List:
    def __init__(self) -> None:
        self.head = None

    def __str__(self):
        s = ''
        record = self.head
        while True:
            s += '->'
            s += str(record.data)
            s += '\n'
            if record.next is None:
                return s
            record = record.next

    def destroy(self) -> None:
        self.head = None

    def add(self, data: Record) -> None:
        data.next = self.head
        self.head = data

    def append(self, data: Record) -> None:
        rec = self.head
        while rec.next.next is not None: 
            rec = rec.next
        rec.next.next = data

    def remove(self):
        self.head = self.head.next

    def remove_end(self):
        rec = self.head
        while rec.next.next is not None: 
            rec = rec.next
        rec.next = None
            
    def is_empty(self) -> bool:
        if self.head is None:
            return True
        else:
            return False

    def lenght(self) -> int:
        x = 0
        record = self.head
        while True:
            x += 1
            if record.next is None:
                return x
            record = record.next

    def get(self):
        return self.head.data


def main():
    uni = [('AGH', 'Kraków', 1919), ('UJ', 'Kraków', 1364), ('PW', 'Warszawa', 1915),
           ('UW', 'Warszawa', 1915), ('UP', 'Poznań', 1919), ('PG', 'Gdańsk', 1945)]

    uczelnie = Liked_List()
    uczelnie.add(Record(uni[0]))
    uczelnie.add(Record(uni[1]))
    uczelnie.add(Record(uni[2]))

if __name__ == '__main__':
    main()
