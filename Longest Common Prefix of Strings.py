# Given an array of strings arr. Return the longest common prefix among all strings present in the array. If there's no prefix common in all the strings, return "-1".

# Examples :

# Input: arr[] = ["geeksforgeeks", "geeks", "geek", "geezer"]
# Output: gee
# Explanation: "gee" is the longest common prefix in all the given strings.
# Input: arr[] = ["hello", "world"]
# Output: -1
# Explanation: There's no common prefix in the given strings.
# Expected Time Complexity: O(n*min(|arri|))
# Expected Space Complexity: O(min(|arri|))

# Constraints:
# 1 ≤ |arr| ≤ 103
# 1 ≤ |arr[i]| ≤ 103

class Solution:
    def longestCommonPrefix(self, arr):
        min_size = -1
        # print(arr[0], len(arr[0]))
        for i in range(len(arr[0])):
            if self.isSame(arr, i):
                # print('for i', arr[0][i])
                min_size = i
            else:
                break
        return arr[0][:min_size+1] if min_size > -1 else -1
            
            
        
    def isSame(self, arr, index):
        if not arr:
            return 0
        
        for string in arr:
            if index >= len(string):
                return 0
        
        ele = arr[0][index]
        for string in arr:
            if string[index] != ele:
                return 0
        
        return 1