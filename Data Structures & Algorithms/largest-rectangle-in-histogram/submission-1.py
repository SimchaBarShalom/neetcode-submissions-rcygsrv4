class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxRectangleArea = 0  
        for i in range(len(heights)):
            h = heights[i] 
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                if not stack:
                    width=i
                else:
                    width=i-stack[-1] - 1
                maxRectangleArea = max(maxRectangleArea, height * width)
            stack.append(i)
        while stack:
            height = heights[stack.pop()]
            if not stack:
                    width=len(heights)
            else:
                width=len(heights) - stack[-1] - 1
            maxRectangleArea = max(maxRectangleArea, height * width) 
        return maxRectangleArea