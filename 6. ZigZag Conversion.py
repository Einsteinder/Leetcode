class Solution:
    def convert(self, s, numRows):
        table = []
        column = (len(s) // (numRows * 2 - 2)) * (numRows - 1) + 1 + (len(s) % (numRows * 2 - 2)) % numRows \
            if len(s) % (numRows * 2 - 2) > numRows \
            else (len(s) // (numRows * 2 - 2)) * (numRows - 1) + 1
        for i in range(numRows):
            tableRow=[]
            for j in range(column):
                tableRow.append(0)
            table.append(tableRow)
        orderList = []
        for j in range(len(table[0])):
            if j % (numRows-1) == 0:
                for k in range(numRows):
                    orderList.append([k,j])
            else:
                orderList.append([numRows-1-(j % (numRows-1)),j ])
        print(orderList)
        generateOrder = (order for order in orderList)

        for c in s:
            x,y = next(generateOrder)
            print(x,y)
            table[x][y]=c
        newString = ""
        for subList in table:
            for item in subList:
                if item != 0:
                    newString+=item

        return newString
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

so = Solution()
print(so.convert("PAYPALISHIRING",1))