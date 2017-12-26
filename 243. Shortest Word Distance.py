words = ["practice", "makes", "perfect", "coding", "makes"]
class Solution:
	def shortestDistance(self, words, word1, word2):
		word1Index=[]
		word2Index=[]
		miniLenth = float("infinity")
		for i in range(len(words)):
			if words[i] == word1:
				word1Index.append(i)
			if words[i] == word2:
				word2Index.append(i)
		for j in word1Index:
			for k in word2Index:
				if abs(j - k)<miniLenth:
					miniLenth = abs(j - k)
		return miniLenth
x = Solution()
print(x.shortestDistance(words,"makes","coding"))