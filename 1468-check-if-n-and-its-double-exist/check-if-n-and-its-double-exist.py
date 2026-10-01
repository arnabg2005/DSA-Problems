class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen = set()
    
        for num in arr:
            if (num * 2 in seen) or (num % 2 == 0 and num // 2 in seen):
                return True
            
            seen.add(num)
            
        return False
            