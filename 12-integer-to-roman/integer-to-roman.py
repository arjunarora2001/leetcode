class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        while num >= 1000:
            num -= 1000
            ans += 'M'
        # if num between 900 and 999, add CM and reduce by 900
        if num >= 900:
            num -= 900
            ans += 'CM'
        while num >= 500:
            num -= 500
            ans += 'D'
        # if num between 400 and 499, add CD and reduce by 400
        if num >= 400:
            num -= 400
            ans += 'CD'
        while num >= 100:
            num -= 100
            ans += 'C'
        # if num between 90 and 99, add XC and reduce by 90
        if num >= 90:
            num -= 90
            ans += 'XC'
        while num >= 50:
            num -= 50
            ans += 'L'
        # if num between 40 and 49, add XL and reduce by 40
        if num >= 40:
            num -= 40
            ans += 'XL'
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
        