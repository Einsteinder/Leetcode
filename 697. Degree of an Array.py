Input = [1,2,2,3,1,4,2]
Input1 = [1, 2, 2, 3, 1]

class Solution:
	def findShortestSubArray(self, nums):
		modeDic = {}
		for item in nums:
			if item in modeDic:
				modeDic[item]+=1
			else:
				modeDic[item] = 1

		rankItems = sorted(modeDic.items(),key=lambda x:x[1],reverse=True)
		firstLenth = rankItems[0][1]
		modeList = []
		for x, y in rankItems:
			if y ==firstLenth:
				modeList.append(x)
		minCount = float("infinity")
		for mode in modeList:
			print(len(nums)-1-nums[::-1].index(mode),nums.index(mode))
			count = len(nums)-1-nums[::-1].index(mode)-nums.index(mode)
			if count < minCount:
				minCount = count
		return minCount+1

x = Solution()
print(x.findShortestSubArray(Input))

        