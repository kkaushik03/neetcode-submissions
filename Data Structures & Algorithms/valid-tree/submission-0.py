class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if(len(edges) != n-1):
            return False 
        adjacencyList = {}
        adjacencyList = {i: [] for i in range(n)}
        for a,b in edges:
            adjacencyList[a].append(b)
            adjacencyList[b].append(a)
        # this is where dfs happens 
        stack = [0]
        visited = set()
        while stack: 
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for neigh in adjacencyList[node]: 
                if neigh not in visited: 
                    stack.append(neigh)    
                        
        return len(visited) == n