class Solution:
    def isPalindrome(self, x):
        before = str(x)
        after = before[::-1]
        if before == after:
            return True
        else:
            return False

so = Solution()
print(so.isPalindrome(10))