class Solution:
    def multiply(self, num1, num2):
        CHAR_DIGIT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        DIGIT_CHAR = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

        ans = ""
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                p1 = i + j
                p2 = i + j + 1
                res[p1] += (CHAR_DIGIT[num1[i]] * CHAR_DIGIT[num2[j]] + res[p2]) // 10
                res[p2] = (CHAR_DIGIT[num1[i]] * CHAR_DIGIT[num2[j]] + res[p2]) % 10
        for i in range(len(res)):
            if not (res[i] == 0 and len(ans) == 0):
                ans += DIGIT_CHAR[res[i]]
        if len(ans) == 0:
            return "0"
        return ans

        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
