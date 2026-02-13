class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = max(nums)
        max_index = nums.index(max_num)
        
        for i in range(len(nums)):
            if i != max_index and nums[i] * 2 > max_num:
                return -1
        
        return max_index
        
