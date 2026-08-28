class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        keys = sorted(Counter(nums))
        return keys[-k:]