# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head:
            return False
        slow = head
        fast = head.next
        while fast:
            if not fast.next: return False
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

        """
        :type head: ListNode
        :rtype: bool
        """