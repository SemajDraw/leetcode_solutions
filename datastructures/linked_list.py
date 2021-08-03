class Node(object):

    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList(object):

    def __init__(self):
        self.head = Node()

    # append
    def append(self, val):
        node = self.head
        while node.next != None:
            node = node.next
        node.next = Node(val)
    
    # length
    def length(self):
        count = 0
        node = self.head
        while node.next != None:
            count += 1
            node = node.next
        return count

    # display
    def display(self):
        node = self.head
        values = []
        while node.next != None:
            if node.next.val != None:

                values.append(node.next.val)
            node = node.next
        print(values)
            
    # get
    def get(self, index):
        count = 0
        node = self.head
        while node.next != None:
            if count == index:
                return node.val
            count += 1
            node = node.next

        if index > count:
            return IndexError('Index out of range')

    # remove
    def remove(self, index):
        node = self.head
        prev = None
        count = 0
        while node.next != None:
            if index == count:
                prev.next = node.next
                break
            count += 1
            prev = node
            node = node.next
        
        if index > count:
            return IndexError('Index out of range')

    # reverse
    def reverse(self):
        prev = None
        node = self.head
        
        while node != None:
            next = node.next
            node.next = prev
            prev = node
            node = next
        
        self.head = Node()
        self.head.next = prev

if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)

    print('length', linked_list.length())
    linked_list.display()
    print('get node 3 value', linked_list.get(3))

    linked_list.remove(3)
    linked_list.display()

    linked_list.reverse()
    linked_list.display()