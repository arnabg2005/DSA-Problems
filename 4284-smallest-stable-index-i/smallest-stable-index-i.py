class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        left = [nums[0]]
        right = [nums[i] for i in range(n)]
        for i in range(n):
            maxi=max(left)
            mini=min(right)
            if (maxi-mini)<=k:
                return i
            else:
                left.append(nums[i])
                right.remove(nums[i])
        return -1   