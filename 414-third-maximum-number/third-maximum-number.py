class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        top_three = set()
    
        for num in nums:
            top_three.add(num)
            if len(top_three) > 3:
                top_three.remove(min(top_three))
                
        if len(top_three) == 3:
            return min(top_three)
        
        return max(top_three)