from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        count = Counter(s)
    
        for i in range(n - 1, -1, -1):
            temp_count = count.copy()
            possible = True
            prefix = target[:i]
        
            for ch in prefix:
                if temp_count[ch] > 0:
                    temp_count[ch] -= 1
                else:
                    possible = False
                    break
                
            if not possible:
                continue
            
            next_char = None
            for c_code in range(ord(target[i]) + 1, ord('z') + 1):
                ch = chr(c_code)
                if temp_count[ch] > 0:
                    next_char = ch
                    break
                
            if next_char:
                temp_count[next_char] -= 1
                rest = []
                for c_code in range(ord('a'), ord('z') + 1):
                    ch = chr(c_code)
                    rest.append(ch * temp_count[ch])
                return prefix + next_char + "".join(rest)
            
        return ""
