class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def square_fun(n):
            square = 0
            while n>0:
                digit = n % 10 
                square += digit * digit
                n = n // 10
            return square
        slow = n
        fast = n
        while fast != 1:
            slow = square_fun(slow)
            fast = square_fun(square_fun(fast))

            if fast == 1:
                return True
            if slow == fast:
                return False
        return True
        
