class Solution:
    def maxArea(self, height: List[int]) -> int:
        # BRUTE FORCE: O(n^2)
        # Two-Pointers: O(n)
        maxArea = 0
        start = 0
        end = len(height) - 1
        while start < end:
            maxArea = max(min(height[start], height[end]) * (end - start), maxArea)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return maxArea