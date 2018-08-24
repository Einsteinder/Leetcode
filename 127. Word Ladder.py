from collections import deque
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
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
                return steps
            for i in range(len(curr)):
                s = curr[:i] + "_" + curr[i+1:]
                next_words = wordDic.get(s,[])
                for next_word in next_words:
                    if next_word not in doneSet:
                        doneSet.add(next_word)
                        q.append((next_word,steps + 1))

        return 0


