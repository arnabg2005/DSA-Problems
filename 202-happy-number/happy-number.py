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

        ### 16     1

        lst = []
        while True: 
            res = square_fun(n)
            #print(f'res {res}')
            if res == 1:
                return True
                break
            else:
                if res in lst:
                    return False
                    break
                else:
                    lst.append(res)
                    n = res
        #print(lst)
