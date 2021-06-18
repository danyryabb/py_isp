import random


class Node:

    def __init__(self, value, nxt=None):
        self.value = value
        self.nxt = nxt

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        return other.value == self.value

    def __hash__(self):
        return hash(self.value)


class LinkedList:

    def __init__(self, nodes: list = None):
        self.head = None
        if nodes is not None:
            node = Node(value=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.nxt = Node(value=elem)
                node = node.nxt

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.nxt

    def __repr__(self):
        node = self.head
        values = []
        while node is not None:
            values.append(str(node.value))
            node = node.nxt
        return " -> ".join(values)

    def delete_repeats(self):
        repeats = set(self)
        self.__init__(list(repeats))


def main():
    ls = LinkedList([1, 2, 1, "asd", 11, "asd", 11])
    ls.delete_repeats()
    print(ls)


if __name__ == '__main__':
    main()