class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        we see 73 and add it to our stack (73, 0)
        we then see 74, which is greater than the top of our stack
        ans[0] = index of curr elem (1) - stack[-1][1] (0) = 1
        """
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                ans[index] = i - index
            stack.append(i)
        return ans
