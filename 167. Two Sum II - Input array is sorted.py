class Solution:
    def twoSum(self, numbers, target):
    	for i in range(len(numbers)):
    		difference = target - numbers[i]
    		for j in range(len(numbers[i+1:])):
    			if numbers[i+1:][j]==difference:
    				return (i+1,i+1+j+1)

x = Solution()
print(x.twoSum([2,7,3,4],9))


        