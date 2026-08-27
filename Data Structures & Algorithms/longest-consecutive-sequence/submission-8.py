class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numMap = {}
        for i, num in enumerate(nums):
            numMap[num] = i
        
        # Count longest consecutive sequence
        count = 0

        for i, num in enumerate(nums):
            loop = 1

            if num - 1 not in numMap:
                target = num + 1
                
                while target in numMap:
                    loop += 1
                    target += 1
                
                count = max(loop, count)
        
        return count

        # numSet = set(nums)

        # longest = 0

        # for num in numSet:
        #     if num - 1 not in numSet:
        #         current = num
        #         length = 1

        #         while current + 1 in numSet:
        #             current += 1
        #             length += 1
                
        #         longest = max(longest, length)
        
        # return longest

