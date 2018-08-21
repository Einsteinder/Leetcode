class Solution:
    def setZeroes(self, matrix):
        zeroXIndex = {}
        zeroYIndex = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroXIndex[i] = 1
                    zeroYIndex[j] = 1
        for i in range(len(matrix)):
            for y in zeroYIndex:
                matrix[i][y] = 0

        for x in zeroXIndex:
            for j in range(len(matrix[0])):
                matrix[x][j] = 0
        return matrix
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
so = Solution()
print(so.setZeroes([
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]))