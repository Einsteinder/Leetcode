class Solution:
    def minDistance(self, word1, word2):
        matrix = []
        for i in range(len(word1)+1):
            newRow = []
            for j in range(len(word2)+1):
                if j == 0:
                    newRow.append(i)
                elif i == 0:
                    newRow.append(j)
                else:
                    newRow.append(0)
            matrix.append(newRow)
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if word1[i-1] == word2[j-1]:
                    matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j] + 1,matrix[i][j-1] + 1)
                else:
                    matrix[i][j] = min(matrix[i-1][j-1] + 1, matrix[i-1][j] + 1,matrix[i][j-1] + 1)


        return matrix[-1][-1]






        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
word1 = "horse"
word2 = "ros"
so = Solution()
print(so.minDistance(word1,word2))