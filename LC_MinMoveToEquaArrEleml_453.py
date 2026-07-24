class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m=min(nums)
        diff=0
        for i in nums:
            diff+=abs(i-m)
        return diff
