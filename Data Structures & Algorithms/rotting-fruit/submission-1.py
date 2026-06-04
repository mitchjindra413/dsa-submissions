class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        oranges_count = 0
        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    oranges_count += 1
                elif grid[r][c] == 2:
                    q.append((r, c, 0))
        
        minutes = 0
        while q:
            r_fruit, c_fruit, lvl = q.popleft()
            minutes = max(minutes, lvl)
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            for dr, dc in directions:
                r = dr + r_fruit
                c = dc + c_fruit
                
                if r < 0 or r >= len(grid):
                    continue
                if c < 0 or c >= len(grid[r]):
                    continue
                if grid[r][c] == 1:
                    grid[r][c] = 2
                    oranges_count -= 1
                    q.append((r, c, lvl + 1))
                    
            
        
        if oranges_count == 0:
            return minutes
        else:
            return -1

        