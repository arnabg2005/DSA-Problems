class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        frequency = {}
        left = 0
        max_len = 0
        
        for right in range(len(nums)):
            current_num = nums[right]
            frequency[current_num] = frequency.get(current_num, 0) + 1
            
            while frequency[current_num] > k:
                left_num = nums[left]
                frequency[left_num] -= 1
                left += 1     
            max_len = max(max_len, right - left + 1)
            
        return max_len
