"""Find the Kth largest element in an array"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class KthLargestNumber:

    def find(self, nums, k):
        nums = self.removeDuplicates(nums)
        return self.quickSelect(nums, 0, len(nums) - 1, k)

    def removeDuplicates(self, nums):
        content = {}
        i = 0
        while i < len(nums):
            if nums[i] not in content.keys():
                content[nums[i]] = 1
                i += 1
            else:
                nums.pop(i)
        return nums

    def quickSelect(self, nums, l, r, k):

        position = self.partition(nums, l, r)

        if position == k - 1:
            return nums[position]

        elif position >= k:
            return self.quickSelect(nums, l, position -1, k)

        elif position <= k:
            return self.quickSelect(nums, l + 1, r, k)

    def partition(self, nums, l, r):
        pivot = nums[r]
        i = l
        for j in range(l, r):
            if nums[j] > pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i


if __name__ == "__main__":
    numes = [3,2,1,5,6,4]
    kr = 2

    calculator = KthLargestNumber()
    print(calculator.find(numes, kr))
