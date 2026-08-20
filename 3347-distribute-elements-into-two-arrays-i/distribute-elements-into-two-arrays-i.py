class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr1=[]
        arr2=[]
        n=len(nums)
        left=0
        right=0
        arr1.append(nums[0])
        arr2.append(nums[1])
        for i in range(2,n):
            if arr1[left]>arr2[right]:
                arr1.append(nums[i])
                left+=1
            else:
                arr2.append(nums[i])
                right+=1
        return arr1+arr2

        