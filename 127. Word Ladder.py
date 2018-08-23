import queue as queue
class Solution:

    def diff(self,w1,w2):
        count = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                count += 1
        return count

    def ladderLength(self, beginWord, endWord, wordList):
        wordDic = {}
        for word in wordList:
            wordDic[word] = []
            for theOther in wordList:
                if self.diff(word,theOther) == 1:
                    wordDic[word].append(theOther)
        wordDic[beginWord] = []
        for theOther in wordList:
            if self.diff(beginWord, theOther) == 1:
                wordDic[beginWord].append(theOther)
        print(wordDic)
        doneSet = set()
        steps = 1
        q = queue.Queue()
        q.put(beginWord)
        while q.qsize() > 0:
            size = q.qsize()
            for i in range(size):
                curr = q.get()
                if curr == endWord:
                    return steps
                for word in wordDic[curr]:
                    if word not in doneSet:
                        q.put(word)
                        doneSet.add(word)
            steps += 1

        return 0

so = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

beginWord="leet"
endWord="code"
wordList=["lest","leet","lose","code","lode","robe","lost"]
print(so.ladderLength(beginWord,endWord,wordList))