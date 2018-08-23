class Solution:
    def subsets(self, nums):
        self.res = []
        def dfs(nums,index,temp):
            self.res.append(temp[:])
            for i in range(index,len(nums)):
                temp.append(nums[i])
                dfs(nums,i+1,temp)
                temp.pop()
        dfs(nums,0,[])
        return self.res

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
so = Solution()
print(so.subsets([1,2,3]))