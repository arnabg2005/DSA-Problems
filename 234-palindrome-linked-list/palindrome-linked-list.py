class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head):
        temp = []
        start = head
        while start is not None:
            temp.append(start.val)
            start = start.next
        left = 0
        right = len(temp) - 1
        while left < right:
            if temp[left] != temp[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
