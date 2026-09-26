# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        lst = []
        temp = head
        while temp is not None:
            lst.append(temp.val)
            temp = temp.next
        
        left = 0
        right = len(lst)-1
        max_element = -9999
        while left < right:
            total = lst[left] + lst[right]
            if total > max_element:
                max_element = total
            left += 1
            right -= 1
        return max_element

        