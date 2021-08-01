import random


def partition(array: list, low: int, high: int) -> int:
    i = low - 1
    pivot = array[high]
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i + 1


def quickSort(unsorted: list, low=0, high=None):
    if high is None:
        high = len(unsorted) - 1
    if low < high:
        pivot = partition(unsorted, low, high)
        quickSort(unsorted, low, pivot - 1)
        quickSort(unsorted, pivot + 1, high)
    return unsorted


if __name__ == '__main__':
    unsorted = random.sample(range(1, 100), 20)
    print(unsorted)
    print(quickSort(unsorted))