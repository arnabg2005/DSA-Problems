import math

class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = n * (n + 1) // 2
        
        x = int(math.sqrt(total_sum))
        
        if x * x == total_sum:
            return x
            
        return -1
