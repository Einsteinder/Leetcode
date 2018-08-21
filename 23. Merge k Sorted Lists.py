# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        def combineList(lists):
            tempDic = {}
            for key,linkedList in enumerate(lists):
                tempDic[key] = []
                if linkedList:
                    tempDic[key].append(linkedList.val)
                    while linkedList.next:
                        tempDic[key].append(linkedList.next.val)
                        linkedList = linkedList.next
            print(tempDic)
            combinedList = []
            for key,list in tempDic.items():
                combinedList += list
            if combinedList:
                combinedList.sort()
            print(combinedList)
            return combinedList

        combineList = combineList(lists)
        newHead = ListNode(0)
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
print(so.mergeKLists([]))