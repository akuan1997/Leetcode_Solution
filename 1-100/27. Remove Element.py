class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        left = 0
        for right in range(n):
            if nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        return left