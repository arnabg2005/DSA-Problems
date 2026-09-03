class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = float('-inf')
        sec_largest = float('-inf')
        index = -1
        for i in range(len(nums)):
            if nums[i] > largest:
                sec_largest = largest
                largest = nums[i]
                index = i
            elif nums[i] > sec_largest and nums[i] != largest:
                sec_largest = nums[i]
            
        if largest >= (sec_largest*2):
            return index
        else:
            return -1
            
