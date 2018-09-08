class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        def dfs(sortedNums, currIndex, length):
            if currIndex == len(sortedNums) - 1:
                return length, currIndex
            if sortedNums[currIndex] + 1 == sortedNums[currIndex + 1]:
                length += 1
                currIndex += 1
                return dfs(sortedNums, currIndex, length)
            elif sortedNums[currIndex] == sortedNums[currIndex + 1]:
                currIndex += 1
                return dfs(sortedNums, currIndex, length)

            else:
                return length, currIndex

        maxLength = 0
        i = 0
        d = collections.Counter()
        while i < len(nums):
            length, i = dfs(sorted(nums), i, 0)
            d[i] += 1
            for item in d.values():
                if item > 1:
                    i += 1
            maxLength = max(length, maxLength)

        return maxLength + 1