# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        if head == None: return None

        temp = head
        while temp:
            newNode = RandomListNode(temp.label)
            newNode.next = temp.next

            temp.next = newNode
            temp = temp.next.next

        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next

        oldHead = head
        newHead = head.next
        returnHead = head.next

        while newHead.next:
            oldHead.next = newHead.next
            oldHead = oldHead.next
            newHead.next = oldHead.next
            newHead = newHead.next
        oldHead.next = None
        newHead.next = None
        return returnHead

        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """