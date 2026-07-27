class Solution(object):
    def maxArea(self, height):
        left=0
        right=len(height)-1
        maxi=0
        while left<right:
            width=right-left
            current_height=min(height[left],height[right])
            area=width*current_height
            maxi=max(maxi,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxi
        