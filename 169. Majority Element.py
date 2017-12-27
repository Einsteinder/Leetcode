class Solution:
    def majorityElement(self, nums):
    	itemDic={}
    	for item in nums:
    		if item in itemDic:
    			itemDic[item]+=1
    		else:
    			itemDic[item]=1
    	return max(itemDic.items(), key=lambda x:x[1])[0]
x = Solution()
print(x.majorityElement([1]))


        