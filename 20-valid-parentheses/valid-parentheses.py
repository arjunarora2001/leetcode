class Solution:
    def isValid(self, s: str) -> bool:
        # Tests:
        # (([]))
        # (({[]}))
        stack = deque()
        # traverse through all the characters in the string
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                match i:
                    case ')':
                        if stack[-1] == '(':
                            stack.pop()
                        else:
                            return False 
                    case '}':
                        if stack[-1] == '{':
                            stack.pop()
                        else:
                            return False 
                    case ']':
                        if stack[-1] == '[':
                            stack.pop()
                        else:
                            return False 
                    case _:
                        return False
        return len(stack) == 0
