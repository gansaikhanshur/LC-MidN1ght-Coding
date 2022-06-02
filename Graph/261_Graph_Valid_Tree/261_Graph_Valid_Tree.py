class DisjointSet:
    def __init__(self, n):
        self.n = n
        self.rank = {i: 0 for i in range(self.n)}
        self.parent = {i: i for i in range(self.n)}
        
    def find_parent(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find_parent(self.parent[n])
            
        return self.parent[n]
    
    def union(self, n1, n2):
        x_parent, y_parent = self.find_parent(n1), self.find_parent(n2)
        if x_parent != y_parent:
            if self.rank[x_parent] > self.rank[y_parent]:
                self.parent[y_parent] = x_parent
            elif self.rank[y_parent] > self.rank[x_parent]:
                self.parent[x_parent] = y_parent
            else:
                self.parent[y_parent] = x_parent
                self.rank[x_parent] += 1
                
            self.n -= 1
    
    
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        disjoint_set = DisjointSet(n)
        
        for edge in edges:
            src, dst = edge[0], edge[1]
            disjoint_set.union(src, dst)
            
        if disjoint_set.n == 1 and len(edges) == n - 1:
            return True
        return False
