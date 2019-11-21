"""
Easy
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""


def two_sum(nums: list, target: int) -> list:
    sum_nums = []
    for index_x, x in enumerate(nums):
        for index_y in range(index_x, len(nums)):
            if index_x != index_y:
                if x + nums[index_y] == target:
                    sum_nums.append(index_x)
                    sum_nums.append(index_y)
                    return sum_nums


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))
