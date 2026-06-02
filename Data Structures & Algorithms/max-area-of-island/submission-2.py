class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island = 0
        seen = set()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                max_island = max(
                    max_island,
                    self._explore(r, c, seen, grid)
                )
        
        return max_island
    
    def _explore(self, r, c, seen, grid):
        if r < 0 or r >= len(grid):
            return 0
        if c < 0 or c >= len(grid[r]):
            return 0
        if grid[r][c] == 0:
            return 0
        key = (r, c)
        if key in seen:
            return 0
        seen.add(key)

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]
        size = 1
        for dr, dc in directions:
            size += self._explore(r + dr, c + dc, seen, grid)
        
        return size
