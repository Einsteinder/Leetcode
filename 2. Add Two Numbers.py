# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807.
	
nodeL1 = ListNode(2)
nodeL1.next = ListNode(4)
nodeL1.next.next = ListNode(3)

nodeL2 = ListNode(5)
nodeL2.next = ListNode(6)
nodeL2.next.next = ListNode(4)


class Solution:
	def addTwoNumbers(self, l1, l2):
		sum = 0
		result_node = ListNode(0)
		head_node = result_node
		while l1 or l2:
			sum = sum//10
			if l1:
				sum += l1.val
				l1 = l1.next
			if l2:
				sum += l2.val
				l2 = l2.next
			result_node.next = ListNode(sum%10)
			result_node = result_node.next
		if sum//10 == 1:
			result_node.next =ListNode(1)
		return head_node.next

so = Solution()
result = so.addTwoNumbers(nodeL1,nodeL2)
print(result.val)
print(result.next.val)
print(result.next.next.val)
print(result)