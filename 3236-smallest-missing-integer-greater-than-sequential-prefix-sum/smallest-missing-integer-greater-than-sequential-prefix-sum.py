class Solution(object):
    def missingInteger(self, nums):
        prefix_sum=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                prefix_sum+=nums[i]
            else:
                break
        nums_set=set(nums)
        while prefix_sum in nums_set:
            prefix_sum+=1
        return prefix_sum


        