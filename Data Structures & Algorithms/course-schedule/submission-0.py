class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def get_indegree(prerequisites):
            # FIXED: init ALL courses to 0, else 0-prereq courses go missing
            indegree = {i: 0 for i in range(numCourses)}
            for i in prerequisites:
                indegree[i[0]] += 1   # (this line was already right: [a,b] means b->a, so a gets indegree)
            return indegree
        indegree = get_indegree(prerequisites)
        visited = set()

        stack = deque()
        # FIXED: seed with ALL zero-indegree nodes at once (was picking one via a broken outer loop)
        for item in indegree:
            if indegree[item] == 0:
                stack.append(item)

        # FIXED: removed the outer `for i in range(numCourses)` — Kahn's doesn't restart per course
        while stack:
            node = stack.pop()
            visited.add(node)
            for i in prerequisites:
                if i[1] == node:
                    indegree[i[0]] -= 1          # FIXED: was indegree[0], must be the neighbor i[0]
                    if indegree[i[0]] == 0:      # FIXED: enqueue neighbor when it hits 0
                        stack.append(i[0])

        return len(visited) == numCourses