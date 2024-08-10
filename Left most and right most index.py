# Given a sorted array with possibly duplicate elements. The task is to find indexes of first and last occurrences of an element X in the given array.

# Note: If the element is not present in the array return {-1,-1} as pair.

 

# Example 1:

# Input:
# N = 9
# v[] = {1, 3, 5, 5, 5, 5, 67, 123, 125}
# X = 5
# Output:
# 2 5
# Explanation:
# Index of first occurrence of 5 is 2
# and index of last occurrence of 5 is 5.
# Example 2:

# Input:
# N = 9
# v[] = {1, 3, 5, 5, 5, 5, 7, 123, 125}
# X = 7
# Output:
# 6 6
 

# Your Task:  
# You don't need to read input or print anything. Your task is to complete the function indexes() which takes the array v[] and an integer X as inputs and returns  the first and last occurrence of the element X. If the element is not present in the array return {-1,-1} as pair.



class Solution:
    def indexes(self, v, x):
        index = self.binarySearch(x, v, 0, len(v)-1)
        # print(index)
        start = end = index
        if index == -1:
            return -1,-1
        while start>=1 and v[start-1] == x:
            start = start - 1
        while end<len(v)-1 and v[end+1] == x:
            end = end + 1
        return start, end
    
    def binarySearch(self, ele, arr, start, end):
        if start > end:
            return -1
        else:
            mid = (start+end)//2
            if arr[mid] == ele:
                return mid
            elif arr[mid] > ele:
                return self.binarySearch(ele, arr, start, mid-1)
            else:
                return self.binarySearch(ele, arr, mid+1, end)
