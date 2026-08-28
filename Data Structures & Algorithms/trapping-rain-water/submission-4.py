class Solution:
    def trap(self, height: List[int]) -> int:
        # n = len(height)
        # prefix = [0] * n
        # suffix = [0] * n

        # for i in range(0, n):
        #     if i == 0:
        #         prefix[i] = height[i]
        #         suffix[-1] = height[-1]
        #     else:
        #         prefix[i] = max(height[i], prefix[i-1])
        #         suffix[n - 1 - i] = max(height[n - 1 - i ], suffix[n - i ])

        # Area 
        # To get the area where water can be stored we can find prefix and suffix of that index
        # for i-th position area = min(prefix[i], suffix[i]) - height[i]
        # area = 0
        # for i in range(0, n):
        #     if min(prefix[i], suffix[i]) - height[i] < 0:
        #         continue
        #     else:
        #         area += min(prefix[i], suffix[i]) - height[i]
        
        # return area


        l, r = 0, len(height) - 1 
        left_max = 0
        right_max = 0

        area = 0

        while l < r:
            if height[l] <= height[r]:
                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    area += left_max - height[l]
                
                l += 1
            else:
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    area += right_max - height[r]
                
                r -= 1
        
        return area

