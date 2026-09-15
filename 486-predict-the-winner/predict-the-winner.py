class Solution:
    def predictTheWinner(self,nums: list[int]) -> bool:
        n = len(nums)
        # memo cache to store results of subproblems
        memo = {}
        
        def get_max_diff(i, j):
            if i == j:
                return nums[i]
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Current player picks the left end or the right end
            pick_left = nums[i] - get_max_diff(i + 1, j)
            pick_right = nums[j] - get_max_diff(i, j - 1)
            
            memo[(i, j)] = max(pick_left, pick_right)
            return memo[(i, j)]
        
        # If Player 1's net score advantage is >= 0, they win
        return get_max_diff(0, n - 1) >= 0  