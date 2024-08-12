class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # use a decision tree
        # for each value in nums, we can either add the next value or not add it
        # creates 2^n possibilites
        # CONSTRAINT: answer must not contain duplicate subsets
        # DFS down one branch: eg: 1, 2, 3
        # once we have a full set, we pop an element and perform dfs again
        ans = []
        tmp = []
        def dfs(num):
            # we can never add more than n elements to the array
            if num >= len(nums):
                ans.append(tmp.copy())
                return
            tmp.append(nums[num])
            dfs(num + 1)

            tmp.pop()
            dfs(num + 1)
        dfs(0)
        return ans