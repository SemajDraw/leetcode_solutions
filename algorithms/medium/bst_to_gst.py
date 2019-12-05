"""
Given the root of a binary search tree with distinct values,
modify it so that every node has a new value equal to the sum of the values of the original tree
that are greater than or equal to node.val.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryToGreaterSumTree:

    def __init__(self, root: TreeNode):
        self.root = root
        self.bst_to_gst()

    def bst_to_gst(self):
        tree_count = self.get_tree_count(self.root)
        self.change_node_values(self.root, tree_count)

        self.get_tree_count(self.root)
        return self.root

    def change_node_values(self, node, tree_count):
        if node is None:
            return
        BinaryToGreaterSumTree.change_node_values(self, node.left, tree_count)
        tree_count = tree_count - node.val
        node.val = tree_count
        BinaryToGreaterSumTree.change_node_values(self, node.right, tree_count)

    @staticmethod
    def get_tree_count(node: TreeNode) -> int:
        if node is None:
            return 0
        print(node.val)
        return (node.val +
                BinaryToGreaterSumTree.get_tree_count(node.left) +
                BinaryToGreaterSumTree.get_tree_count(node.right))


if __name__ == '__main__':

    root = TreeNode(4)
    left_1 = TreeNode(1)
    left_2 = TreeNode(0)
    left_3 = TreeNode(2)
    left_4 = TreeNode(3)
    right_1 = TreeNode(6)
    right_2 = TreeNode(5)
    right_3 = TreeNode(7)
    right_4 = TreeNode(8)

    root.left = left_1
    left_1.left = left_2
    left_1.right = left_3
    left_3.right = left_4

    root.right = right_1
    right_1.left = right_2
    right_1.right = right_3
    right_3.right = right_4

    bt_st = BinaryToGreaterSumTree(root)

