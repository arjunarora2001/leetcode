class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        for i in range(len(s) - 1):
            if mapping[s[i]] < mapping[s[i + 1]]:
                num -= mapping[s[i]]
            else:
                num += mapping[s[i]]
        return num + mapping[s[-1]]