class Solution(object):
    def twoSum(self, nums, target):
        hashmap={}
        for i in range(len(nums)):
            need=target-nums[i]

            if need in hashmap:
                return [hashmap[need],i]
            hashmap[nums[i]]=i
        