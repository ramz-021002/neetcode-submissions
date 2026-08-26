class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Bruteforce approach
        # for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        
        # return False
        
        #Optimized for lists
        has_dup = len(nums) != len(set(nums))
        return has_dup

        #Optimized using dicts
        # numsMap = {}
        # for i, num in enumerate(nums):
        #     numsMap[i] = num
        
        # has_duplicates = len(numsMap.values()) != len(set(numsMap.values()))

        # return has_duplicates
