class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq={}
        for ch in s:
            s_freq[ch] = s_freq.get(ch,0)+1
        t_freq={}
        for ch in t:
            t_freq[ch] = t_freq.get(ch,0)+1
        return s_freq==t_freq
