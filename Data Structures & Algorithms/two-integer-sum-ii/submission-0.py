class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numsMap = {}

        for i, num in enumerate(numbers):
            complement = target - num

            if complement in numsMap:
                return [complement, num]
            
            numsMap[num] = i
        
        return []