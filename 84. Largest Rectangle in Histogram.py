import sys
class Solution:
    def largestRectangleArea(self, heights):
        if not heights:
            return 0
        maxArea = 0
        for i in range(len(heights)):
            minHeight = sys.maxsize
            if i == len(heights) - 1 or heights[i] > heights[i + 1]:
                for j in range(i, -1, -1):
                    minHeight = min(minHeight, heights[j])
                    maxArea = max(maxArea, (i - j + 1) * minHeight)
        return maxArea

        """
        :type heights: List[int]
        :rtype: int
        """
