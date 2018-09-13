# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        def helper(mi, ma):
            res = []
            if mi > ma:
                return res
            for root in range(mi, ma + 1):
                leftList = helper(mi, root - 1)
                rightList = helper(root + 1, ma)
                if not leftList and not rightList:
                    res.append(TreeNode(root))
                elif not leftList:
                    for rnode in rightList:
                        rootNode = TreeNode(root)
                        rootNode.right = rnode
                        res.append(rootNode)
                elif not rightList:
                    for lnode in leftList:
                        rootNode = TreeNode(root)
                        rootNode.left = lnode
                        res.append(rootNode)
                else:
                    for lnode in leftList:
                        for rnode in rightList:
                            rootNode = TreeNode(root)
                            rootNode.left = lnode
                            rootNode.right = rnode
                            res.append(rootNode)
            return res

        return helper(1, n)

        """
        :type n: int
        :rtype: List[TreeNode]
        """
