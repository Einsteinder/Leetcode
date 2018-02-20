nums1 = [1, 2]
nums2 = [3, 4]
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
    	newList = nums1+nums2
    	newList.sort()
    	if len(newList)%2:
    		return newList[len(newList)//2]
    	else:
    		return 1/2*(newList[int(len(newList)/2)]+newList[int(len(newList)/2)-1])

so = Solution()
print(so.findMedianSortedArrays(nums1,nums2))