from collections import deque
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordList.append(beginWord)
        wordDic = {}
        for word in wordList:
            for i in range(len(word)):
                s = word[:i] + "_" + word[i+1:]
                wordDic[s] = wordDic.get(s,[]) + [word]

        doneSet = set()
        q = deque()
        q.append((beginWord,1))
        while len(q) > 0:
            curr,steps= q.popleft()
            if curr == endWord:
                break
            for i in range(len(curr)):
                s = curr[:i] + "_" + curr[i+1:]
                next_words = wordDic.get(s,[])
                for next_word in next_words:
                    if next_word not in doneSet:
                        doneSet.add(next_word)
                        q.append((next_word,steps + 1))

        res = []
        doneSet = [beginWord]
        def dfs(currList):
            if len(currList) > steps: return
            currWord = currList[-1]
            for i in range(len(currWord)):
                s = currWord[:i] + "_" + currWord[i+1:]
                next_words = wordDic.get(s,[])
                for next_word in next_words:
                    if next_word not in doneSet:
                        doneSet.append(next_word)
                        currList.append(next_word)
                        if len(currList) == steps and next_word == endWord:
                            res.append(currList[:])
                        dfs(currList)
                        doneSet.remove(next_word)
                        currList.remove(next_word)
        dfs([beginWord])

        return res







so = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

beginWord="leet"
endWord="code"
wordList=["lest","leet","lose","code","lode","robe","lost"]
print(so.findLadders(beginWord,endWord,wordList))