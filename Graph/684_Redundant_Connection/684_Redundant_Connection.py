class DisjointSet:
    def __init__(self, n):
        self.n = n
        self.parent = {i: i for i in range(self.n)}
        self.rank = {i: 1 for i in range(self.n)}
        
    def find(self, n):
        if n != self.parent[n]:
            self.parent[n] = self.find(self.parent[n])
            
        return self.parent[n]
    
    def union(self, n1, n2):
        n1_root, n2_root = self.find(n1), self.find(n2)
        
        if n1_root == n2_root:
            return False
        
        if self.rank[n1_root] > self.rank[n2_root]:
            self.parent[n2_root] = n1_root
        elif self.rank[n2_root] > self.rank[n1_root]:
            self.parent[n1_root] = n2_root
        else:
            self.parent[n2_root] = n1_root
            
        return True
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        disjoint_set = DisjointSet(len(edges) + 1)
        
        for src, dst in edges:
            if not disjoint_set.union(src, dst):
                return [src, dst]
