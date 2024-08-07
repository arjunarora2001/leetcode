class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        prefix = [1] * size
        postfix = [1] * size
        prefix[0] = nums[0]
        postfix[-1] = nums[-1]
        for i in range(1, size):
            prefix[i] = prefix[i - 1] * nums[i]
        for i in range(size - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i]
        ans = [1] * size
        ans[0] = postfix[1]
        ans[-1] = prefix[-2]
        for i in range(1, size - 1):
            ans[i] = prefix[i - 1] * postfix[i + 1]
        return ans

