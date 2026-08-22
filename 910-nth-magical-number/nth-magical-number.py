class Solution(object):


    def nthMagicalNumber(self, n, a, b):
        def gcd_num(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        MOD = 10**9 + 7

        left = 1
        right = n * min(a, b)
        temp=gcd_num(a,b)
        lcm = (a * b) // temp
        
        while left < right:
            mid = (left + right) // 2

            count = (mid // a) + (mid // b) - (mid // lcm)

            if count < n:
                left = mid + 1
            else:
                right = mid

        return left % MOD