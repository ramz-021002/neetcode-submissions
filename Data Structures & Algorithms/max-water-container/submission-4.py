class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0

        # for i, h in enumerate(heights):
        #     l, r = i, len(heights) - 1
        #     while l < r:
        #         if heights[l] < heights[r]:
        #             area = max(area, (r-l)*heights[l])
        #             l += 1
        #         else:
        #             area = max(area, (r-l)*heights[r])
        #             r -= 1
        l, r = 0, len(heights) - 1
        while l < r:
            if heights[l] < heights[r]:
                area = max(area, (r-l)*heights[l])
                l += 1
            else:
                area = max(area, (r-l)*heights[r])
                r -= 1
        
        return area