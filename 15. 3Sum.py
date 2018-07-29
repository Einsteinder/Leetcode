class Solution(object):
    def threeSum(self, nums):
        sortedNums = sorted(nums)
        result = []
        for i in range(len(sortedNums) - 2):
            j = i + 1
            k = len(sortedNums) - 1
            sumOfTwo = 0 - sortedNums[i]
            if i == 0 or sortedNums[i] != sortedNums[i - 1]:
                while j < k:
                    if sortedNums[j] + sortedNums[k] == sumOfTwo:
                        result.append([sortedNums[i], sortedNums[j], sortedNums[k]])
                        while (j < k and sortedNums[j] == sortedNums[j + 1]):
                            j += 1
                        while (j < k and sortedNums[k] == sortedNums[k - 1]):
                            k -= 1
                        j += 1
                    elif sortedNums[j] + sortedNums[k] < sumOfTwo:
                        j += 1
                    else:
                        k -= 1
        return list(result)

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

so = Solution()
print(so.threeSum([-1, 0, 1, 2, -1, -4]))


