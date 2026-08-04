class Solution(object):
    def missingNumber(self, nums):
        sumi=sum(nums)
        result=0
        for i in range(len(nums)+1):
            result=result+i
        return result-sumi
        