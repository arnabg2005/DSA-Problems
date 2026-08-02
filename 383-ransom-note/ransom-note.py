class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        freq = {}

        # Count characters in magazine
        for ch in magazine:
            freq[ch] = freq.get(ch, 0) + 1

        # Use characters for ransom note
        for ch in ransomNote:

            if freq.get(ch, 0) == 0:
                return False

            freq[ch] -= 1

        return True