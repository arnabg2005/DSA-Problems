class Solution(object):
    def containsDuplicate(self, nums):
        hashmap={}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
            hashmap[nums[i]]=i
        return False
        