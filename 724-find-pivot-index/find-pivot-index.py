class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)

        for i in range(len(nums)):
            if left_sum == right_sum - nums[i]:
                return i

            left_sum += nums[i]
            right_sum -= nums[i]

        return -1
            


        