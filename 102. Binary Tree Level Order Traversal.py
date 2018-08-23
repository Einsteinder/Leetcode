# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        self.level = 0
        if root:
            self.res = [[root.val]]
        else:
            return []
        def checkNode(node):
            self.level += 1
            self.res.append([])
            if node.left:
                self.res[self.level].append(node.left.val)
                checkNode(node.left)
            if node.right:
                self.res[self.level].append(node.right.val)
                checkNode(node.right)
            if not self.res[-1]:
                self.res.pop()
            self.level -= 1

        checkNode(root)
        return self.res
inputNode = TreeNode(3)
inputNode.left =TreeNode(9)
inputNode.right =TreeNode(20)
inputNode.right.left=TreeNode(15)
inputNode.right.right=TreeNode(7)
so = Solution()
print(so.levelOrder(inputNode))







