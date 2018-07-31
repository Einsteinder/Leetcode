class Solution:
    def search(self, nums, target):
        if len(nums) == 1:
            if target == nums[0]:
                return 0
        lo = 0
        hi = len(nums)-1
        while lo < hi:
            mi = (lo + hi) // 2
            if nums[mi] > nums[hi]:
                lo = mi + 1
            else:
                hi = mi

        ro = lo
        lo = 0
        hi = len(nums)-1
        while lo <= hi:
            mi = (lo + hi) // 2
            realMi = (mi + ro) % len(nums)
            if nums[realMi] == target:
                return realMi
            if nums[realMi] < target:
                lo = mi + 1
            else:
                hi = mi - 1
        return -1

so = Solution()
print(so.search([1, 3], 1))
print(so.search([4,5,6,7,0,1,2],0))