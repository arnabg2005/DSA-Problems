class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = []

        for i in range(len(s)):
            if s[i] == '1':
                ones.append(i)

        if len(ones) < k:
            return ""

        best = ""
        min_len = float('inf')

        for i in range(len(ones) - k + 1):
            left = ones[i]
            right = ones[i + k - 1]

            length = right - left + 1
            current = s[left:right + 1]

            if length < min_len:
                min_len = length
                best = current

            elif length == min_len and current < best:
                best = current

        return best