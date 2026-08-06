class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range (len(edges)+1)]

        def parents(node): 
            while(parent[node]!=node):
                return parents(parent[node])
            return parent[node]
        
        for a,b in edges:
            parenta = parents(a)
            parentb = parents(b)
            if(parenta==parentb):
                return [a,b]
            parent[parenta] = parentb
        return []