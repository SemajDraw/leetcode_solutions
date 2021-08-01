

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, value):
        self.root = Node(value)

    # Write an in order search algo for a binary tree
    def in_order_traversal(self, node):
        if node is None:
            return

        self.in_order_traversal(node.left)
        print(node.value)
        self.in_order_traversal(node.right)

class BST:
    def __init__(self, value):
        self.root = Node(value)

    # Return successor value in BST
    def in_order_successor(self, node: Node, value):
        if node is None:
            return
        if node.value == value:
            if node.right:
                successor = node.right
                while successor.left:
                    successor = successor.left
                return successor.value
            elif node.left:
                successor = node.left
                while successor.right:
                    successor = successor.right
                return successor.value
            elif node.left is None and node.right is None:
                return None

        if node.value > value:
            return self.in_order_successor(node.left, value)
        if node.value < value:
            return self.in_order_successor(node.right, value)

    def insert(self, value):
        self.inserter(Node(value), self.root)

    def inserter(self, node, root):
        if root.value > node.value:
            if root.left is None:
                root.left = node
            else:
                self.inserter(node, root.left)
        if root.value < node.value:
            if root.right is None:
                root.right = node
            else:
                self.inserter(node, root.right)

    def print_tree(self, head):
        if head is None:
            return
        print(head.value, '-')
        self.print_tree(head.left)
        self.print_tree(head.right)

    def print_in_order(self, node):
        if node is None:
            return
        self.print_in_order(node.left)
        print(node.value, '-')
        self.print_in_order(node.right)


if __name__ == '__main__':

    # Set up tree
    tree = BST(5)

    # Insert elements
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(9)
    tree.insert(8)
    tree.insert(10)
    tree.insert(7)
    tree.insert(12)

    print('------------- Pre Order -----------')
    tree.print_tree(tree.root)
    print('------------- In Order -----------')
    tree.print_in_order(tree.root)
    print('------------- In Order Successor -----------')
    print(tree.in_order_successor(tree.root, 12))
