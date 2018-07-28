class Solution:
    def threeSum(self, nums):
        result = []
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append(tuple(sorted([nums[i], nums[j], nums[k]])))
        return list(set(result))

so = Solution()
print(so.threeSum([-1, 0, 1, 2, -1, -4]))


