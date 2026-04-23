class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])

        pac = set()
        atl = set()

        pac_queue = deque()
        atl_queue = deque()

        # pac
        for r in range(rows):
            pac.add((r, 0))
            pac_queue.append((r, 0))

        for c in range(cols):
            pac.add((0, c))
            pac_queue.append((0, c))

        # atl
        for r in range(rows):
            atl.add((r, cols - 1))
            atl_queue.append((r, cols - 1))

        for c in range(cols):
            atl.add((rows - 1, c))
            atl_queue.append((rows - 1, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(queue, visited):
            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < rows and 0 <= nc < cols):
                        continue

                    if (nr, nc) in visited:
                        continue

                    if heights[nr][nc] < heights[r][c]:
                        continue

                    visited.add((nr, nc))
                    queue.append((nr, nc))

        bfs(pac_queue, pac)
        bfs(atl_queue, atl)

        return list(pac & atl)