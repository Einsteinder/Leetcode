import sys
"""
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
class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        maxArea = 0
        i = 0
        while i < len(heights):
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                if not stack:
                    area = heights[top] * i
                else:
                    area = heights[top] * (i - stack[-1] -1)
                maxArea = max(maxArea,area)
        while stack:
            top = stack.pop()
            if not stack:
                area = heights[top] * i
            else:
                area =heights[top] * (i - stack[-1] - 1)
            maxArea = max(maxArea,area)
        return maxArea



so = Solution()
print(so.largestRectangleArea([2,1,5,6,2,3]))