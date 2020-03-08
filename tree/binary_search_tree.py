

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class PreOrderBinarySearchTree:

    def __init__(self):
        self.root = None

    def build_tree(self, node_values):
        number_of_nodes = len(node_values)
        count = 0
        while count <= (number_of_nodes - 1):
            new_node = TreeNode(node_values[count])
            if self.root is None:
                self.root = new_node

            PreOrderBinarySearchTree.add_node(new_node, self.root)
        count += 1

    @staticmethod
    def add_node(node, root):

        if root is None:
            root = node

        if node.val <= root.val:
            PreOrderBinarySearchTree.add_node(node, root.left)

        if node.val >= root.val:
            PreOrderBinarySearchTree.add_node(node, root.right)



if __name__ == '__main__':


    in_order_node_values = [1, 2, 3, 8, 9, 11, 15, 20, 22, 26, 30, 32, 41]

