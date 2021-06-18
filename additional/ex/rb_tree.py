class Node:
    def __init__(self, value, parent, color, left=None, right=None):
        self.value = value
        self.parent: Node = parent
        self.color = color
        self.left: Node = left
        self.right: Node = right

    def __iter__(self):
        if self.left.color != NULL:
            yield from self.left.__iter__()

        yield self.value

        if self.right.color != NULL:
            yield from self.right.__iter__()

    def iter(self, reverse=False):
        yield self.value

        if reverse:
            node = find_predecessor(self)
        else:
            node = find_successor(self)

        if node is not None:
            yield from node.iter(reverse)


def find_predecessor(node: Node) -> Node:
    if node is None:
        return None
    elif node.left.color != NULL:
        node = node.left
        while node.right.color != NULL:
            node = node.right
        return node
    else:
        p = node.parent
        while p is not None and p.right != node:
            node = p
            p = node.parent
        return p


def find_successor(node: Node) -> Node:
    if node is None:
        return None
    elif node.right.color != NULL:
        node = node.right
        while node.left.color != NULL:
            node = node.left
        return node
    else:
        p = node.parent
        while p is not None and p.left != node:
            node = p
            p = node.parent
        return p


B = "black"
R = "red"
NULL = "NIL"


class RBTree:
    def __init__(self):
        self.root = None
        self.null_node = Node(value=None, color=NULL, parent=None)

    def add(self, value):
        if self.root is None:
            self.root = Node(value, None, B, self.null_node, self.null_node)
            return

        def _add_node(parent):
            if value == parent.value:
                return None
            elif value < parent.value:
                if parent.left.color == NULL:
                    node = Node(value, parent, R, self.null_node, self.null_node)
                    parent.left = node
                    return node
                return _add_node(parent.left)
            else:
                if parent.right.color == NULL:
                    node = Node(value, parent, R, self.null_node, self.null_node)
                    parent.right = node
                    return node
                return _add_node(parent.right)

        node = _add_node(self.root)
        if node is None:
            return

        self._balance(node)

    def _balance(self, node):
        if node.parent is None or node.parent.parent is None:
            return
        if node.parent.color == B:
            return

        x = node
        p = node.parent
        g = p.parent
        u = None

        if p.value < g.value:  # l
            u = g.right
        else:  # r
            u = g.left

        def switch(new_child: Node, old_child: Node):
            parent = old_child.parent
            new_child.parent = parent
            if parent:
                if old_child.value < parent.value:
                    parent.left = new_child
                else:
                    parent.right = new_child
            else:
                self.root = new_child

            if new_child.value < old_child.value:
                old_child.left = new_child.right
                new_child.right.parent = old_child
                new_child.right = old_child
            else:
                old_child.right = new_child.left
                new_child.left.parent = old_child
                new_child.left = old_child
            old_child.parent = new_child

        p.color = R
        x.color = R
        g.color = R

        if u.color == NULL or u.color == B:
            if x.value < p.value:  # l
                if p.value < g.value:  # l
                    switch(p, g)
                    p.color = B
                else:  # r
                    switch(x, p)
                    switch(x, g)
                    x.color = B
            else:  # r
                if p.value < g.value:  # l
                    switch(x, p)
                    switch(x, g)
                    x.color = B
                else:  # r
                    switch(p, g)
                    p.color = B
        else:
            g.right.color = B
            g.left.color = B
            if g != self.root:
                g.color = R
            self._balance(g)

    def find(self, value):
        def _find(root):
            if root is None or root.color == NULL:
                return None
            if value > root.value:
                return _find(root.right)
            elif value < root.value:
                return _find(root.left)
            else:
                return root

        node = _find(self.root)
        return node

    def __str__(self):
        def _print(root: Node, level):
            if level == 0 and root is None:
                return

            if root.right is not None and root.right.color != NULL:
                yield from _print(root.right, level + 1)

            for i in range(level):
                yield "\t"

            yield str(root.value) + root.color[0:1] + '\n'

            if root.left is not None and root.left.color != NULL:
                yield from _print(root.left, level + 1)

        return ''.join(_print(self.root, 0))


t = RBTree()
t.add(123)
t.add(155)
t.add(188)
t.add(15)
t.add(2)
t.add(17)
for val in t.find(15):
    print(val)

# from random import randint
# import time
#
# start_time = time.time()
# l = []
# for i in range(1000000):
#     l.append(i)
# for i in range(1000000, 0, -1):
#     index = randint(0, i-1)
#     t.add(l.pop(index))
# print("--- %s seconds ---" % (time.time() - start_time))
#
# start_time = time.time()
# for i in range(1000000):
#     t.find(i)
# print("--- %s seconds ---" % (time.time() - start_time))
