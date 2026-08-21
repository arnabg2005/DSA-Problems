class Solution(object):
    def addStrings(self, num1, num2):
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        ans = ""

        while i >= 0 or j >= 0:
            a = int(num1[i]) if i >= 0 else 0
            b = int(num2[j]) if j >= 0 else 0

            total = a + b + carry

            ans = str(total % 10) + ans
            carry = total // 10

            i -= 1
            j -= 1

        if carry:
            ans = "1" + ans

        return ans