class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        even=0
        odd=0
        for i in nums1:
            if i%2==0:
                even += 1
            else:
                odd += 1
        if even == len(nums1) or odd == len(nums1):
            return True
        if even > 0 and odd > 0:
            return True
            
        return False


