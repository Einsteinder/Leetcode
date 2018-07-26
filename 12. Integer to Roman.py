class Solution:
    def intToRoman(self, num):
        str1 = "M" * (num // 1000)
        if num % 1000 // 100 != 9 and num % 1000 // 100 != 4:
            str2 = "D" * (num % 1000 // 500)
        elif num % 1000 // 100 == 9:
            str2 = "CM"
        elif num % 1000 // 100 == 4:
            str2 = "CD"
        else:
            str2 = "C" * (num % 1000 % 500 // 100)

        if num % 1000 % 500 % 100 // 10 != 9 and num % 1000 % 500 % 100 // 10 != 4:
            str3 = "L" * (num % 1000 % 500 % 100 // 50)
        elif num % 1000 % 500 % 100 // 10 == 9:
            str3 = "XC"
        elif num % 1000 % 500 % 100 // 10 == 4:
            str3 = "XL"
        else:
            str3 = "X" * (num % 1000 % 500 % 100 % 50 // 10)

        if num % 1000 % 500 % 100 % 10 != 9 and num % 1000 % 500 % 100 % 10 != 4:
            str4 = "V" * (num % 1000 % 500 % 100 % 50 % 10 // 5)
        elif num % 1000 % 500 % 100 % 10 == 9:
            str4 = "IX"
        elif num % 1000 % 500 % 100 % 10 == 4:
            str4 = "IV"
        else:
            str4 = "I" * (num % 1000 % 500 % 100 % 50 % 10 % 5)
        return str1 + str2 + str3 + str4
so = Solution()
print(so.intToRoman(1994))
