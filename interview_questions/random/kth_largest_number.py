

def kthLargestNumber(array, k):
    array.sort()
    return array[-k]


def bruteForceKthLargestNumber(array,k):
    if len(array) == 1:
        return array[0]
    i = 0
    while i < k:
        index, largest = 0,0
        for j, num in enumerate(array):
            if num > largest:
                largest = num
                index = j
        array.pop(index)
        i += 1
    return largest


if __name__ == '__main__':
    array = [5,7,2,3,4,1,6]
    array2 = [5, 7, 2, 3, 4, 1, 6]
    k = 3

    print(bruteForceKthLargestNumber(array, k))
    print(kthLargestNumber(array2, k))
