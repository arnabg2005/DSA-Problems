class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        m = n // 2
        
        # Step 1: Count frequencies
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1
            
        # Validate palindrome condition
        odd_count = 0
        mid_char = ""
        half_freq = [0] * 26
        
        for i in range(26):
            if freq[i] % 2 != 0:
                odd_count += 1
                mid_char = chr(ord('a') + i)
            half_freq[i] = freq[i] // 2
            
        if odd_count > 1:
            return ""

        def build_palindrome(half_list):
            first_half = "".join(half_list)
            second_half = first_half[::-1]
            return first_half + mid_char + second_half

        # Step 2: Try matching target prefix of length L from m down to 0
        for L in range(m, -1, -1):
            # Check if target[0...L-1] can be formed from half_freq
            curr_freq = list(half_freq)
            possible = True
            prefix = []
            
            for i in range(L):
                idx = ord(target[i]) - ord('a')
                if curr_freq[idx] > 0:
                    curr_freq[idx] -= 1
                    prefix.append(target[i])
                else:
                    possible = False
                    break
            
            if not possible:
                continue

            # Case 1: Full match of first half (L == m)
            if L == m:
                cand = build_palindrome(prefix)
                if cand > target:
                    return cand
                continue

            # Case 2: L < m, place a character strictly greater than target[L] at index L
            target_char_idx = ord(target[L]) - ord('a')
            for c_idx in range(target_char_idx + 1, 26):
                if curr_freq[c_idx] > 0:
                    # Place c_idx at position L
                    temp_freq = list(curr_freq)
                    temp_freq[c_idx] -= 1
                    
                    candidate_half = list(prefix)
                    candidate_half.append(chr(ord('a') + c_idx))
                    
                    # Fill the remaining m - L - 1 positions with smallest available chars
                    for rem_idx in range(26):
                        while temp_freq[rem_idx] > 0:
                            candidate_half.append(chr(ord('a') + rem_idx))
                            temp_freq[rem_idx] -= 1
                            
                    cand = build_palindrome(candidate_half)
                    if cand > target:
                        return cand
                        
        return ""