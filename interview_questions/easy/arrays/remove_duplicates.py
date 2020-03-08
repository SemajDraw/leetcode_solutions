

def removeDuplicates(nums):
    i = 1
    while i < len(nums):
        if nums[i] == nums[i-1]:
            del nums[i]
        else:
            i += 1
    return nums


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    ans = removeDuplicates(nums)
    print(ans, len(ans))
