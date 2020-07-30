

def singleNumber(nums: list) -> int:
    singleSet = {}
    for num in nums:
        if num not in singleSet:
            singleSet[num] = 1
        else:
            singleSet[num] += 1

    for key, value in singleSet.items():
        if value == 1:
            return key


if __name__ == '__main__':
    nums = [4, 1, 2, 1, 2]
    print(singleNumber(nums))