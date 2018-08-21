# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None



class Solution:
    def mergeTwoLists(self, l1, l2):
        list1 = []
        list2 = []
        if l1:
            list1.append(l1.val)
            while l1.next:
                list1.append(l1.next.val)
                l1 = l1.next
        if l2:
            list2.append(l2.val)
            while l2.next:
                list2.append(l2.next.val)
                l2 = l2.next

        combineList = list1 + list2
        if combineList:
            combineList.sort()
        newHead = ListNode(0)
        print(combineList)
        temp = newHead
        if combineList:
            for i in range(0,len(combineList)):
                temp.next = ListNode(combineList[i])
                temp = temp.next
        return newHead.next


        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
l1 = ListNode(1)
l1.next=ListNode(2)
l1.next.next=ListNode(4)
l2 = ListNode(1)
l2.next=ListNode(3)
l2.next.next=ListNode(4)
so=Solution()
print(so.mergeTwoLists(l1,l2).val)