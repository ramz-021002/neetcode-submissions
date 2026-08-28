class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numMap = {}
        for i, num in enumerate(nums):
            numMap[num] = i
        
        # Count longest consecutive sequence
        count = 0

        for i, num in enumerate(nums):
            loop = 1
            target = num + 1
            
            while target in numMap:
                loop += 1
                target += 1
            
            count = max(loop, count)
        
        return count

