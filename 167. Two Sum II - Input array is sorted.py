class Solution:
	def twoSum(self, numbers, target):
		differenceList = []
		for i in range(len(numbers)):
			difference = target - numbers[i]
			differenceList.append(difference)
		otherElement = set(differenceList)&set(numbers)
		otherElement = list(otherElement)
		otherRealElement=[]
		print("other",otherElement)
		for item in otherElement:
			if item == target/2:
				if numbers.count(item)==1:
					continue
				else:
					otherRealElement.append(item)
			print("oteer",otherRealElement)
			otherRealElement.append(item)

		result = []
		count = 0
		otherRealElement.sort()
		print(otherRealElement)

		for item in otherRealElement:

			print("number",numbers)
			result.append(numbers.index(item)+count)
			print("item",item)
			print("numbers.index(item)",numbers.index(item))
			print("count",count)
			print("result",result)
			numbers.remove(item)
			count+=1

		return [x+1 for x in result]




x = Solution()
print(x.twoSum([0,4,0,4],0))


        