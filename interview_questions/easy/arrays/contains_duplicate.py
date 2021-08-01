

def hasDuplicates(array):
    duplicateSet = {}
    for num in array:
        if num not in duplicateSet:
            duplicateSet[num] = 1
        else:
            duplicateSet[num] += 1

    for num in duplicateSet.values():
        if num > 1:
            return True
    return False


if __name__ == '__main__':
    array = [1,1,1,3,3,4,3,2,4,2]

    print(hasDuplicates(array))


