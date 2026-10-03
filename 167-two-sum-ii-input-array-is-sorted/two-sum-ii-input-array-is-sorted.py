class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        dic = {}
        for i in range(len(numbers)):
            if target-numbers[i] in dic.keys():
                return [dic[target-numbers[i]],i+1]
            else:
                dic[numbers[i]]=i+1

            
