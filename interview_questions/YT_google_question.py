"""
Given a collection of numbers find a matching pair that is equal to a value

[1,2,3,9] 8
[1,2,4,4] 8
"""


def bruteForce(array: list, target: int) -> list:
    valid_numbers = []
    i = 0
    while i < len(array):
        j = i + 1
        while j < len(array):
            if array[i] + array[j] == target:
                valid_numbers.append([i, j])
            j += 1
        i += 1
    return valid_numbers


def pointers(array: list, target: int) -> list:
    left = 0
    right = len(array) - 1
    valid_numbers = []
    while left < right:
        if array[left] + array[right] > target:
            right -= 1
        elif array[left] + array[right] < target:
            left += 1
        else:
            valid_numbers.append([left, right])
            right -= 1

    return valid_numbers


if __name__ == '__main__':
    array1 = [1,2,3,9]
    array2 = [1,2,4,4]
    target = 8
    print('Brute force: ', bruteForce(array1, target))
    print('Brute force: ', bruteForce(array2, target))

    print('Pointers: ', pointers(array1, target))
    print('Pointers: ', pointers(array2, target))
