"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    number1 = int(get_number_from_linked_list(l1))
    number2 = int(get_number_from_linked_list(l2))
    return create_number_linked_list(number1 + number2)


def create_number_linked_list(number):
    num_array = list(map(int, str(number)))
    last_node = ListNode
    new_node = ListNode
    for num in num_array:
        new_node = ListNode(num)
        if last_node is not None:
            last_node.next = new_node
    return new_node


def get_number_from_linked_list(ll: ListNode):
    number1 = ""
    while ll is not None:
        number1 += str(ll.val)
        ll = ll.next
    return number1


def print_number(number):
    print(int(get_number_from_linked_list(number)))


if __name__ == '__main__':
    # Number 1
    number1_0 = ListNode(int(0))
    number1_1 = ListNode(3)
    number1_2 = ListNode(5)

    number1_2.next = number1_1
    number1_1.next = number1_0
    number1_0.next = None

    # Number 2
    number2_0 = ListNode(1)
    number2_1 = ListNode(4)
    number2_2 = ListNode(6)

    number2_2.next = number2_1
    number2_1.next = number2_0
    number2_0.next = None

    new_number = add_two_numbers(number1_2, number2_2)
    print_number(new_number)
