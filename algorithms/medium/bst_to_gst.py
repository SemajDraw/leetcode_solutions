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
        self.val_list = []
        self.bst_to_gst()

    def bst_to_gst(self):
        self.val_list = self.ordered_tree_vals(self.root)
        self.change_node_values(self.root)

        self.ordered_tree_vals(self.root)
        return self.root

    def change_node_values(self, node):
        if node is None:
            return

        node.val = sum(self.val_list[self.val_list.index(node.val):])
        BinaryToGreaterSumTree.change_node_values(self, node.left)
        BinaryToGreaterSumTree.change_node_values(self, node.right)

    def ordered_tree_vals(self, node: TreeNode):
        if node is None:
            return []
        print(node.val)
        val_list = self.ordered_tree_vals(node.left) + [node.val] + self.ordered_tree_vals(node.right)
        return val_list


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

