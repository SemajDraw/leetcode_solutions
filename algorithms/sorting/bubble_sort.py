import random


def bubbleSort(unsorted: list) -> list:
    i = 0
    while i < len(unsorted):
        j = i + 1
        while j < len(unsorted):
            if unsorted[i] > unsorted[j]:
                temp = unsorted[j]
                unsorted[j] = unsorted[i]
                unsorted[i] = temp
            j += 1
        i += 1
    return unsorted


if __name__ == '__main__':
    unsorted = random.sample(range(1, 100), 20)
    print(unsorted)
    print(bubbleSort(unsorted))
