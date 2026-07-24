class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # median
        nums.sort()
        n = len(nums)
        median = nums[n//2]
        return sum([abs(num-median) for num in nums])
