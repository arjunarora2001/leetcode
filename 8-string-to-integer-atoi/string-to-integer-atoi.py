class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        incrementer = 0
        while incrementer < len(s) and s[incrementer] == ' ':
            incrementer += 1
        isNegative = False
        if incrementer < len(s) and s[incrementer] == '-':
            isNegative = True
            incrementer += 1
        if not isNegative:
            if incrementer < len(s) and s[incrementer] == '+':
                incrementer += 1
        while incrementer < len(s) and s[incrementer] == '0':
            incrementer += 1
        
        ans = ""
        for i in range(incrementer, len(s)):
            if not s[i].isalnum():
                break
            elif ord(s[i]) >= 48 and ord(s[i]) <= 57:
                ans += s[i]
            else:
                break
        if isNegative:
            if ans:
                if int(ans) > 2147483648:
                    return -2147483648
                return -1 * int(ans)
            return 0
        else:
            if ans:
                if int(ans) > 2147483647:
                    return 2147483647
                return int(ans)
            return 0
        return 0
