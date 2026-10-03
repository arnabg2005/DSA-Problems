class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        set1 = set()
        result = []
        for i in nums:
            set1.add(i)

        for i in range(1,len(nums)+1):
            if i not in set1:
                result.append(i)
        return result