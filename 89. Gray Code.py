class Solution:
    def grayCode(self, n):
        res = [0]
        for i in range(n):
           size = len(res)
           for j in range(size-1,-1,-1):
               res.append(res[j] | 1<<i)
        return res

so = Solution()
print(so.grayCode(2))

