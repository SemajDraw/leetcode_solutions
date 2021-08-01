
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        last_node = self.head
        while last_node:
            print(last_node.data)
            last_node = last_node.next


def merge_two_sorted_lists(node1: Node, node2: Node) -> Node:
    dummy_node = Node(0)
    tail = dummy_node

    while True:
        if node1 is None:
            tail.next = node2
            break
        if node2 is None:
            tail.next = node1
            break

        if node1.data <= node2.data:
            tail.next = node1
            node1 = node1.next
        else:
            tail.next = node2
            node2 = node2.next
        tail = tail.next
    return dummy_node.next


if __name__ == "__main__":

    l1 = LinkedList()
    l1.append(3)
    l1.append(4)
    l1.append(6)

    l2 = LinkedList()
    l2.append(6)
    l2.append(7)
    l2.append(8)

    merged_head = merge_two_sorted_lists(l1.head, l2.head)
    while merged_head:
        print(merged_head.data)
        merged_head = merged_head.next
