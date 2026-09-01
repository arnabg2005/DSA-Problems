class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums=[num**2 for num in nums]
        return sorted(nums)
        