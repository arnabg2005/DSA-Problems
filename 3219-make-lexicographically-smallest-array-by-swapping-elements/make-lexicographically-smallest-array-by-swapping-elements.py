from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        sorted_pairs = sorted([(val, idx) for idx, val in enumerate(nums)])
        
        result = [0] * n
        i = 0
        while i < n:
            j = i + 1
            while j < n and sorted_pairs[j][0] - sorted_pairs[j - 1][0] <= limit:
                j += 1
            group_vals = [sorted_pairs[k][0] for k in range(i, j)]
            group_indices = sorted([sorted_pairs[k][1] for k in range(i, j)])
            for val, idx in zip(group_vals, group_indices):
                result[idx] = val
            i = j
            
        return result
