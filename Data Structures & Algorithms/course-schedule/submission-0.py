class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        # b -> a
        for a, b in prerequisites:
            graph[b].append(a)

        state = [0] * numCourses  # 0,1,2

        def dfs(course):
            if state[course] == 1:
                return False  # 发现环
            if state[course] == 2:
                return True   # 已确认无环

            state[course] = 1  # 标记为 visiting

            for nxt in graph[course]:
                if not dfs(nxt):
                    return False

            state[course] = 2  # 标记为 visited
            return True

        # 每门课都可能是一个连通分量
        for i in range(numCourses):
            if state[i] == 0:
                if not dfs(i):
                    return False

        return True