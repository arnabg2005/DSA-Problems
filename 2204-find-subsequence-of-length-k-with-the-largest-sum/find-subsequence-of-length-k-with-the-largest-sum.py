class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        paired = list(enumerate(nums))
        top_k = sorted(paired,key=lambda x:x[1],reverse=True)[:k]
        top_k.sort(key = lambda x : x[0])
        return [val for idx,val in top_k]
        