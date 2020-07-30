import random


def quickSort(unsorted: list):
    if len(unsorted) <= 1:
        return unsorted
    smaller, equal, larger = [], [], []
    pivot = median(unsorted)
    for num in unsorted:
        if num < unsorted[pivot]: smaller.append(num)
        elif num == unsorted[pivot]: equal.append(num)
        else: larger.append(num)

    return quickSort(smaller)+equal+quickSort(larger)


def median(elements: list) -> int:
    low = 0
    mid = len(elements) // 2
    pivot = high = len(elements) - 1
    if elements[low] < elements[mid]:
        if elements[mid] < elements[high]:
            pivot = mid
    elif elements[low] < elements[high]:
        pivot = low
    return pivot


if __name__ == '__main__':
    unsorted = random.sample(range(1, 30), 10)
    print('Unsorted:', unsorted)
    print('Sorted: ', quickSort(unsorted))
