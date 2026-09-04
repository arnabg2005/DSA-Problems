class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count=0
        nums.sort()
        i = 0
        j=len(nums)-1
        while i<j:
            sumi = nums[i] + nums[j]
            if sumi<target:
                count += (j-i)
                i +=1
            else:
                j-=1
        return count