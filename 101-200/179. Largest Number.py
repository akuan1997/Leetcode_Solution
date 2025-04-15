class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums.sort(key=lambda x:x*10, reverse=True)
        ans = ''.join(nums)
        return '0' if ans[0] == '0' else ans