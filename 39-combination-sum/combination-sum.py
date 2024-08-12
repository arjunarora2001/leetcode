class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        size = len(candidates)
        def dfs(i, currSum, tmp):
            if currSum > target or i >= size:
                return
            if currSum == target:
                ans.append(tmp.copy())
                return
            # currSum < target
            tmp.append(candidates[i])
            dfs(i, currSum + candidates[i], tmp)
            tmp.pop()
            dfs(i + 1, currSum, tmp)
        
        dfs(0, 0, [])
        return ans