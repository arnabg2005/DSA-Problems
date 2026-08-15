class Solution:

    def longestSubsequence(self, nums: list[int]) -> int:
        total_xor = 0
        has_nonzero = False

        for num in nums:
            total_xor ^= num
            if num != 0:
                has_nonzero = True

        if not has_nonzero:
            return 0

        if total_xor != 0:
            return len(nums)

        return len(nums) - 1
