# In the discussion, people are arguing about "is reverse() considered as o(1)"
# Yes I think so...
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """     
        slow = head
        fast = head
        rev = None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = rev
            rev = slow
            slow = temp
        if fast:
            slow = slow.next
        
        while slow!=None and rev!=None:
            if(rev.val != slow.val):
                return False
            rev = rev.next
            slow = slow.next
        return True
