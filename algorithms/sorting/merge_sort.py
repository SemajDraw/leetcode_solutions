import random


def merge(left: list, right: list) -> list:
    left_index, right_index = 0, 0
    sorted = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted.append(left[left_index])
            left_index += 1
        else:
            sorted.append(right[right_index])
            right_index += 1

    sorted.extend(left[left_index:]) if left_index < right_index else sorted.extend(right[right_index:])
    return sorted


def mergeSort(unsorted: list) -> list:
    if len(unsorted) <= 1:
        return unsorted
    mid = len(unsorted)//2
    left, right = mergeSort(unsorted[:mid]), mergeSort(unsorted[mid:])

    return merge(left, right)


if __name__ == '__main__':

    unsorted = random.sample(range(1, 100), 30)
    print(unsorted)
    print(mergeSort(unsorted))
