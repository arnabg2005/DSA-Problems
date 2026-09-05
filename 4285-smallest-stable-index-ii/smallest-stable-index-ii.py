class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums)==0:
            return -1
        
        left= [0]*len(nums)
        n=len(nums)
        left[0] = nums[0]
        for i in range(1,len(nums)):
            left[i] = max(nums[i],left[i-1])

        right = [0] * n
        right[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            right[i] = min(right[i + 1], nums[i])

        for i in range(len(nums)):
            temp=left[i]-right[i]
            if temp<=k:
                return i
        return -1
        