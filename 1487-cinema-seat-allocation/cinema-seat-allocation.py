class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        import collections
        
        row_reserved = collections.defaultdict(set)
        for r, s in reservedSeats:
            if 2 <= s <= 9:
                row_reserved[r].add(s)
                
        # Each row can seat at most 2 groups initially
        ans = 2 * n
        
        for r, seats in row_reserved.items():
            left = not (2 in seats or 3 in seats or 4 in seats or 5 in seats)
            right = not (6 in seats or 7 in seats or 8 in seats or 9 in seats)
            middle = not (4 in seats or 5 in seats or 6 in seats or 7 in seats)
            
            if left and right:
                continue # Can fit 2 groups, no deduction
            elif left or right or middle:
                ans -= 1 # Can fit only 1 group, lose 1
            else:
                ans -= 2 # Cannot fit any group, lose 2
                
        return ans
