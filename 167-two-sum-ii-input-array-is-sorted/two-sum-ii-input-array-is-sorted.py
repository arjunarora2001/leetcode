class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Binary search - O(log n)
        # Traverse through array - O(n)
        # For each element, try to find target - element using binary search
        # Overall - O(n log n)
        # Can optimize by not looking for redundant values
        start = 0
        end = len(numbers) - 1
        while (start < end):
            tmp = numbers[start] + numbers[end]
            if tmp == target:
                return [start + 1, end + 1]
            elif tmp > target:
                end -= 1
            elif tmp < target:
                start += 1
        return {-1, -1}