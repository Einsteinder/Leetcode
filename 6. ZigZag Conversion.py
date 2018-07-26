class Solution:
    def convert(self, s, numRows):
        if numRows==1:
            return s
        row = []
        for i in range(min(numRows,len(s))):
            row.append("")
        goingDown = False
        curRow = 0
        for c in s:
            row[curRow] += c
            if curRow == 0 or curRow == numRows-1:
                goingDown = not goingDown
            curRow += 1 if goingDown else -1
        return "".join(row)


so = Solution()
print(so.convert("PAYPALISHIRING",3))