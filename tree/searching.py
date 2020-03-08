from typing import List


class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:

    def __init__(self):
        self.head = None

    def buildTree(self, nodesVals: List[int]):
        if len(nodesVals) <= 0:
            return 'Enter a non empty array'

        if self.head is None:
            self.createHeadNode(nodesVals[0])

        for val in nodeVals[1:]:
            self.insertNode(val, self.head)

    def insertNode(self, val: int, node: Node) -> None:
        if val <= node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self.insertNode(val, node.left)

        elif val > node.val:
            if node.right is None:
                node.right = Node(val)
            else:
                self.insertNode(val, node.right)

    def createHeadNode(self, val):
        self.head = Node(val)

    def printInOrder(self, node):
        if node is None:
            return
        self.printInOrder(node.left)
        print(node.val)
        self.printInOrder(node.right)

    class DepthFirstSearch:

        """
            In order (Left,Root,Right)
        """
        def inOrderSearch(self, node: Node, val):
            if node is None:
                return
            self.inOrderSearch(node.left, val)
            if node.val == val:
                print("Node with value found at ", node)
                return True
            return self.inOrderSearch(node.right, val)

        """
            Pre order (Root,Left,Right)
        """
        def preOrderSearch(self, node: Node, val: int):
            if node is None:
                return False
            if node.val == val:
                print("Node with value found at ", node)
                return True
            self.preOrderSearch(node.left, val)
            self.preOrderSearch(node.right, val)

        """
            Post order (Left,Right,Root)
        """
        def postOrderSearch(self, node: Node, val: int):
            if node is None:
                return
            self.postOrderSearch(node.left, val)
            self.postOrderSearch(node.right, val)
            if node.val == val:
                print("Node with value found at ", node)
                return True

    def breathFirstSearch(self):
        pass

    def binarySearch(self, node: Node, val: int) -> bool:
        if node is None:
            print("No node contains this value")
            return False
        if val == node.val:
            print("Found at ", node)
            return True
        if val < node.val:
            return self.binarySearch(node.left, val)
        if val > node.val:
            return self.binarySearch(node.right, val)


if __name__ == '__main__':
    nodeVals = [20, 15, 11, 9, 41, 32, 30, 2, 3, 8, 26, 22, 1]

    tree = Tree()
    tree.buildTree(nodeVals)

    print("Printing tree in order")
    tree.printInOrder(tree.head)

    print("\nBinary search")
    tree.binarySearch(tree.head, 26)

    print("\nSearching tree in order")
    tree.DepthFirstSearch().inOrderSearch(tree.head, 26)

    print("\nSearching tree in pre order")
    tree.DepthFirstSearch().preOrderSearch(tree.head, 26)

    print("\nSearching tree in post order")
    tree.DepthFirstSearch().postOrderSearch(tree.head, 26)
