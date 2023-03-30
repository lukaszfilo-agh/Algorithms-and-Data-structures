class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        s = f'{self.key} {self.value}'
        return s


class BST:
    def __init__(self):
        self.root = None

    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node != None:
            self.__print_tree(node.right, lvl+5)

            print()
            print(lvl*" ", node.key, node.value)

            self.__print_tree(node.left, lvl+5)

    def __search(self, key, node: Node):
        if node is not None:
            if node.key > key:
                return self.__search(key, node.left)
            elif node.key < key:
                return self.__search(key, node.right)
            elif node.key == key:
                return node
        else:
            return None

    def search(self, key):
        return self.__search(key, self.root)

    def __insert(self, key, value, node: Node):
        if node == None:
            return Node(key, value)
        else:
            if node.key < key:
                if node.right is not None:
                    return self.__insert(key, value, node.right)
                else:
                    node.right = Node(key, value)
            elif node.key > key:
                if node.left is not None:
                    return self.__insert(key, value, node.left)
                else:
                    node.left = Node(key, value)
            else:
                node.value = value
                return node

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
            return
        return self.__insert(key, value, self.root)

    def delete(self):
        pass

    def print(self):
        pass

    def height(self):
        pass


def main():
    tree = BST()
    dict = {50: 'A', 15: 'B', 62: 'C', 5: 'D', 20: 'E', 58: 'F',
            91: 'G', 3: 'H', 8: 'I', 37: 'J', 60: 'K', 24: 'L'}
    for key in dict:
        tree.insert(key, dict[key])
    tree.print_tree()
    print(tree.search(50))


if __name__ == '__main__':
    main()
