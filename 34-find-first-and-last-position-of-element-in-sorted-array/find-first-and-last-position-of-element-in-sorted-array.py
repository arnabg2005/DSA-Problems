class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findBound(isFirst: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    bound = mid
                    if isFirst:
                        right = mid - 1  
                    else:
                        left = mid + 1   
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
                    
            return bound

        return [findBound(True), findBound(False)]
        