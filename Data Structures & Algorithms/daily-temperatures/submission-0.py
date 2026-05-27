class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        for i, tmp in enumerate(temperatures):
            if not stack or stack[-1][0] >= tmp:
                stack.append((tmp, i))
            else:
                while stack and stack[-1][0] < tmp:
                    t, idx = stack.pop()
                    res[idx] = i - idx
                stack.append((tmp, i))

        for tmp, i in stack:
            res[i] = 0
        
        return res