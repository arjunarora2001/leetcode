class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        size = len(candidates)
        def dfs(index: int, arr: List[int], total: int):
            if index >= size or total > target:
                return False
            elif total == target:
                res.append(arr.copy())
                return True
            arr.append(candidates[index])
            dfs(index, arr, total + candidates[index])
            arr.pop()
            dfs(index + 1, arr, total)
        dfs(0, [], 0)
        return res