class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        seen = set()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    island_count += self.explore(r, c, seen, grid)

        return island_count
    
    def explore(self, r, c, seen, grid):
        if r < 0 or r >= len(grid):
            return 0
        if c < 0 or c >= len(grid[r]):
            return 0
        if grid[r][c] == "0":
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

        count = 1
        for dr, dc in directions:
            self.explore(r + dr, c + dc, seen, grid)

        return count