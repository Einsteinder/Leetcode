class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = abs((nums[0] + nums[1] + nums[2]) - target)
        answer = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            low = i + 1
            high = len(nums) - 1
            while low < high:
                if abs((nums[i] + nums[low] + nums[high]) - target) <= result:
                    result = abs((nums[i] + nums[low] + nums[high]) - target)
                    answer = nums[i] + nums[low] + nums[high]
                if nums[i] + nums[low] + nums[high] > target:
                    high -= 1
                else:
                    low += 1
        return answer


so = Solution()
print(so.threeSumClosest([0, 2, 1, -3], 1))