# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        ret = dummy
        while dummy.next and dummy.next.next:
            curr = dummy.next
            after = curr.next
            temp = after.next
            dummy.next = after
            after.next = curr
            curr.next = temp
            
            dummy = dummy.next.next
        return ret.next
