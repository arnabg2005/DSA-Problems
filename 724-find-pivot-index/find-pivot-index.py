class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = 1
        
        for i in range(len(nums)):
            left_sum = sum(nums[:left])
            pivot = nums[i]
            right_sum = sum(nums[right:])

            if left_sum == right_sum:
                return i
            else:
                left += 1
                right += 1
        return -1


        