li = [0,1,0,2,1,0,1,3,2,1,2,1]
"""

x = li.index(2)
print(x)
reversedLi = list(reversed(li))
print(reversedLi)
y = reversedLi.index(2)
print(y)
lastIndex = len(li)-1-y
print(lastIndex)
print(li[lastIndex])
"""
#return 6.

class Solution(object):
    def trap(self, height):
        total=0
        rightBarList = []
        leftBarlist =[]
        for i in range(len(height)):
        	rightBar = max(height[i:])
        	rightBarList.append(rightBar)
        for i in range(len(height)):
        	leftbar = max(list(reversed(height))[i:])
        	leftBarlist.append(leftbar)
        leftBarlist = list(reversed(leftBarlist))

        for i in range(len(height)):
        	if height[i]< min(leftBarlist[i],rightBarList[i]):
        		total+=min(leftBarlist[i],rightBarList[i])-height[i]
        return total



so=Solution()
print(so.trap(li))


       