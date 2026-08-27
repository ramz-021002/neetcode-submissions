class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numsMap = {}

        for i, num in enumerate(numbers):
            complement = target - num

            if complement in numsMap:
                return [numsMap[complement]+1, i+1]
            
            numsMap[num] = i
        
        return []