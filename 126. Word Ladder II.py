class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        self.res = []
        if endWord not in wordList:
            return []
        length = len(beginWord)
        curr = beginWord
        path = [curr]

        for word in wordList:
            if length - len(list(word) and curr) == 1:
                curr = word
                path.append(curr)
            if word == endWord:
                self.res.append(path)
                


        def move(curr,wordL,end,res):
            for word in wordL:
                temp = []
                    temp.append(word)
            if len(temp) > 1:
                self.res.append()
            for word in temp:
                if word == end:
                    return res
                else:
                    self.res.append(word)
                    move(word,wordL)




        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
