import numpy as np
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        new=nums1+nums2
        new=sorted(new)
        median=np.median(new)
        return median

        
        