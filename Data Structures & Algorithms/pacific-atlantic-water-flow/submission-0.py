class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])

        pac = set()
        atl = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, visited, prevHeight):
            if (
                r < 0 or c < 0 or r >= rows or c >= cols or
                (r, c) in visited or
                heights[r][c] < prevHeight
            ):
                return

            visited.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # from pacific
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])

        # from atl
        for r in range(rows):
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        for c in range(cols):
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        # intersection
        return list(pac & atl)

        