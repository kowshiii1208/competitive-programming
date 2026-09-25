class Solution:
    def minimumSum(self, num: int) -> int:
        nums = [i for i in str(num)]
        nums.sort()
        num1 = str(nums[0])+str(nums[2])
        num2 = str(nums[1])+str(nums[3])
        return int(num2)+int(num1)

        
