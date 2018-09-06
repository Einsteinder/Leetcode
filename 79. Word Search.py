class Solution:
    def exist(self, board, word):
        def dfs(x, y, b, curr, w, index):

            if x < 0 or x == len(b)or y < 0 or y ==len(b[x]):
                return False
            if w[index] == b[x][y]:
                curr += b[x][y]
                print(curr)
                if curr == w:
                    return True
                else:
                    curWord = b[x][y]
                    b[x][y] = 0
                    res = dfs(x + 1, y, b, curr, w, index + 1) or\
                    dfs(x - 1, y, b, curr, w, index + 1) or \
                    dfs(x, y - 1, b, curr, w, index + 1) or \
                    dfs(x, y + 1, b, curr, w, index + 1)
                    b[x][y] = curWord
                    return res
            else:
                return False

        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(i, j, board, "", word, 0):
                    return True

        return False

        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
board =\
[
  ['a','b']
]

word = "ba"
so = Solution()
print(so.exist(board,word))