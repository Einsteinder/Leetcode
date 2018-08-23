class Solution:
    def getRow(self, rowIndex):
        a = [1]
        for x in range(rowIndex):
            a.append(0)
        for i in range(rowIndex+1):
            for j in range(i,0,-1):
                a[j] += a[j-1]
        return a
so = Solution()
print(so.getRow(3))

