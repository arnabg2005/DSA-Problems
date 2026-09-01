class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi=0
        count=0
        for i in nums:
            if i==1:
                count+=1
            else:
                maxi=max(count,maxi)
                count=0
        return max(maxi,count)