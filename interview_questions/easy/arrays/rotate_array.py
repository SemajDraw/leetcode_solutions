import random


def rotateNumsSlice(nums, k):
    temp = nums
    nums = nums[-k:]
    nums.extend(temp[:-k])
    return nums


def rotateNumsLoop(nums, k):
    for i in range(0, k):
        nums.insert(0, nums.pop())
    return nums


if __name__ == '__main__':
    nums = random.sample(range(1,11), 10)
    print(nums)
    # print(rotateNumsSlice(nums, 3))
    print(rotateNumsLoop(nums, 3))