# Given a number x and an array of integers arr, find the smallest subarray with sum greater than the given value. If such a subarray do not exist return 0 in that case.

# Examples:

# Input: x = 51, arr[] = [1, 4, 45, 6, 0, 19]
# Output: 3
# Explanation: Minimum length subarray is [4, 45, 6]
# Input: x = 100, arr[] = [1, 10, 5, 2, 7]
# Output: 0
# Explanation: No subarray exist
# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)

# Constraints:
# 1 ≤ arr.size, x ≤ 105
# 0 ≤ arr[] ≤ 104



class Solution:
    def smallestSubWithSum(self, x, arr):
        sum = arr[0]
        start = 0
        end = 0
        min_length = float('inf') 
        while end<len(arr)-1:
            if sum <= x:
                end = end + 1
                sum = sum + arr[end]
            elif sum > x:
                while sum > x:
                    if len(arr[start:end+1]) < min_length:
                      min_length = len(arr[start:end+1])
                    sum = sum - arr[start]
                    start = start + 1
        if sum > x:
                while sum > x:
                    if len(arr[start:end+1]) < min_length:
                      min_length = len(arr[start:end+1])
                    sum = sum - arr[start]
                    start = start + 1
        return 0 if min_length == float('inf') else min_length