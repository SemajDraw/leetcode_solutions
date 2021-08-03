class ArrayList(object):

    def __init__(self):
        self.array = []

    def add(self, item: object):
        self.array.append(item)

    def get(self, index):
        return self.array[index]

    def size(self):
        return len(self.array)

    def remove(self, index):
        self.array.pop(index)

    def is_empty(self):
        return len(self.array) == 0

if __name__ == '__main__':

    array_list = ArrayList()
    array_list.add(1)
    array_list.add(2)
    array_list.add(3)

    for i in range(array_list.size()):
        print(array_list.get(i))

    array_list.remove(2)

    for i in range(array_list.size()):
        print(array_list.get(i))

    print('is empty', array_list.is_empty())