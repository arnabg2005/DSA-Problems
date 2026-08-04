class Solution(object):
    def findMissingElements(self, nums):
        start, end = min(nums), max(nums)
        nums_set = set(nums)
    
        missing = [num for num in range(start, end + 1) if num not in nums_set]
    
        return missing 