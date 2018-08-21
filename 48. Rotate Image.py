class Solution:
    def rotate(self, matrix):
        newMatrix = []
        for i in range(len(matrix)):
            subRow = []
            for j in range(len(matrix[0])):
                subRow.append(0)
            newMatrix.append(subRow)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                newMatrix[j][len(matrix[0])-i-1] = matrix[i][j]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = newMatrix[i][j]
        return matrix
so=Solution()
print(so.rotate([
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]))

