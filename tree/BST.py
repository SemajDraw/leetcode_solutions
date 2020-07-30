

class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):

    def __init__(self, value):
        self.root = Node(value)

    def insert(self, value):
        self.inserter(self.root, Node(value))

    def inserter(self, head, node):
        if node.value < head.value:
            if head.left is None:
                head.left = node
            else:
                self.inserter(head.left, node)
        if node.value > head.value:
            if head.right is None:
                head.right = node
            else:
                self.inserter(head.right, node)

    def search(self, value):
        return self.searcher(self.root, value)

    def searcher(self, head, value):
        if head is None:
            return False
        if head.value == value:
            return True
        if value < head.value:
            return self.searcher(head.left, value)
        if value > head.value:
            return self.searcher(head.right, value)

    def printTree(self, head):
        if head is None:
            return
        print(head.value, '-')
        self.printTree(head.left)
        self.printTree(head.right)


if __name__ == '__main__':
    # Set up tree
    tree = BST(4)

    # Insert elements
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)

    # Check search
    # Should be True
    print(tree.search(4))
    # Should be False
    print(tree.search(6))

