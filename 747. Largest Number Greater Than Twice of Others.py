nums = [3, 6, 1, 0]
class Solution:
	def dominantIndex(self, nums):
		maxNumber = max(nums)
		index = nums.index(maxNumber)
		nums.remove(maxNumber)
		for item in nums:
			if maxNumber < 2*item:
				return -1
		return index

x = Solution()
print(x.dominantIndex(nums))