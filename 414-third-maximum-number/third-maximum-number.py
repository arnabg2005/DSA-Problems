class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        max1 = max2 = max3 = None
    
        for num in nums:
            # Skip duplicate values to ensure we only count distinct maximums
            if num == max1 or num == max2 or num == max3:
                continue
                
            # Case 1: num is greater than the current highest maximum
            if max1 is None or num > max1:
                max3 = max2
                max2 = max1
                max1 = num
                
            # Case 2: num is between the first and second maximum
            elif max2 is None or num > max2:
                max3 = max2
                max2 = num
                
            # Case 3: num is between the second and third maximum
            elif max3 is None or num > max3:
                max3 = num
                
        # If the third distinct maximum exists, return it; otherwise, return the absolute maximum
        return max3 if max3 is not None else max1