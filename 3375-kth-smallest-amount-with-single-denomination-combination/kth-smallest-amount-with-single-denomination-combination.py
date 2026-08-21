class Solution(object):
    def findKthSmallest(self, coins, k):

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return (a * b) // gcd(a, b)

        def count(x):
            total = 0
            n = len(coins)

            for mask in range(1, 1 << n):
                multiple = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        multiple = lcm(multiple, coins[i])
                        bits += 1

                if bits % 2 == 1:
                    total += x // multiple
                else:
                    total -= x // multiple

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) < k:
                left = mid + 1
            else:
                right = mid

        return left