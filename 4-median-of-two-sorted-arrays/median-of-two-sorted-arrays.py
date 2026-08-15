class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        '''new=nums1+nums2
        new=sorted(new)
        median=np.median(new)
        return median'''
        merge_array=sorted(nums1+nums2)
        lenght=len(merge_array)
        idx=lenght//2
        if lenght%2==0:
            return (merge_array[idx-1]+merge_array[idx])/2.0
        else:
            return merge_array[idx]
        