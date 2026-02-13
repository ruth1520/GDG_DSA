class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        numm = set(nums)
        for i in range(n + 1):
            if i not in numm:
                return i
