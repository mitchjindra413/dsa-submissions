class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_rectangle = float("-inf")

        for i, h in enumerate(heights):
            tmp_i = i
            while stack and stack[-1][1] > h:
                prev_i, prev_h = stack.pop()
                tmp_i = prev_i
                max_rectangle = max(max_rectangle, prev_h * (i - prev_i))
            stack.append((tmp_i, h))

        for i, h in stack:
            max_rectangle = max(max_rectangle, h * (len(heights) - i))
        
        return max_rectangle