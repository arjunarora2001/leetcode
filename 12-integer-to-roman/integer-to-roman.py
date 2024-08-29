class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        # while num > 0:
            # this works easily since the maximum number is 3999
        while num >= 1000:
            num -= 1000
            ans += 'M'
        # now num is 749
        # if num between 900 and 999, add CM and reduce by 900
        while num >= 900 and num <= 999:
            num -= 900
            ans += 'CM'
        while num >= 500:
            num -= 500
            ans += 'D'
        # if num between 400 and 499, add CD and reduce by 400
        while num >= 400 and num <= 499:
            num -= 400
            ans += 'CD'
        # now num is 249
        while num >= 100:
            num -= 100
            ans += 'C'
        # now num is 49
        # if num between 90 and 99, add XC and reduce by 90
        while num >= 90 and num <= 99:
            num -= 90
            ans += 'XC'
        # if num between 40 and 49, add XL and reduce by 40
        while num >= 40 and num <= 49:
            num -= 40
            ans += 'XL'
        while num >= 50:
            num -= 50
            ans += 'L'
        while num >= 10:
            num -= 10
            ans += 'X'
        # if num is 9
        if num == 9:
            num -= 9
            ans += 'IX'
            return ans
        while num >= 5:
            num -= 5
            ans += 'V'
        # if num is 4
        if num == 4:
            num -= 4
            ans += 'IV'
            return ans
        while num >= 1:
            num -= 1
            ans += 'I'
        return ans
        