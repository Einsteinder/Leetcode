
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        a={}
        b={}
        pb = headB
        while headA:
            a[id(headA)] = headA
            headA = headA.next
        print(a)
        for key,value in a.items():
            while pb:
                print(id(pb))
                if id(pb) == key:
                    print(pb.val)
                    return pb
                pb = pb.next
            pb = headB
        return None
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
c.next = a
a.next = b
e = c
f = c

so = Solution()
so.getIntersectionNode(e,e)