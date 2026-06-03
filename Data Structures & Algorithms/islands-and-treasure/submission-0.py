class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def explore(row, col):
            q = deque([(row, col, 0)])
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            while q:
                r, c, lvl = q.popleft()
                print(f"{r} {c}")
                if r < 0  or r >= len(grid):
                    continue
                if c < 0 or c >= len(grid[r]):
                    continue
                if grid[r][c] < lvl:
                    continue

                grid[r][c] = lvl
                for dr, dc in directions:
                    q.append((dr + r, dc + c, lvl + 1))


        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    explore(r, c)