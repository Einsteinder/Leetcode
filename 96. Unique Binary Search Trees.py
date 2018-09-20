# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def numTrees(self, n):
        dp = [1]
        for i in range(1, n + 1):
            res = 0
            for j in range(i):
                res += dp[j] * dp[i - 1 - j]
            dp.append(res)
        return dp[-1]

