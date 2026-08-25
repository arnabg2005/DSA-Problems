class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        multiple=k
        while multiple in nums:
            multiple+=k
        return multiple

        