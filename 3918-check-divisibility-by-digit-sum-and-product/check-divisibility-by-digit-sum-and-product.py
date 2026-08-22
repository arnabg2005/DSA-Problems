class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        orginal=n
        sum1=0
        product=1
        while n>0:
            digit=n%10
            sum1=sum1+digit
            product=product*digit
            n=n//10
        total=sum1+product
        if orginal%total==0:
            return True
        else:
            return False
