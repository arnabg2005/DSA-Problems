class Solution(object):
    def minSubArrayLen(self, target, nums):
        left=0
        window_sum=0
        min_lenght=float('inf')
        for right in range(len(nums)):
            window_sum+=nums[right]
            while window_sum>=target:
                min_lenght=min(min_lenght,right-left+1)
                window_sum-=nums[left]
                left+=1
        if min_lenght==float('inf'):
            return 0
        return min_lenght