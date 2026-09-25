class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set1 = set()
        for i in range(len(nums)):
            if nums[i] in set1:
                return nums[i]
            else:
                set1.add(nums[i])
        return 0
        