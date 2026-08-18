class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if k == n:
            return max(nums)
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        if k == 1:
            single_nums = [num for num in nums if count[num] == 1]
            return max(single_nums) if single_nums else -1
        
        candidates = []
        if count[nums[0]] == 1:
            candidates.append(nums[0])
        if count[nums[-1]] == 1:
            candidates.append(nums[-1])
            
        return max(candidates) if candidates else -1
