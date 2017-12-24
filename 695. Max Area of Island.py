
xgrid=[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]


class Solution(object):
    def maxAreaOfIsland(self, grid):
        seen = set()
        maxCount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count = self.checkToZero(grid,i,j,seen)
                if count > maxCount:
                    maxCount = count

        return maxCount

    def checkToZero(self,grid,x,y,seen):
        

        if x>=len(grid) or x<0 or y>= len(grid[0]) or y<0:return 0    
        if not (grid[x][y] and (0<= x <len(grid)) and (x,y) not in seen and (0<= y< len(grid[0]))):

            return 0           

        else:
            seen.add((x,y))
            return 1+self.checkToZero(grid,x+1,y,seen)+self.checkToZero(grid,x-1,y,seen)+self.checkToZero(grid,x,y+1,seen)+self.checkToZero(grid,x,y-1,seen)
x = Solution()
result=x.maxAreaOfIsland(xgrid)
print(result)
        