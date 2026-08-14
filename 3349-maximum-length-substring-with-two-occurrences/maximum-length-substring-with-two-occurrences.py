class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        char_counts = {}
        
        for right in range(len(s)):
            char_counts[s[right]] = char_counts.get(s[right], 0) + 1
            
            while char_counts[s[right]] > 2:
                char_counts[s[left]] -= 1
                left += 1
                
            max_len = max(max_len, right - left + 1)
            
        return max_len
