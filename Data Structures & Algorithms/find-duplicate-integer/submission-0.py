class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ListMap = {}

        for i, num in enumerate(nums):
            if num in ListMap:
                return num
            else:
                ListMap[num] = i
            