class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        area = 0

        def dfs(r, c):
            #1.check boundaries
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 
            
            # 2. stop if warter or visited
            if grid[r][c] == "0" or (r, c) in visited:
                return

            # 3. mark as vistied
            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    area += 1
                    dfs(r, c)


        return area


