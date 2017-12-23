import sys
sys.setrecursionlimit(1500)


xgrid1=[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

xgrid=[[0,0,1,1,1,0,0]]
class Solution(object):
    def maxAreaOfIsland(self, grid):
        maxCount = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                count = self.checkToZero(grid,i,j)
                if count > maxCount:
                    maxCount = count
                print(count)
        return maxCount

    def checkToZero(self,grid,x,y):
        count = 0
        print("x:",x,"y:",y)
        if grid[x][y]:
            count+=1
            count += self.checkToZero(grid,x,y-1)
            count += self.checkToZero(grid,x,y+1)
            count += self.checkToZero(grid,x+1,y)
            count += self.checkToZero(grid,x-1,y)
            return count            

        else:
            return count


x = Solution()
result=x.maxAreaOfIsland(xgrid)
print(result)
        