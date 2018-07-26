class Solution:
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        maxArea = 0
        while i < j:
            maxArea = max((j-i) * min(height[i], height[j]), maxArea)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxArea
        """
        :type height: List[int]
        :rtype: int
        """
so = Solution()
print(so.maxArea([1,8,6,2,5,4,8,3,7]))