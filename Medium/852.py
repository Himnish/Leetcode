# Peak Index in Mountain Array

# An array arr a mountain if the following properties hold:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

# You must solve it in O(log(arr.length)) time complexity.

# Example 1:

# Input: arr = [0,1,0]
# Output: 1
# Example 2:

# Input: arr = [0,2,1,0]
# Output: 1
# Example 3:

# Input: arr = [0,10,5,2]
# Output: 1

# Constraints:

# 3 <= arr.length <= 105
# 0 <= arr[i] <= 106
# arr is guaranteed to be a mountain array.

class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        i = 0
        j = len(arr) - 1
        n = len(arr)
        while i <= j:
            mid = (i + j) // 2
            if (mid == 0 or arr[mid - 1] < arr[mid]) and (mid == n - 1 or arr[mid + 1] < arr[mid]):
                return mid
            elif mid > 0 and arr[mid - 1] > arr[mid]:
                j = mid - 1
            else:
                i = mid + 1
        return -1
