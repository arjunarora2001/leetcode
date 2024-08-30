class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if not stack:
                    return False
                bracket = stack.pop()
                match bracket:
                    case '(':
                        if i != ')':
                            return False
                    case '{':
                        if i != '}':
                            return False
                    case '[':
                        if i != ']':
                            return False
                    case _:
                        return False
        
        return not stack