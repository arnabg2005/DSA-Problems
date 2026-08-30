class Solution(object):
    def minimumDeletions(self, nums):

        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        a = min(min_index, max_index)
        b = max(min_index, max_index)

        front = b + 1
        back = n - a
        both = (a + 1) + (n - b)

        return min(front, back, both)