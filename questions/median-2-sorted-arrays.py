#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#The overall run time complexity should be O(log (m+n)).

# Merge the 2 arrays
#   loop through both arrays using a pointer and compare the values at that index
#   add the smaller one to the merged list then the larger on
#   if one of the list has no more values append the rest of the other list
# If the array is an odd length i can return the middle element
# If array length is even i need to find the median of the 2 middle numbers

class Solution:

    def findMedianSortedArrays(self, nums1: list(int), nums2: list(int)) -> int:
        merged = []
        
        i = 0
        while i < len(nums1) and i < len(nums2):
            if nums1[i] < nums2[i]:
                merged.append(nums1[i])
                merged.append(nums2[i])
            else:
                merged.append(nums2[i])
                merged.append(nums1[i])

            i += 1
        
        if (len(nums1) - 1) > i:
            merged.append(nums1[i:len(nums1)])
        if (len(nums2) - 1) > i:
            merged.append(nums2[i:len(nums2)])

        if len(merged) % 2 != 0:
            return merged[(len(merged) -1) // 2]
        else:
            mid1 = len(merged) // 2
            mid2 = mid1 - 1
            return (merged[mid1] + merged[mid2]) / 2