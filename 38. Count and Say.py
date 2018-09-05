from collections import OrderedDict
class Solution:
    def countAndSay(self, n):
        seq = '1'
        for _ in range(n-1):
            first = seq[0]
            count = 0
            temp = ""

            for i in seq:
                if i == first:
                    count += 1
                else:
                    temp += str(count)
                    temp += first
                    first = i
                    count =1
            temp += str(count) + first
            seq = temp
        return seq




so = Solution()
print(so.countAndSay(10))