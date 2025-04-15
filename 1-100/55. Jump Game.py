class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        n = len(nums)
        if n <= 1:
            return True

        for i in range(n):
            if i > max_reach:
                return False

            max_reach = max(max_reach, nums[i] + i)

            if max_reach >= n - 1:
                return True

        return True