class Solution:
    def groupAnagrams(self, strs):
        setDic = {}
        for origin in strs:
            if("".join(sorted(origin)) in setDic):
                setDic["".join(sorted(origin))].append(origin)
            else:
                setDic["".join(sorted(origin))] = [origin]
        res = []
        for key,value in setDic.items():
            res.append(value)
        return res



        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
so = Solution()
print(so.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))