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

    def __delete(self, key, node: Node):
        if key > node.key:
            node.right = self.__delete(key, node.right)
        elif key < node.key:
            node.left = self.__delete(key, node.left)
        else:
            if node.right is None:
                return node.left
            elif node.left is None:
                return node.right

            new_node = node.right
            while new_node.left is not None:
                new_node = new_node.left

            node.key, node.value = new_node.key, new_node.value
            node.right = self.__delete(new_node.key, node.right)

        return node

    def delete(self, key):
        return self.__delete(key, self.root)

    def __print(self, node: Node):
        if node.left is not None:
            self.__print(node.left)
        print(f'{node.key} {node.value}', end=', ')
        if node.right is not None:
            self.__print(node.right)

    def print(self):
        self.__print(self.root)
        print()

    def __node_search(self, key, node: Node):
        if node.key == key:
            return node
        elif key > node.key:
            return self.__node_search(key, node.right)
        elif key < node.key:
            return self.__node_search(key, node.left)

    def __height(self, node: Node):
        if node is None:
            return 0
        else:
            left = self.__height(node.left)
            right = self.__height(node.right)

            if left > right:
                return left + 1
            else:
                return right + 1

    def height(self, key=None):
        if key == None:
            key = self.root.key
        node = self.root
        if key != node.key:
            new_node = self.__node_search(key, node)
            return self.__height(new_node)
        else:
            return self.__height(node)


def main():
    tree = BST()
    dict = {50: 'A', 15: 'B', 62: 'C', 5: 'D', 20: 'E', 58: 'F',
            91: 'G', 3: 'H', 8: 'I', 37: 'J', 60: 'K', 24: 'L'}
    for key in dict:
        tree.insert(key, dict[key])
    tree.print_tree()
    tree.print()
    print(tree.search(24).value)
    tree.insert(20, 'AA')
    tree.insert(6, 'M')
    tree.delete(62)
    tree.insert(59, 'N')
    tree.insert(100, 'P')
    tree.delete(8)
    tree.delete(15)
    tree.insert(55, 'R')
    tree.delete(50)
    tree.delete(5)
    tree.delete(24)
    print(tree.height())
    tree.print()
    tree.print_tree()


if __name__ == '__main__':
    main()
