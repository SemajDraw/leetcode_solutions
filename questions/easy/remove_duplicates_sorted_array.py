""" Easy """

def remove_duplicates_generic(nums: list):
    count = 0
    while count < (len(nums) - 1):
        if nums[count] == nums[count + 1]:
            del nums[count + 1]
        else:
            count += 1
    return len(nums)


def remove_duplicates_pythonic(nums: list):
    return len(list(set(nums)))


if __name__ == '__main__':
    print(remove_duplicates_generic([0,0,1,1,1,2,2,3,3,4]))

    print(remove_duplicates_pythonic([1,1,2]))
